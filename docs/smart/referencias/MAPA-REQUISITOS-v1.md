# EOS-DENO · Mapa de Requisitos (consolidado) — Gate do Passo 2

> Consolidação fiel dos **5 blocos** do pacote `eos-deno-requisitos-produto-2026-06-30-CONF` (hardware, software, produtos, mercado, engenharia-DRAFT), reconciliada com a suite `docs/smart` (00–15). Preserva a taxonomia **[F]** fato c/fonte · **[E]** estimativa · **[H]** hipótese · **[INPUT]** placeholder. Detalhe por bloco em [`extracao/`](extracao/) (REQ-HW-*, REQ-SW-*, REQ-PROD-*, FATO-MKT-*, ENG-*).
>
> **Este é o artefato de gate.** Nada de PRD/ADR é escrito antes da sua revisão das decisões da **Parte E**.

---

## A. Síntese executiva & reenquadramento

1. **A venture é a EOS-DENO** (nome de trabalho; era "CORRENTE") — plataforma de energia **AI-native/operada por agentes**, BR, **spinoff de empresa-âncora** (Marcus = CPTO). O rótulo **"Smart"** da suite `docs/smart` era um nome anterior. **Marca = decision-gate ABERTO** (sem checagem de colisão).
2. **O v1 é uma fatia estreita e confirmada** — não a plataforma inteira. Aprendizado literal do STATE: *"não specar 'a plataforma' — specar a fatia mínima do beachhead"*.
   - **Beachhead = Integrador/EPC (produto P1).** Única persona que fecha unit economics **sem gatilho regulatório** [F]; funciona como máquina de CAC subsidiado das demais camadas.
   - **v1 = portal do integrador sobre o smart-meter EXISTENTE** (não o ODM próprio): **ingestão → time-series → modelo de ativo → portal (monitoramento + frota + comissionamento + diagnóstico remoto)**, com **camada de abstração de device (S2.3) desde a 1ª linha**.
   - **FORA do v1 (deliberado):** VPP, CCEE, agent-fabric, otimização, mercado livre, os 18 cenários.
3. **Build já decidido:** **fork OpenEMS** (EMS/edge) · **build-on ThingsBoard** (ingestão/multi-tenant/IoT) · EMHASS/PyPSA (otimização, fase-2). *Isto responde a antiga pergunta "fork vs greenfield": é fork/build-on.*
4. **Moat = dois tetos de mercado vazios:** **CCEE/BR** (liquidação/rateio nativos) e **agent-fabric AI-native (LLM)** — ambos **Fase-2+**, mas condicionam a arquitetura desde já (tenant-aware, modularização, device-abstraction).
5. **Redenção dos "repos side":** os repos [`energy-connectors`](../../../repos/energy-connectors/) (cloud-to-cloud) e [`energy-device-maps`](../../../repos/energy-device-maps/) (perfis Modbus) **NÃO são desvio** — eles **SÃO** a camada **S0.2 / S2.3 (abstração de device)** do v1. Passam a ser componentes-núcleo da fatia mínima do integrador, subordinados à plataforma.

> **Convergência forte:** a suite `docs/smart` é **o mesmo produto** que o EOS-DENO CONF, com mais detalhe de engenharia — mesmas 7 personas, mesmos 18 cenários, mesma DAL, mesmas fundações OSS, mesmo veredito build/fork/buy. Não há conflito de tese; há **diferença de altitude** (visão ampla vs. fatia v1) e alguns pontos a reconciliar (Parte D/E).

---

## B. Escopo V1 — requisitos consolidados (a fatia buildável)

> Deduplicado entre os blocos HW e SW (o mesmo requisito aparece nos dois com nomes diferentes). Organizado pelo fluxo do v1. Tag epistêmica + origem.

### B1. Abstração de device (S2.3) — *disciplina inegociável, 1ª linha*
| Requisito | Tag | Origem |
|---|---|---|
| **Protocol Adapter Registry / driver-model**: 1 driver por fabricante traduz Modbus/API proprietário → **modelo canônico** *capability-based*; resto do sistema fala uma língua só. | [F] | REQ-SW-02 (S0.2) = REQ-HW-01 = ENG-17 |
| **Modelo canônico de capacidades** (telemetry/setpoint/mode/schedule/meta). | [F] | REQ-SW-10 (S2.3); `docs/smart/05` (spec completa da DAL) |
| **Biblioteca de perfis versionada** por fabricante/modelo/firmware (semente; ampliar = Fase-2). | [E] | REQ-HW-02; repo `energy-device-maps` (perfil GoodWe g1 já ingerido) |
| **Onboarding de equipamento**: auto-detecção (varredura de barramento + registrador de modelo) + fallback manual; teste da **colisão Modbus 247**. | [E]/[F] | REQ-HW-03; ENG-18 |
| **Envelope canônico de telemetria versionado** (`schema_version, device_id, ts, kind, seq, payload, sig`). | [F] | ENG-04 |

> **Implementação = os dois repos.** `energy-device-maps` (perfis Modbus/SunSpec) + `energy-connectors` (APIs de nuvem, GoodWe 1º). Contrato canônico compartilhado já existe em ambos.

### B2. Ingestão (S0) & time-series (S1)
| Requisito | Tag | Origem |
|---|---|---|
| **Device Gateway/Connector**: ingerir telemetria via adaptadores Modbus/MQTT/REST + fila. | [F] | REQ-SW-01 (S0.1); REQ-HW-04..06 |
| **Edge Sync / store-and-forward**: buffer offline + idempotência. *No v1 vive cloud-side / no coletor do smart-meter de terceiro (não há borda própria).* | [F] | REQ-SW-03 (S0.3); REQ-HW-19 |
| **Command Dispatch Bus (base)**: entregar config/comando ao coletor com ack+retry — **só para comissionamento/config remota** (controle-otimizado é Fase-2). | [F] | REQ-SW-04 (S0.4) |
| **Time-Series Store**: TSDB **TimescaleDB** (⚠ Amazon Timestream LiveAnalytics fechou p/ novos clientes 20/06/2025 — ver D-F). | [F] | REQ-SW-05 (S1.1); `docs/smart/08:65` |
| **Telemetry API** (REST/GraphQL + cache) e **Event Bus** (pub/sub). | [F] | REQ-SW-06/07 (S1.4/S1.2) |

### B3. Modelo de ativo (S2)
| Requisito | Tag | Origem |
|---|---|---|
| **Asset Registry** (UCs, medidores, inversores, baterias, VE, cargas) + **Topology Model** (fase/circuito/UC↔usina) + **Digital Twin State** (estado tempo-real). | [F] | REQ-SW-08/09/11 (S2.1/2.2/2.4) |

### B4. Portal do Integrador (S12.2) — *superfície central do v1*
| Requisito | Tag | Origem |
|---|---|---|
| **Installer Portal (web SPA)**: comissionamento, diagnóstico remoto, gestão de frota, multi-cliente. | [F] | REQ-SW-12 (S12.2); REQ-HW-15/16; ENG-22 |
| **Fleet Manager** (agrupamento, rollout em ondas, health) + **Fleet Health/RMA**. | [F] | REQ-SW-13/14 (S6.1/S14.4); REQ-HW-17 |
| **Comissionamento sem-app (web/QR)** + auto-detecção de ativos. | [E] | REQ-HW-15 |

### B5. Multi-tenant, identidade & segurança (base)
| Requisito | Tag | Origem |
|---|---|---|
| **Modelo tenant-aware desde o dia 1** (multi-tenant base; white-label/theming adiado até o 2º tenant). | [F]/[E] | REQ-SW-16 (S9.2); ENG-08/C8 |
| **Auth OIDC (Keycloak/Ory)** + **RBAC por persona** (foco INT). | [F] | REQ-SW-15/17 (S9.1/9.3); `docs/smart/08` (matriz de roles) |
| **Identidade X.509 por device + Fleet Provisioning by claim** (fim do cert de frota compartilhado); **sem senha default global** (`1234` proibido). | [F-decisão] | ENG-06/08; REQ-HW-13 |
| **Criptografia/segredos + audit log append-only** de comandos/acessos. | [F] | REQ-SW-21 (S15); ENG-07 |

### B6. Infra mínima de sustentação
| Requisito | Tag | Origem |
|---|---|---|
| **Observabilidade** (Prometheus/Grafana/OTel), **CI/CD + cloud-native runtime (k8s)**, **API Gateway base + webhooks**. | [F] | REQ-SW-20/22/23 (S14/S16/S10) |
| **Fork OpenEMS + build-on ThingsBoard**; **modularização → bundles por persona** desde o dia 1. | [F-decisão] | REQ-SW-18/19/38 |

### B7. Contexto BR embutido (aterrar, não construir mercado)
| Requisito | Tag | Origem |
|---|---|---|
| **GD compartilhada é o mercado maduro** (~1,55 mi UCs, ~2.224 sistemas, 99,3% solar) → o portal precisa lidar com **frota FV multi-UC + comissionamento**. | [F] | FATO-MKT-02/03/04; REQ-PROD-05 |
| **Split-phase 127/254 V + zero-export/SCEE** como cidadãos de 1ª classe (leitura no v1; controle de zero-export exige borda → Fase-2). | [E] | ENG-19/20; REQ-HW context |

> **Nota crítica sobre "borda":** como o v1 lê um **smart-meter de terceiro**, **não há firmware/edge próprio no v1**. Store-and-forward, OTA de device, safety-loop e X.509 ou vivem **no device existente** ou são **cloud-side**. O que se constrói é **cloud + portal + camada de abstração/drivers**. Isso resolve o conflito de hardware (ver D-C).

---

## C. Backlog Fase-2+ (fora do v1 — resumo por domínio)

| Domínio | Conteúdo | Origem | Marco |
|---|---|---|---|
| **Forecasting (S3)** | solar/carga/preço/clima; build-on pvlib/EMHASS | REQ-SW-24 | M1 |
| **Otimização (S4)** | MILP/MPC, motor de tarifa (branca/bandeiras/dinâmica), multi-objetivo; OR-Tools/PyPSA/EMHASS | REQ-SW-25; REQ-HW-25 | M1 |
| **EMS/Controle (S5)** | control loop, **safety guardrails**, cenas/modos; **fork forte OpenEMS** | REQ-SW-26; REQ-HW-24 | M1 (guardrails podem subir — ver D-E/H) |
| **DERMS/Frota (S6.2–4)** | group control, sinais de rede, curtailment | REQ-SW-27 | M2 |
| **VPP/Mercado (S7)** | agregação, bidding, ancilares FCR/aFRR, DR; OpenADR | REQ-SW-28; REQ-HW-28 | M2 (monetização gradual [H]) |
| **CCEE/Billing BR (S8)** ⭐moat | integração CCEE, rateio Lei 14.300, liquidação ACL, billing; **build puro** | REQ-SW-29 | M2 |
| **Agent-fabric (S11)** ⭐moat | runtime de agentes LLM por persona, copilot NL, guardrails; build (inspirado Volttron) | REQ-SW-30 | M3 |
| **Apps consumidor (S12.1)** | Consumer App/mobile, engagement | REQ-SW-31 | Fase-2 (ver D-B) |
| **ODM próprio (hardware)** | medidor universal + Energy Hub premium; Linux AP + MCU safety; break-even ~35% adoção [E] | REQ-HW-20; ENG-10 | M0/Fase-2 |
| **Edge/firmware próprio** | store-and-forward SQLite, OTA A/B, safety-loop, BLE comissionamento offline | ENG-05/07/09/23/26 | com o ODM |
| **VE/bomba de calor** | OCPP/smart-charging/V2G; SG-Ready/EEBUS | REQ-HW-23 | M1 |
| **Demais** | Data Lake, MLOps (S13), SDK/marketplace (S10.3-4), white-label (S9.4), comercial (S17) | REQ-SW-32..37 | Fase-2+ |
| **18 cenários (A1–C5)** | exigem forecasting/otimização/EMS/VPP/CCEE | REQ-SW-cenários | Fase-2+ |

---

## D. Reconciliação `docs/smart` ↔ EOS-DENO CONF

| Situação | Itens |
|---|---|
| ✅ **Alinhado** (mesma substância) | 7 personas (CON/INT/COM/AGG/GER/DSO/ORQ) · 18 cenários A/B/C×N0–N5 · **DAL/S2.3** (`docs/smart/05` = spec da abstração) · fundações OSS e veredito build/fork/buy · multi-tenant desde a fundação (`08` matriz de roles) · fluxo ingestão→time-series→modelo de ativo (`03`,`04`) |
| 🔼 **Supera / atualiza** | **BESS regulamentado ANEEL 02/jun/2026** (supera o `[VERIFICAR]` de `docs/smart/02 §7`) · **Timestream fechou → TimescaleDB** (`08:65`) · camada quantitativa de mercado (UCs/GW/TAM) que faltava em `02` |
| 🔤 **Nomenclatura** (mapear, sem conflito) | nomes de produto de `docs/smart/08` ↔ taxonomia S0–S17 (DAL↔S2.3, Ingestão↔S0/S1, Otimização↔S3/S4, EMS↔S5, VPP↔S6/S7, Billing/Rateio↔S8, IAM↔S9, API↔S10, Observ.↔S14) |
| ⚠️ **Conflito / decisão** | **C1 tese de hardware** (medidor billing-grade-moat vs Gateway+Meter-commodity) · **MVP: INT-only (CONF) vs CON+INT (`01`)** · **agent-fabric ausente do roadmap `12`** · **marca "Smart" vs "EOS-DENO"** · **A/B/C**: STATE (dono-book/operador-white-label/distressed) ≠ `docs/smart/15` (HW+SaaS/HaaS/canal) |

---

## E. Decisões para o gate (recomendação marcada) — **preciso do seu OK**

| # | Decisão | Opções | Recomendação |
|---|---|---|---|
| **D-A** | **Marca / naming nos docs** | (a) manter suite `docs/smart` como está (legado "Smart") e escrever **PRD/ADR novos sob "EOS-DENO"**, sem renomear em massa até o gate de marca fechar; (b) renomear tudo agora Smart→EOS-DENO | **(a)** — marca é gate aberto; não faço rename em massa. Uso "EOS-DENO" (nome de trabalho) nos novos artefatos, registro em ADR. |
| **D-B** | **Escopo do MVP** | (a) **INT-only** (portal do integrador; Consumer App = Fase-2); (b) CON+INT (inclui app do consumidor no v1) | **(a)** — coerente com STATE/README; o que o consumidor "vê" chega pelo portal do integrador. |
| **D-C** | **Tese de hardware (C1)** | (a) **v1 NÃO constrói hardware** — lê o smart-meter existente; a disputa "billing-grade-moat vs Gateway+Meter-commodity" vira decisão do **ODM (Fase-2)**; (b) decidir a tese de HW agora | **(a)** — destrava o v1 sem travar a decisão de ODM. |
| **D-D** | **Colisão A/B/C** | (a) adotar o esquema do **STATE** (A dono-do-book / B operador-white-label / C distressed) como canônico e aposentar o A/B/C de `docs/smart/15`; (b) manter os dois | **(a)** — um só esquema; o de `15` era proposta anterior. |
| **D-E** | **Bootstrap do v1** | (a) construir v1 **sobre ThingsBoard** (ingestão/multi-tenant/IoT) + os 2 repos (device-abstraction), **adiando o fork OpenEMS** para quando entrar controle/EMS; (b) forkar OpenEMS já no v1 | **(a)** — ThingsBoard cobre o grosso do v1; OpenEMS é EMS/controle (Fase-2). |
| **D-F** | **TSDB** | **TimescaleDB** (Timestream LiveAnalytics fechou); confirmar região sa-east-1 | **TimescaleDB.** |
| **D-G** | **Guardrails de safety (S5.2) no v1?** | Se o portal emitir **qualquer** comando/config remota, pode precisar de interlocks antes do EMS completo | **[H] a decidir** — provável **sim, mínimo** (validação de comando na borda/coletor). |

---

## F. Gaps & artefatos faltantes (preciso de você / ação minha)

1. **`receitas-energia-br.md` (REV-01) não está no repo** — é a fonte declarada de **R-01…R-13**; R-01…R-11 foram reconstruídos da matriz de produtos. → **subir o arquivo** (ou confirmar que os R-* da matriz bastam). R-12/R-13 autorizadas mas a refletir no REV-01 (gate aberto no STATE).
2. **`eos-deno-unit-economics-top5.xlsx`** (binário) — tem os números de LTV:CAC/payback/deflator que hoje são só `[E]/[INPUT]`. → **posso converter agora via `markitdown`** (MCP disponível) e anexar em markdown. *Autoriza?*
3. **Protótipo de DERMS herdado (D5)** — a spec diz "já existe", mas **nenhum artefato localizado no repo**. → **onde está?** (impacta o quanto se herda vs constrói).
4. **Repos `energy-connectors`/`energy-device-maps`** — confirmo que **entram como componentes V1** (a camada S0.2/S2.3), não "estacionados". (Recomendo sim.)

---

## G. [INPUT]/[H] a validar (descoberta com 2–3 integradores, em paralelo ao build)

- **[H] Win-rate no beachhead vs incumbentes** (Thunders/Clarke/Way2) — *maior lacuna de inteligência atual*; bake-off do P1 (win-rate <20% invalida). (bear #3)
- **[INPUT] Preços P1** (R$1–5/usina/mês; R$200–1.500/mês/integrador) e **P2** (R$2–6/UC/mês).
- **[H] Apetite do integrador BR sem gatilho regulatório** (risco banana-com-banana: benchmarks AU/EU são mercados mandatados).
- **[H] Agnosticismo = passivo de engenharia perpétuo** — priorizar as marcas que cobrem ~80% da base BR.
- **[H] Receita de flexibilidade/VPP no BR pode não existir** (não só estar vazia) — não modelar M2 como receita certa.

---

### Anexos (detalhe por bloco, fiel às tags)
- [`extracao/REQ-01-mercado.md`](extracao/REQ-01-mercado.md) · [`REQ-02-hardware.md`](extracao/REQ-02-hardware.md) · [`REQ-03-software.md`](extracao/REQ-03-software.md) · [`REQ-04-produtos.md`](extracao/REQ-04-produtos.md) · [`REQ-05-engenharia-DRAFT.md`](extracao/REQ-05-engenharia-DRAFT.md)

> **Próximo passo (após seu OK nas decisões D-A…D-G):** redijo o **PRD** (Visão da plataforma + Escopo v1 do integrador) e os **ADRs iniciais** (device-abstraction S2.3; build-on ThingsBoard; fork OpenEMS diferido; fronteira v1/Fase-2; smart-meter existente→ODM; marca=gate; TSDB).
