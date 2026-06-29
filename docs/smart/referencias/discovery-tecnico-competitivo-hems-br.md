# Relatório de Discovery Técnico-Competitivo: HEMS Brasileiro derivado do GoodWe EzManager3000

> **Estudo de referência curado pelo usuário.** Reproduzido em `referencias/`. Ver mapa de absorção em [00-absorcao-e-ajustes.md](00-absorcao-e-ajustes.md).

> **Natureza:** fase de discovery/pesquisa que precede a escrita dos documentos de engenharia (Arquitetura, Hardware, Firmware, Cloud, Backend, APIs, Contratos de interface). Relatório fundamentado que alimenta as ADRs sobre topologia de hardware, divisão edge/cloud, escolha de medidor, trilha de certificação e design de APIs.

## TL;DR
- **Padrão dominante = "HEMS híbrido":** gateway de borda faz medição, controle local de safety e store-and-forward offline; otimização/AI e agregação VPP rodam na nuvem — modelo de gridX (gridBox + XENON), Kiwigrid (Energy Manager + KiwiOS X), SolarEdge ONE e do próprio GoodWe EzManager/SEMS+. Para o Brasil, é o caminho recomendado, com a ressalva de que o **laço de safety zero-export deve ficar 100% na borda**, independente de RTT à nuvem.
- **Trilha regulatória BR tratável e até favorável:** zero-export ("grid zero") dispensa análise de inversão de fluxo (**REN ANEEL 1.098/2024**); **ANATEL** obrigatória para rádio 4G/WiFi/BLE (**Res. 715/2019**); **INMETRO** mudou para **Declaração de Conformidade** do fornecedor (**Portaria 657/2025**, vigente 01/01/2026) — favorece medidor OEM externo já certificado (Eastron/Acrel).
- **Três decisões de alto impacto:** (1) **Amazon Timestream for LiveAnalytics fechou para novos clientes em 20/06/2025** — usar Timestream for InfluxDB ou TimescaleDB; (2) otimização por tarifa no BR não tem mercado spot residencial (usar Tarifa Branca + SCEE, não §14a alemão nem preços dinâmicos europeus); (3) VPP/FTM residencial BR ainda carece de marco de agregador — projetar "VPP-ready" mas monetizar via autoconsumo e Tarifa Branca.

## Key Findings
1. **Arquitetura de referência:** edge+cloud híbrido é o padrão. Gateway de borda garante latência baixa, operação offline e isolamento de safety; a nuvem concentra AI/forecast, dashboards multi-tenant, OTA e VPP. GoodWe EzManager3000 segue o padrão.
2. **Topologia de hardware:** dois domínios — SoC Linux (aplicação/conectividade) + MCU/domínio de tempo real (laço crítico). SoCs como NXP i.MX, TI Sitara AM62x e ST STM32MP2 (Cortex-A35 + Cortex-M33).
3. **Conectividade 4G + ANATEL:** Quectel EG915U-LA (variante Latin America) com certificação ANATEL listada; qualquer 4G/WiFi/BLE exige homologação ANATEL (Res. 715/2019).
4. **Medidor OEM:** Eastron (SDM630 trifásico classe 0.5S, SDM120 monofásico classe 1) e Acrel (ADL200 mono, ADL400 trifásico classe 0.5) — ~R$100 CIF, Modbus RTU RS485, versões CT-operated para split-phase BR.
5. **Regulação BR:** zero-export dispensa estudo de inversão de fluxo; INMETRO migrou para autodeclaração; medição segue PRODIST Módulo 5 e portarias INMETRO.
6. **AWS IoT:** Fleet Provisioning by claim p/ dispositivos DIY; X.509 por dispositivo + IoT policy com policy variables (multi-tenant); Greengrass v2 stream manager para store-and-forward offline.
7. **Otimização/AI:** forecasting (LSTM/CNN) e scheduling (MILP/MPC determinístico vs RL/metaheurísticas). Edge para controle rápido, cloud para forecast/treino.
8. **Open-API:** GoodWe Open-API tem três tipos (OpenAPI de dados de negócio via HTTPS; Real-time Data via raw/Kafka; Batch Remote Control via Kafka — suporta VPP/microgrid). Padrões: SunSpec Modbus (local), IEEE 2030.5/CSIP (DER-utility), OpenADR (DR), EEBus.
9. **Panorama Brasil:** GD solar entre as maiores do mundo (>55 GW solar total em mar/2025; ~37,4 GW de GD em >2 milhões de sistemas — Rodrigo Sauaia/ABSOLAR), mas gestão inteligente/VPP incipiente; pilotos por AES Brasil, CPFL, Neoenergia, Comerc, Eletrobras, Auren (P&D VPP II). Falta marco de agregador e mercado de flexibilidade residencial.

## Details (por eixo)

### Eixo 1 — Arquiteturas de referência (edge vs cloud)
Consenso de engenharia: divisão híbrida edge+cloud é o padrão.
- **gridX (XENON + gridBox):** gateway local essencial; flash previne perda em queda; funciona independente da nuvem do OEM; offline até ~10 dias; otimização na nuvem (Cloud Optimization API) ou local; tarifa-agnóstico, modular.
- **Kiwigrid (KiwiOS X + Energy Manager):** gateway é a interface entre dispositivos e a plataforma (leitura e escrita); gateways VoyagerX e Rail; nuvem com APIs de otimização e previsão PV; PaaS pay-per-use.
- **SolarEdge ONE:** EMS com AI; plano de 24h; "Negative Rate Optimization" muda inversor p/ Zero Export; ONE Controller (2024) p/ controle de cargas de terceiros; VPP e grid services.
- **Victron (Cerbo GX + Venus OS):** gateway dual/quad-core, Venus OS (Linux), broker MQTT embutido, API VRM, Node-RED (Venus OS Large) — plataforma programável de borda.
- **Enphase (IQ Gateway/Envoy):** ponte microinversores↔Enlighten cloud; metering integrado; modem celular obrigatório p/ Ensemble.
- **GoodWe (EzManager3000 + SEMS+):** "cérebro" conecta solar/ESS/EV/bombas/cargas via Shelly; AI embarcada conecta a marketplaces; SEMS Portal cloud-based com delay (não tempo real garantido).
- **Huawei (FusionSolar + SmartLogger/SmartDongle):** Modbus TCP local (porta 502) com limitação — habilitar Modbus TCP local pode bloquear o envio à nuvem (conflito cloud-vs-local); polling ≥5s.

**Implicação BR:** modelo híbrido é o alvo; borda autossuficiente p/ safety e offline; nuvem AWS concentra otimização, multi-tenant e VPP.

### Eixo 2 — Arquitetura de borda (SoC, OS, safety, OTA)
- **Dois domínios:** domínio determinístico (MCU/Cortex-M) p/ safety (zero-export/anti-backfeed) separado do domínio de aplicação (Linux/Cortex-A). Ex.: ST STM32MP2 (A35 + M33). TI Sitara AM62x p/ IoT/gateway.
- **SO embarcado:** Yocto (multi-SKU, SBOM, package feeds, compliance) vs Buildroot (simples, appliance single-purpose). HEMS multi-SKU → Yocto tende a ser melhor. Zephyr no MCU de safety.
- **OTA/secure boot/store-and-forward:** secure/measured boot, rootfs verificado (dm-verity), assinatura, A/B updates, CVE tracking. gridBox usa flash (até 10 dias offline). AWS Greengrass stream manager faz buffer local.
- **Isolamento do laço de safety:** zero-export garantido na borda, independente de nuvem.

### Eixo 3 — Conectividade 4G e ANATEL
- **Quectel EG915U series** (LTE Cat 1) tem **EG915U-LA** (Latin America) com bandas LTE-FDD + GSM e certificação FCC/Anatel listada. Quectel investe em homologação ANATEL.
- **Res. ANATEL 715/2019:** homologação é pré-requisito obrigatório p/ comercialização; produtos com rádio precisam de homologação via OCD. Certificação FCC/estrangeira NÃO substitui ANATEL.
- **Módulo pré-certificado** reduz escopo, mas o dispositivo integrado ainda requer homologação. DIY com celular embutido → homologação inescapável; planejar SIM/eSIM M2M.

### Eixo 4 — Medidores OEM Modbus (~R$100 CIF)
- **Eastron SDM630:** trifásico, até 100A (ou MCT com TC), 1P2W/3P3W/3P4W, **classe 0.5S**, bidirecional, RS485 Modbus RTU + pulse, DIN 4 módulos, MID B+D. Até ~30 dispositivos por barramento.
- **Eastron SDM120:** monofásico, 1 módulo, classe 1, RS485 Modbus + pulse, MID B+D.
- **Acrel ADL series:** ADL200 mono (classe 1), ADL400 trifásico (classe 0.5, split-phase, demanda, 31º harmônico, registro 48 meses), ADL200N-CT com TC 80-300A. IEC62053-21/22, EN50470.
- **Split-phase BR (127/254V):** medidores 1P2W e configuráveis (SDM630) e Acrel atendem; preferir CT-operated.
- **INMETRO:** Portaria 657/2025 (vig. 01/01/2026) substitui Verificação Inicial por Declaração de Conformidade — facilita medidor OEM importado com DC, exige autorização prévia.

### Eixo 5 — Regulação e certificação Brasil (2026)
- **REN 1.000/2021 + inversão de fluxo (Art. 73):** a **REN 1.098/2024** (DOU 31/07/2024) definiu **três cenários onde a análise de inversão de fluxo é dispensada**: (1) micro/minigeração que NÃO injeta ("grid zero"); (2) microgeração com gratuidade e geração compatível com consumo; (3) autoconsumo local até 7,5 kW. **Favorável ao zero-export.**
- **Lei 14.300/2022 + SCEE:** créditos expiram em 60 meses (REN 1.059/2023, Art. 655-L). Sem mercado spot residencial — moeda = crédito de compensação (kWh) + regra de transição da TUSD/Fio B.
- **PRODIST:** Módulo 5 (Medição) e Módulo 8 (Qualidade); ABNT NBR 14519/14520 e portarias INMETRO (493/2021 medidores ativos, 587/2012 EMC).
- **INMETRO Portaria 657/2025** (DOU 15/10/2025, vig. 01/01/2026): Declaração de Conformidade do fabricante/importador autorizado substitui Verificação Inicial; verificações periódicas/pós-reparo permanecem. Autorização até 30/11/2025 (ref. Portaria 295/2021).
- **INMETRO equipamentos FV:** Portaria 140/2022 (substituiu 004/2011) via DC; inversores >10 kW isentos de registro (mudança em curso p/ até 75 kW). Inversores com WiFi/BT também precisam de ANATEL.
- **Não usar §14a alemão (RCR):** construto alemão (controle grid-friendly pelo DSO), irrelevante no BR. Lógica BR = zero-export + SCEE + Tarifa Branca.

### Eixo 6 — AWS IoT para fleet de energia
- **Fleet Provisioning:** JITP/JITR, Multi-Account Registration, e **Fleet Provisioning by claim/trusted user**. By claim: cert de "claim" por lote, trocado por X.509 único no 1º connect + Lambda pre-provisioning hook validando serial/MAC. By trusted user: instalador via app (cert temporário 5 min).
- **Identidade X.509 + multi-tenant:** cert por dispositivo + IoT policy de menor privilégio; **policy variables** (`${iot:Connection.Thing.ThingName}`) escalam a milhares; topic design com 2º campo imutável por dispositivo.
- **Greengrass v2:** componentes versionados, Token Exchange Service + IAM role alias, **stream manager** p/ store-and-forward offline (export p/ Kinesis/S3/SiteWise). Ressalva: Greengrass não encripta stream em repouso/trânsito entre componentes locais.
- **Telemetria — DECISÃO CRÍTICA:** **Timestream for LiveAnalytics fechou p/ novos clientes em 20/06/2025**. Opções: (a) **Timestream for InfluxDB** (gerenciado; InfluxDB 3 Core/Enterprise out/2025); (b) **TimescaleDB** (PostgreSQL + hypertables, compressão columnar 90-95%, full SQL p/ join multi-tenant; modo multi-node descontinuado — sharding app-level). Ingestão: IoT Core rule action (baixo volume) ou Greengrass stream manager (alto volume).
- **IoT SiteWise:** asset models, property alias, SiteWise Monitor, ExecuteQuery, SiteWise Edge — possivelmente overhead p/ fleet residencial simples.
- **Multi-tenant data isolation:** topic namespaces per-tenant + policy variables (ingest) + silo/pool/hybrid no store. Reference architectures de energia AWS ainda retratam Timestream LiveAnalytics — o padrão de ingestão permanece, mas o destino deve ser InfluxDB/TimescaleDB/Aurora.

### Eixo 7 — Otimização e AI em HEMS
- **Métodos (2024-2026):** forecasting com deep learning (LSTM, CNN-LSTM, MLP-ANN); SVM p/ anomalia. Scheduling: determinístico (MILP, MPC — ótimo global, escala mal) vs estocástico/data-driven (RL, metaheurísticas — escalam melhor).
- **Onde roda:** receding horizon 5-15 min. Forecast/treino na nuvem; controle rápido e setpoints na borda.
- **Contexto BR — diferenças cruciais:**
  - **Sem mercado spot residencial:** alavancas = **Tarifa Branca** (ponta ~18h-21h, intermediário 1h antes/depois) e **SCEE** (créditos kWh, validade 60 meses).
  - **Tarifa Branca:** opcional Grupo B; vantajosa só p/ quem desloca consumo p/ fora-ponta.
  - **Autoconsumo + zero-export:** otimização foca maximizar autoconsumo instantâneo e usar bateria p/ evitar import na ponta, não arbitragem de exportação.
  - **FTM/VPP:** oportunidade futura, sem mercado de flexibilidade residencial.

### Eixo 8 — Open-API e ecossistema
- **GoodWe Open-API (referência):** três tipos via HTTPS e Kafka:
  - **OpenAPI:** dados de negócio processados pelo SEMS, HTTPS, 4 interfaces (plant, device, remote control, datalogger), limite default ~3600 chamadas/h.
  - **Real-time Data Monitoring API:** dados raw, aberto a terceiros (conta de API, license agreement, whitelist, autorização do usuário final); múltiplos inversores; **não** suporta controle remoto.
  - **Batch Remote Control API:** controle remoto via Kafka (6 interfaces). **Usado com Real-Time Data p/ VPP e Microgrid.**
- **Padrões:** SunSpec Modbus (local); IEEE 2030.5/CSIP (DER-utility, mandatório CA Rule 21, HI, AUS CSIP-AUS com DOE; PKI/ECC; certificação 8-16 semanas); OpenADR (DR); IEEE 1547-2018/1547.1 (exige SunSpec/2030.5/DNP3); EEBus. São complementares.
- **Implicação BR:** sem mandato de IEEE 2030.5/CSIP hoje. V1 = Open-API própria (raw/processed/batch); projetar p/ futura compatibilidade 2030.5/OpenADR ("VPP-ready").

### Eixo 9 — Panorama competitivo Brasil
- **Mercado:** >55 GW solar total em mar/2025 (22,2% da matriz); ~37,4 GW de GD em >2 milhões de sistemas (ABSOLAR). 6º país em capacidade solar acumulada (66,7 GW até dez/2024). GD saltou de <1 GW (2018) p/ 40 GW (jun/2025) — 43% das adições do período (U.S. EIA). Gestão inteligente/VPP incipiente.
- **Armazenamento (BESS):** 269 MWh novos em 2024 (685 MWh acum.); leilão dedicado a baterias em 2025. Regulação inicial.
- **VPP/agregadores:** P&Ds (AES, CPFL, Neoenergia, Comerc, Eletrobras, Auren VPP II); acesso ao mercado p/ ativos residenciais "está por construir". Falta agregador, mercado de flexibilidade, interoperabilidade, regras de medição/liquidação p/ pequenos ativos.
- **Benchmarks:** Next Kraftwerke (>13.500 MW agregados; Shell); Tesla VPP (South Australia); U.S. DOE ("80-160 GW de VPPs até 2030 reduziria custos em US$10 bi/ano").
- **Modernização:** abertura do mercado livre, varejista, resposta à demanda, digitalização. Troca nacional de medidores BT até 2035 (Portaria Normativa 126/2026, ~2%/ano).
- **Oportunidade:** HEMS DIY plug-and-play multi-tenant com 4G nativo, multi-inversor, zero-export nativo e plataforma white-label endereça um gap — a maioria é amarrada a um OEM. Independência de OEM (estilo gridX/Kiwigrid) é o diferencial central.

## Recommendations

**Fase 0 — ADRs imediatas**
1. **Topologia de hardware:** dois domínios — SoC Linux (i.MX/AM62x/STM32MP2) + MCU/Cortex-M p/ safety zero-export determinístico. Se anti-injeção exigir <100ms garantido e isolamento de falhas, dois processadores; se o inversor já faz anti-backfeed nativo, um SoC pode bastar (reavaliar).
2. **Divisão edge/cloud:** borda autossuficiente p/ medição + safety + store-and-forward (alvo ≥7 dias offline; benchmark gridX 10 dias); nuvem p/ forecast/AI, multi-tenant, OTA, VPP. Safety NUNCA depende de RTT à nuvem.
3. **Medidor:** Eastron SDM630 (trifásico/CT, 0.5S) e SDM120/Acrel ADL200 (mono) como SKUs OEM externos via Modbus RTU. Validar CIF ≤R$100 e split-phase 127/254V.
4. **Stack de telemetria AWS:** NÃO usar Timestream LiveAnalytics. Decidir entre Timestream for InfluxDB e TimescaleDB (Aurora/Tiger Cloud). Inicial: TimescaleDB se o time domina PostgreSQL e precisa de joins ricos; senão Timestream for InfluxDB.
5. **Trilha de certificação:** (a) ANATEL via OCD usando módulo Quectel EG915U-LA pré-homologado; (b) INMETRO via Declaração de Conformidade (657/2025); (c) medidor OEM com DC própria ou do importador.
6. **Design de API:** espelhar GoodWe (raw/processed/batch) com HTTPS + streaming (MQTT/Kafka), policy de menor privilégio multi-tenant, camada de controle "2030.5/OpenADR-ready" sem implementar agora.

**Fase 1 — v1 (go-to-market BR)**
7. Otimização v1: regras + MILP/MPC horizonte deslizante (5-15 min) focado em **autoconsumo + evitar ponta na Tarifa Branca**, com forecast LSTM/CNN-LSTM na nuvem. Não assumir preços spot.
8. Fleet provisioning: by claim (cert por lote) com Lambda hook; ou by trusted user via app do instalador. Greengrass v2 + stream manager offline.
9. SO: Yocto (multi-SKU, SBOM, OTA A/B, secure boot, dm-verity).

**Fase 2 — VPP/FTM (quando o marco evoluir)**
10. Acompanhar regulação ANEEL de agregador/flexibilidade e BESS. Gatilho: marco de agregador residencial ou mercado de flexibilidade → ativar VPP (estilo GoodWe Batch Remote Control + Real-time Data). Até lá, "VPP-ready" sem custo regulatório.

**Benchmarks que mudam decisões**
- Se ANEEL exigir IEEE 2030.5/CSIP → priorizar stack 2030.5.
- Se CIF do medidor integrado certificado <R$100 → reavaliar medição integrada.
- Se Timestream for InfluxDB limitar escala/custo → migrar p/ TimescaleDB (ou vice-versa).

## Caveats
- **Incerteza de VPP/agregador BR:** sem marco definido; monetização FTM/VPP residencial é prospectiva. Confirmar com texto regulatório vigente.
- **Timestream end-of-sale:** 20/06/2025 (maintenance mode, fechado a novos). Confirmar disponibilidade de Timestream for InfluxDB no sa-east-1.
- **ANATEL do módulo Quectel:** datasheet marca certificação com "*" (em curso) — verificar no painel ANATEL.
- **Métricas de otimização:** valores variam por estudo — citar fonte primária antes de usar.
- **Registradores Modbus:** fora de escopo (já implementados pelo time).
- **GoodWe Open-API:** doc oficial parcialmente restrita; validar contra community.goodwe.com / doc oficial.
- **Arquitetura interna de concorrentes:** inferências de datasheets/manuais; tratar fontes blog/revenda como indicativo.
- **Split-phase BR:** varia por região; validar por região-alvo.
- **Custos/prazos de certificação:** não quantificados — orçar antes do go/no-go.
- **Dados de mercado (GD, BESS):** ABSOLAR/EIA/Energy Tracker Asia; revalidar na data de escrita.
