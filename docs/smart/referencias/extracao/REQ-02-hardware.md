> Extração fiel (subagente) do bloco. Fonte: docs/smart/referencias/produto/eos-deno-requisitos-produto-2026-06-30-CONF/. Preserva taxonomia [F]/[E]/[H]/[INPUT].

I now have the reconciliation point clearly. This is a significant conflict worth flagging: the `02-hardware` block (referenced by my prompt) treats the smart-meter as a **billing-grade Classe 1/2 native meter that IS the sensor/moat** ("o EOS-DENO é o medidor"), while `docs/smart/06` reframes hardware as **Smart Gateway (control by signal) + Smart Meter (commodity, <1%, EMS-grade not billing)**. I have everything needed to produce the extraction. Let me capture the key figures precisely before writing.

I have enough to produce the faithful extraction now.

---

# EOS-DENO · Bloco 02-hardware — Extração de Requisitos (FIEL)

## 1. Resumo do bloco

O bloco 02-hardware descreve o **device** do EOS-DENO por três lentes complementares: (a) uma **matriz de funcionalidades** — árvore de engenharia de um EMS/HEMS/VPP/DER "de classe mundial" com 10 camadas núcleo (00–09) + módulo C&I + horizonte 2030, cada item com *o quê* (destino) e *como* (mecanismo); (b) um **scoring 0–4** de 11 players contra essa matriz; e (c) uma **spec "Herdar/Alcançar/Ocupar"** que ordena o esforço por risco. O achado central é **cirúrgico**: o smart-meter existente **já detém o teto** em Medição (00), Hardware (08) e Conformidade-BR (07 por ausência de concorrente), e está no **chão absoluto (0)** em Inteligência (04) e VPP (05). A disciplina inegociável do v1 aparece codificada como capacidade **02.7 ★ Agnosticismo de fabricante** (camada de driver/modelo canônico) — a mesma coisa que o STATE chama de "camada de abstração de device (S2.3) desde a 1ª linha". A matriz e a spec ainda carregam vocabulário AI-native/VPP/CCEE que está **fora do v1** e serve de contexto de roadmap (M2/M3). **Ponto quente de reconciliação:** este bloco trata o smart-meter como **medidor billing-grade Classe 1/2 que É o sensor/moat**, enquanto `docs/smart/06` o reescreve como **Smart Gateway (controle por sinal) + Smart Meter commodity <1% (grau-EMS, não faturamento)** — divergência de tese de produto, detalhada na seção 4.

## 2. Requisitos

> Convenção: enunciado curto · tag epistêmica · relevância · fonte. As tags [F]/[E]/[H]/[INPUT] são atribuídas pela natureza do conteúdo nos docs de origem (os docs de matriz/spec não taggeiam item-a-item; o scoring é explícito sobre fidelidade de fonte — ver 3.x). Onde o doc-fonte afirma um nível de scoring validado, marco **[F] (scoring)**; onde é destino de engenharia idealizado, **[E]**; onde depende de mercado/regulação em construção, **[H]**.

### V1 — a fatia a construir (device-abstraction + telemetria do smart-meter existente + Energy Hub attach)

| REQ | Enunciado | Tag | Relevância | Fonte |
|---|---|---|---|---|
| **REQ-HW-01** | **Camada de abstração de device (driver layer)**: um driver por fabricante traduz o mapa Modbus/API proprietário para um **modelo de dados canônico**; o resto do sistema fala uma só língua. *É o S2.3 do STATE — 1ª linha.* | [F] (scoring: smart-meter=3) | **V1** | matriz §02.7.1; scoring §3.1 (agnost.=3); spec §02.3 (3→4) |
| **REQ-HW-02** | **Cobertura multimarca versionada**: biblioteca de perfis de equipamento, cada perfil um arquivo de mapeamento testado em lab (dezenas→centenas de marcas). | [E] | **V1** (semente; ampliar é Fase-2+) | matriz §02.7.2; spec §02.3 |
| **REQ-HW-03** | **Onboarding de equipamento**: auto-detecção por varredura de barramento + registrador de modelo; fallback manual ("Outros"); processo de certificação de novo device. | [E] | **V1** | matriz §02.7.3 |
| **REQ-HW-04** | **Medição elétrica nativa** (fonte de verdade do v1): V(L-N/L-L), I, P/Q/S, FP, freq, energia import/export, THD, desequilíbrio; amostragem simultânea V+I a kHz via metering IC/DSP. | [F] (scoring: 00=3, lidera) | **V1** | matriz §00.1.1; spec §02.1; scoring §2 (teto 00=3, smart-meter detém) |
| **REQ-HW-05** | **Resolução temporal multi-escala**: sub-segundo (transitórios), 1s (controle), 1–15min (telemetria) com agregação configurável. *Base da ingestão→time-series.* | [E] | **V1** | matriz §00.1.5 |
| **REQ-HW-06** | **Telemetria tempo-real + histórico** com granularidade/retenção configurável (time-series DB, streaming WebSocket). | [E] | **V1** | matriz §06.3.1 |
| **REQ-HW-07** | **Comando de inversor FV** (leitura + curtailment/limite P, reativo Q) via Modbus/SunSpec. | [F] (scoring: 3) | **V1** | matriz §02.1.1–02.1.2; scoring §3.1; spec §02.4 |
| **REQ-HW-08** | **Comando de bateria/BESS** (SOC/SOH/potência; setpoint carga-descarga, limites SOC, modo) via inversor híbrido/BMS (CAN/Modbus). | [F] (scoring: 2) | **V1** | matriz §02.2.1–02.2.2; scoring §3.1; spec §02.4 |
| **REQ-HW-09** | **Comando de cargas** (smart plug/relé liga-desliga, agendamento). | [F] (scoring: 2) | **V1** | matriz §02.5.1; spec §02.4 |
| **REQ-HW-10** | **Conectividade celular 4G/LTE + NB-IoT/Cat-M** (modem embarcado + SIM/eSIM M2M) — autonomia sem Wi-Fi do cliente. | [F] (scoring: teto 3, manter) | **V1** | matriz §01.1.2; spec §02.5 |
| **REQ-HW-11** | **Serial/barramento RS485 (Modbus-RTU multidrop) + CAN** (BMS). *Meio físico do driver layer e do attach do medidor.* | [F] | **V1** | matriz §01.1.3; spec §02.5 |
| **REQ-HW-12** | **I/O físico**: DI (contatos, RCR/ripple), AI (0-10V/4-20mA); DO/relé para atuação local **sem depender da nuvem**. | [F] (scoring: manter) | **V1** | matriz §01.3.1–01.3.2; spec §02.5 |
| **REQ-HW-13** | **OTA seguro com rollback**: flash dual-bank A/B, checksum, reversão em falha; imagem assinada + secure boot. | [F] (scoring: manter) | **V1** | matriz §01.4.1–01.4.2; spec §02.5 |
| **REQ-HW-14** | **Hardware/forma existente**: gateway DIN-rail / medidor c/ TCs; **IP65** outdoor abrigado (IP20 indoor); **<5–7W** sem ventilação ativa; **-30~+70°C**; display TFT/e-paper + LED/RGB + QR. | [F] (scoring: 08=4, lidera) | **V1** (herda) | matriz §08.1–08.3; spec §02.2; scoring §2 (teto 08=4) |
| **REQ-HW-15** | **Comissionamento sem-app (web/QR) + auto-detecção de ativos**; QR no device abre fluxo web. *Alimenta o comissionamento do portal do integrador.* | [E] | **V1** | matriz §06.4.1, §09.1.1 |
| **REQ-HW-16** | **Diagnóstico remoto**: logs/telemetria remotos + acesso remoto ao device p/ troubleshooting sem ir a campo; alarmes; fluxo de RMA. *Requisito explícito do portal do integrador.* | [E] | **V1** | matriz §06.4.2 |
| **REQ-HW-17** | **Fleet management**: console aplica config/firmware em lote a milhares de devices, rollout em ondas, monitoramento de saúde. *Requisito explícito "frota" do v1.* | [E] | **V1** | matriz §06.4.3 |
| **REQ-HW-18** | **Multi-tenant + RBAC + multi-site** e visões por papel (portal instalador/dashboard operador). *Comercializadora-âncora = tenant, não dona.* | [E]/[H] | **V1** (fundação; a decisão arquitetural é do bloco SW) | matriz §06.1.1–06.1.2; spec §05-dec.3, §03.4 |
| **REQ-HW-19** | **Resiliência offline de borda** (store-and-forward): buffer em flash/RAM guarda telemetria na queda do link e reenvia ao reconectar. *Smart-meter hoje = locus 1; subir é o degrau.* | [F] (scoring: locus=1) | **V1** (mínimo store-and-forward) | matriz §01.5.1; scoring §3.2 |

### FASE-2+ — o ODM próprio e a camada software/mercado (fora do v1, contexto de roadmap)

| REQ | Enunciado | Tag | Relevância | Fonte |
|---|---|---|---|---|
| **REQ-HW-20** | **ODM próprio / topologia desacoplada**: medidor universal barato em toda a base + **Energy Hub premium só onde há geração**; break-even vs. SKU integrado **~35% de adoção**. *Trocar smart-meter existente→ODM = configuração, não reescrita (viabilizado por REQ-HW-01).* | [E]/[H] | **FASE-2+** | spec §05-dec.1 (Topologia desacoplada); §06 roadmap M0 |
| **REQ-HW-21** | **Inteligência cloud-edge** (previsão geração/carga por ML+meteorologia → otimizador MILP/MPC, parte no edge). *Bloco inteiro ausente hoje (04=0).* | [E] | **FASE-2+** (M1) | matriz §04.1–04.2; scoring §3.2 (0→4); spec §03.1 |
| **REQ-HW-22** | **Compute no edge resiliente (locus 4)**: runtime leve (contêiner/WASM) executa lógica/modelos localmente; controle ótimo sobrevive à queda da nuvem. | [E] | **FASE-2+** (M1) | matriz §01.5.2, §04.4.1–04.4.2; spec §03.2; scoring §3.2 |
| **REQ-HW-23** | **Comando de VE (OCPP, smart charging, V2G/V2H) + bomba de calor (SG-Ready/Modbus/EEBUS, power-to-heat)**. *Lacunas pontuais do smart-meter: VE=0, bomba=0.* | [F] (scoring: 0/0) | **FASE-2+** (M1) | matriz §02.3, §02.4; scoring §3.1; spec §03.6 |
| **REQ-HW-24** | **Controle & EMS avançado**: anti-backfeed/zero feed-in, peak shaving/limite de demanda, balanço de fase, backup/ilhamento grid-forming, load shedding hierárquico. *EMS hoje=1.* | [E] | **FASE-2+** (M1) | matriz §03.1; scoring §2 (03=1); spec §M1 |
| **REQ-HW-25** | **Otimização por tarifa** (ToU, dinâmica day-ahead/spot, **tarifa BR**: branca/bandeiras/ponta-fora-ponta) e multi-objetivo (custo×autoconsumo×vida-bateria×CO₂). | [E] | **FASE-2+** (M1) | matriz §03.2; spec §03.5 |
| **REQ-HW-26** | **Protocolos adicionais**: Modbus-TCP (LAN), SunSpec, DLMS/COSEM, EEBUS, OCPP, MQTT/REST; grid/utility IEC 61850 / 60870-5-104 / DNP3. | [E] | **FASE-2+** (M1/M2) | matriz §01.2; spec §03.8 |
| **REQ-HW-27** | **API aberta / white-label / multi-tenant marketplace** (REST/GraphQL, webhooks, SDK, cloud-to-cloud HA/Google/Alexa). | [E] | **FASE-2+** (M1/M2) | matriz §06.2; spec §03.4 |
| **REQ-HW-28** | **VPP / agregação / serviços ancilares / demand response / trading** (BSP/BRP; FCR/aFRR/mFRR). *Bloco 05 inteiro ausente hoje (0).* | [H] | **FASE-2+** (M2) — **fora do v1 explícito** | matriz §05.1–05.4; scoring §3.3; spec §03.3 |
| **REQ-HW-29** | **UX autopilot + copilot linguagem natural (LLM) + visualização de valor (R$/CO₂)**. *Lição do Zerofy (UX=4).* | [E] | **FASE-2+** (M1) | matriz §09; spec §03.7 |
| **REQ-HW-30** | **Sensoriamento ambiental** (irradiância/piranômetro, temperatura painel-bateria-ambiente, qualidade de energia/anti-ilhamento). *Único gap de 00.* | [E] | **FASE-2+** | matriz §00.2; scoring §2 ("Falta só sensoriamento ambiental") |

### CONTEXTO — regulatório/mercado/2030 (não é requisito de build v1)

| REQ | Enunciado | Tag | Relevância | Fonte |
|---|---|---|---|---|
| **REQ-HW-31** | **Conformidade grid-code BR**: ANEEL/PRODIST + **homologação INMETRO da medição** + homologação de distribuidora + NBR. *Teto 07=2, smart-meter lidera "por ausência"; INMETRO formal ainda falta.* | [F] (scoring: 07=2) / [H] (custo-prazo) | **CONTEXTO** (fosso e armadilha; M2) | matriz §07.1.2, §07.2.1; scoring §2 (07=2 ⭐); spec §04.1 |
| **REQ-HW-32** | **Classe metrológica billing-grade**: Classe 0.5S/1 (IEC 62053), bidirecional, aprovação INMETRO por ensaio de exatidão. | [E] | **CONTEXTO** (ver conflito §4) | matriz §00.1.4 |
| **REQ-HW-33** | **Segurança/cyber**: TLS, encriptação em repouso, LGPD; hardening (secure boot, pen-testing, NIS2, BSI TR-03109). | [E] | **CONTEXTO** (transversal; parte já em REQ-HW-13) | matriz §07.3 |
| **REQ-HW-34** | **Integração CCEE / mercado livre (ACL)** + liquidação automática. *Teto BR vazio (0).* | [H] | **CONTEXTO** — **fora do v1 explícito** | matriz §05.3.3; spec §04.2, §04.4; scoring §3.3 |
| **REQ-HW-35** | **Agent-fabric AI-native por persona (LLM) + copilot operacional** + DOE, digital twin, manutenção preditiva, V2G em escala, P2P/transactive energy. *Fronteira 2030.* | [H] | **CONTEXTO** — **fora do v1 explícito** | matriz §2030 (todos); spec §04.3, §M3 |
| **REQ-HW-36** | **Módulo C&I acoplável**: submedição multi-ponto, demanda contratada BR, correção FP em escala, SCADA/BMS, ACL C&I. | [E] | **CONTEXTO** (módulo separado do núcleo) | matriz §C&I.1–C&I.4 |

## 3. Números / figuras-chave

| Figura | Valor | Tag | Fonte |
|---|---|---|---|
| Catálogo de sub-itens da matriz | ~118 (10 camadas núcleo 00–09 + C&I + 2030) | [F] | matriz (contagem) / prompt |
| Escala de scoring | 0–4 (0 ausente · 1 observa · 2 controla-regra · 3 otimiza · 4 autônomo/transaciona) | [F] | scoring §"Escala" |
| Players pontuados | 11 | [F] | scoring §título |
| **smart-meter — média/rank** | **1,7 · rank 10** (empata com Zerofy, por motivos espelhados) | [F] (scoring) | scoring §1 |
| smart-meter — perfil de camadas | 00=2·01=2·02=2·03=1·04=**0**·05=**0**·06=2·07=2·08=**4**·09=2 | [F] (scoring) | scoring §1 |
| Líderes de completude | Kiwigrid 3,3 (rank 1) · gridX 3,2 · Eniris 3,0 · Fenecon 2,9 | [F] (scoring) | scoring §1 |
| Camadas onde smart-meter detém o teto | Medição (00=3), Hardware (08=4); lidera Conformidade-BR (07=2) por ausência | [F] (scoring) | scoring §2 |
| Blocos inteiros ausentes (0) | Inteligência (04) e VPP/Flex (05) | [F] (scoring) | scoring §2, §5 |
| Players com edge resiliente (locus 4) | **5 de 11** (gridX, Kiwigrid, Fenecon, Eniris, Air 2) | [F] (scoring) | scoring §3.2 |
| Hardware existente | IP65 (outdoor abrigado) / IP20 (indoor); **<5–7W**; **-30~+70°C** | [F]/[E] | matriz §08.2; spec §02.2 |
| Break-even topologia desacoplada (medidor+Energy Hub) vs SKU integrado | **~35% de adoção** | [E] | spec §05-dec.1 |
| Cobertura VPP no Brasil (CCEE) entre os 10 estrangeiros | **0 (vazio)** | [F] (scoring) | scoring §3.3, §5 |
| Barramento RS485 Modbus | ~500 m / 32 nós | [F] | matriz §01.1.3 |
| Canal âncora BR | ~5k integradores | [E] | spec §02.6 |
| **(cross-ref docs/smart/06)** exatidão do Smart Meter commodity | **< 1% de desvio** (alvo classe 1, folga 0,5S) | [F] | docs/smart/06 §3 (contexto de reconciliação) |

## 4. Conflitos / ambiguidades e pontos a reconciliar com a suite `docs/smart`

**C1 — Tese de hardware DIVERGENTE (o ponto mais importante).**
Este bloco (02-hardware) trata o **smart-meter como o produto e o moat**: *"o EOS-DENO **é** o medidor"* (spec §02, §M0 "Nada a construir"), com **medição nativa Classe 1/2 billing-grade** (matriz §00.1.4, §07.2.1) como fonte de verdade e sensor-fosso. Já `docs/smart/06-especificacao-hardware.md` **reescreve a família** em dois elementos: **Smart Gateway** (o HEMS/cérebro, **controle por SINAL** — relé/DO de contato seco; "quem chaveia potência é externo: contator/disjuntor/ATS") + **Smart Meter** rebaixado a **commodity, exatidão <1%, grau-EMS** (proprietário *ou* OEM/ODM de mercado; ~R$100 CIF; Eastron SDM630/SDM120, Acrel ADL200/400) — e explicita que **o medidor de faturamento oficial continua sendo o da distribuidora** (`06 §3` "Medição EMS vs faturamento"). São teses opostas de onde mora o valor:
- **Reconciliar:** o "medidor billing-grade Classe 1 como moat" (02-hardware) vs. "medição é commodity <1%, o cérebro/sinal é o produto" (docs/smart/06). Afeta REQ-HW-04, REQ-HW-14, REQ-HW-20, REQ-HW-32. Recomendo alinhar a linguagem do v1: **o moat do v1 é a camada de abstração + telemetria + attach (Energy Hub), não a classe metrológica** — o que aproxima 02-hardware de docs/smart/06 e do STATE.

**C2 — "Energy Hub attach" não é vocabulário nativo do bloco 02-hardware.**
O prompt pede destacar o "Energy Hub attach" como V1. No bloco 02, o conceito mais próximo é **spec §05-dec.1** ("Energy Hub premium só onde há geração", topologia desacoplada) e **matriz §06.2.2** (white-label/marketplace). Mas a spec coloca o Energy Hub no lado do **ODM/topologia desacoplada (M0/Fase-2+)**, não como attach de v1 sobre o hardware existente. **Ambiguidade a reconciliar:** o "attach" do v1 é sobre o **smart-meter existente** (portal + assinatura ativando controle), enquanto o Energy Hub premium da spec pressupõe o novo SKU. Marquei o attach/topologia como **FASE-2+ (REQ-HW-20)** por fidelidade ao doc; se o STATE quer "Energy Hub attach" no v1, isso precisa de definição explícita — hoje o bloco 02 não a fornece.

**C3 — Vocabulário fora-de-escopo embutido na matriz/spec como se fosse produto.**
A matriz e a spec descrevem **VPP, CCEE, agent-fabric, otimização, mercado livre** como capacidades de destino (M2/M3), sem marcá-las como fora-do-v1. O README/STATE são explícitos que isso é **FORA do v1**. Não é contradição factual, mas **risco de arrastar escopo**: qualquer leitura direta da matriz/spec para "requisitos" traria os 05/2030 como se fossem alvo imediato. Marquei-os CONTEXTO/FASE-2+ e sinalizo para o brief de escopo do v1 travar isso.

**C4 — Multi-tenant: fundação vs. requisito de HW.**
REQ-HW-18 (multi-tenant/RBAC) aparece na matriz §06 e spec §05-dec.3 como decisão travada, mas é rigorosamente do **bloco software** (README: build-on ThingsBoard multi-tenant). No bloco HW é **fundação/pré-condição**, não implementação. Reconciliar ownership com a spec de software para não duplicar/conflitar.

**C5 — Marca "CORRENTE" pendente (metadado).**
`scoring-11-players.md` ainda usa **"ideal CORRENTE"** e **"Projeto CORRENTE"** (§1 linha 30; §6; rodapé linha 160), apesar do rename CORRENTE→EOS-DENO já decidido (MEMORIA LOG). É o único dos três arquivos do bloco com a marca antiga (confirma o aviso do README §"Marca pendente"). Matriz e spec já dizem "EOS-DENO". **Ação:** trocar CORRENTE→EOS-DENO no scoring ao consolidar.

**C6 — Fidelidade de dados desigual (limita a força epistêmica das notas).**
O próprio scoring declara (§"Fidelidade dos dados"): smart-meter = validado clique-a-clique (alta); EzManager/Air 2 = datasheet; os 8 demais = pesquisa web; `–` onde a fonte não sustenta. Logo, notas de terceiros são **[E] com base em fonte pública**, não [F] equivalente ao smart-meter. Ao citar tetos de mercado (ex. "5 de 11 fazem edge"), preservar essa ressalva.

## 5. Itens [INPUT]/[H] a validar (descoberta com integradores / assessoria)

1. **[H] Receita de flexibilidade/VPP no BR pode não existir** (não só estar vazia) — pré-mortem §04 do spec. Não modelar M2 como receita certa; validar com regulação em construção. (REQ-HW-28, REQ-HW-34)
2. **[H]/[INPUT] Break-even ~35% de adoção** da topologia desacoplada (medidor universal + Energy Hub premium) — número [E] da spec §05-dec.1 sem fonte; validar com economia real do canal de integradores. (REQ-HW-20)
3. **[H] Conformidade ANEEL/PRODIST/INMETRO como fosso vs. armadilha de prazo/caixa** — spec pré-mortem §03; INMETRO formal ainda **falta** (scoring §2: "Falta INMETRO formal"). Validar custo/tempo de homologação com assessoria; começar cedo, em paralelo ao M1. (REQ-HW-31, REQ-HW-32)
4. **[H] Timing banana-com-banana**: a aderência dos benchmarks (Intellihub AU) é em mercado **mandatado**; BR **sem mandato** de smart meter → timing não transfere (MEMORIA LOG). Validar apetite do integrador BR sem gatilho regulatório. (transversal)
5. **[H] Agnosticismo é passivo de engenharia perpétuo** — cada firmware de inversor que muda quebra a integração (pré-mortem §05). Validar as ~marcas que cobrem 80% da base BR para priorizar perfis. (REQ-HW-01, REQ-HW-02)
6. **[INPUT] ~5k integradores** no canal âncora (spec §02.6) — número [E]; validar tamanho/qualidade real do canal com descoberta de 2–3 integradores (ritual do STATE/README).
7. **Reconciliação C1/C2 (device/attach)** exige decisão de produto, não só validação: definir se o v1 assume **Smart Gateway+Meter-commodity (docs/smart/06)** ou **medidor billing-grade-como-moat (02-hardware)**, e o que exatamente é "Energy Hub attach" sobre o hardware **existente**. — decision-gate de escopo do v1.
