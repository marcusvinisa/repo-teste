> Extração fiel (subagente) do bloco. Fonte: docs/smart/referencias/produto/eos-deno-requisitos-produto-2026-06-30-CONF/. Preserva taxonomia [F]/[E]/[H]/[INPUT].

This confirms strong alignment. Key reconciliation points found:
- `docs/smart/01-visao-e-prd.md:55,62`: INT = primary/beachhead; **MVP primaries = CON + INT**, others "avançadas/posteriores" — a slight nuance vs the CONF STATE which puts v1 as INT-only (CON@A0 is a minimal bundle but the framing says "produto do integrador").
- `docs/smart/12-roadmap-e-faseamento.md`: Fase 0 MVP = monitor + autoconsumo + comissionar; Fase 2 = VPP/CCEE gated by regulation. Agent-fabric is NOT phased into the docs/smart roadmap at all (only mentioned as an OSS/build note in 08).
- `docs/smart/03-arquitetura-de-sistema.md:36`: DAL is in the architecture from the start (matches S2.3 discipline).

I have enough to produce the faithful extraction. Here is the result.

---

# EOS-DENO — Bloco 03-software · Extração de Requisitos (FIEL)

## 1 · Resumo do bloco

O bloco 03-software decompõe a "plataforma ideal de energia" em **~70 microsserviços** organizados em 18 domínios (S0–S17): domínios de energia (S0–S12) + plataforma/operação cross-cutting (S13–S17). Ele mapeia **7 personas da cadeia** (CON/INT/COM/AGG/GER/DSO/ORQ) e **18 cenários do consumidor** (arranjo comercial A/B/C × níveis de ativo N0–N5), onde cada persona/cenário = um *bundle* de serviços (modularização como forma de personalizar sem reescrever). Faz **scoring de 16 players** em dupla-lente (comparável competitivo **e** fundação de build-on), escala 0–4, em 12 macro-domínios (D1–D12), com tiers banana-com-banana (PLAT/VPP-OP/APP/OSS). A conclusão-âncora se repete deslocada do hardware: **dois tetos de mercado vazios — D7 CCEE/BR e D9 agent-fabric AI-native (LLM) — mais um ativo herdado (protótipo de DERMS, D5)**. A spec organiza tudo em **herdar → alcançar → ocupar** e cristaliza a decisão **build/fork/buy por domínio**: forkar as commodities (OpenEMS EMS, ThingsBoard IoT/multi-tenant, stack cloud-native, EMHASS/PyPSA na matemática) e construir os diferenciadores (CCEE + agent-fabric). **Ressalva-chave:** este bloco documenta a *plataforma inteira* (escopo 1+2+3); o **v1 confirmado é apenas a fatia mínima do integrador** — o corte V1/Fase-2+ abaixo é aplicado por mim a partir do STATE, não está pré-marcado nos 4 arquivos.

---

## 2 · Requisitos (`REQ-SW-NN`)

Legenda relevância: **[V1]** = fatia mínima do integrador (build agora) · **[FASE-2+]** = fora do v1 deliberado · **[CONTEXTO]** = enquadramento/decisão, não feature construível. Tags: [F] fato c/fonte · [E] estimativa · [H] hipótese · [INPUT] placeholder. Fonte = `matriz` / `personas` / `scoring` / `spec` / `STATE`.

### Núcleo V1 — a fatia mínima do integrador (ingestão → time-series → modelo de ativo → portal, sobre smart-meter existente)

| ID | Enunciado | Tag | Relevância | Fonte |
|---|---|---|---|---|
| REQ-SW-01 | **Device Gateway/Connector (S0.1)** — ingerir telemetria de medidores/inversores/baterias via adaptadores Modbus/MQTT/REST + fila de mensagens. | [F] | **[V1]** | matriz S0 |
| REQ-SW-02 | **Protocol Adapter Registry (S0.2)** — biblioteca de drivers por fabricante, plugins versionados mapeados ao modelo canônico. | [F] | **[V1]** | matriz S0 |
| REQ-SW-03 | **Edge Sync / Store-and-forward (S0.3)** — sincronizar estado edge↔cloud, buffer offline, idempotência. | [F] | **[V1]** | matriz S0 |
| REQ-SW-04 | **Command Dispatch Bus (S0.4)** — entregar setpoints/comandos ao edge com ack + retry idempotente. | [F] | **[V1]**¹ | matriz S0 |
| REQ-SW-05 | **Time-Series Store (S1.1)** — armazenar medição em alta resolução em TSDB (TimescaleDB/InfluxDB), retenção configurável. | [F] | **[V1]** | matriz S1 |
| REQ-SW-06 | **Telemetry API (S1.4)** — consulta de telemetria por serviços/apps (REST/GraphQL + cache). | [F] | **[V1]** | matriz S1 |
| REQ-SW-07 | **Event Bus / Streaming (S1.2)** — pub/sub de eventos (Kafka/NATS) para serviços reativos. | [F] | **[V1]**² | matriz S1 |
| REQ-SW-08 | **Asset Registry (S2.1)** — cadastro canônico de UCs, medidores, inversores, baterias, VE, cargas. | [F] | **[V1]** | matriz S2 |
| REQ-SW-09 | **Topology Model (S2.2)** — relação elétrica (fase, circuito, ponto de conexão, UC↔usina). | [F] | **[V1]** | matriz S2 |
| REQ-SW-10 | **Device Abstraction (S2.3)** — modelo canônico *capability-based* que abstrai fabricantes. **Disciplina inegociável: desde a 1ª linha** — trocar p/ medidor ODM depois = configuração, não reescrita. | [F] STATE / [E] disciplina | **[V1] — obrigatório** | STATE + matriz S2 + spec §05.3 |
| REQ-SW-11 | **Digital Twin State (S2.4)** — estado em tempo real de cada ativo/site (state store + projeções de eventos). | [F] | **[V1]** | matriz S2 |
| REQ-SW-12 | **Installer Portal (S12.2)** — portal web do integrador: **comissionamento, diagnóstico remoto, frota**. Superfície central do v1. | [F] | **[V1]** | matriz S12 + personas §3.4 |
| REQ-SW-13 | **Fleet Manager (S6.1)** — gerir frota de devices/sites em escala (agrupamento, rollout em ondas, health) para o integrador. | [F] | **[V1] (subset frota)**³ | matriz S6 + personas |
| REQ-SW-14 | **Fleet Health (S14.4)** — saúde dos devices (RMA, falhas) via health checks + telemetria. | [F] | **[V1]** | matriz S14 |
| REQ-SW-15 | **Auth & Identity (S9.1)** — autenticação OAuth/OIDC (Keycloak/Ory). | [F] | **[V1]** | matriz S9 |
| REQ-SW-16 | **Tenant Isolation (S9.2)** — **modelo de dados tenant-aware desde o dia 1** (multi-tenant base); ferramental completo de white-label adiado até o 2º tenant. | [F] / [E] faseamento | **[V1] (base) / white-label FASE-2** | matriz S9 + spec §05.3 + pré-mortem 04 |
| REQ-SW-17 | **RBAC & Permissions (S9.3)** — papéis/permissões por persona (foco INT no v1). | [F] | **[V1]** | matriz S9 |
| REQ-SW-18 | Modularização em **microsserviços → bundles por persona/cenário**: ativar/desativar serviços em vez de reescrever o produto (decisão de arquitetura nº1). | [F] | **[V1]** (padrão) / **[CONTEXTO]** | matriz + personas §4 + spec §05 |
| REQ-SW-19 | Fork/build-on **OpenEMS** para a camada edge/EMS-connector (S0/S5); ingestão via **ThingsBoard** (gateway IoT). | [F] decisão | **[V1] (S0 base)** | STATE + matriz S0/S5 + scoring §5 |

¹ S0.4 (command dispatch) é infraestrutura de comando; entra no v1 como base para comissionamento/config remota, mesmo que o controle-otimizado (EMS/despacho) seja fase 2.
² S1.2/S1.3 (event bus, data lake): o event bus é base de plataforma reativa; **Data Lake (S1.3)** é analytics/ML → Fase-2.
³ S6.1 (Fleet Manager) tem lente dupla: a **gestão de frota do integrador** é V1; a coordenação de despacho de grupo (S6.2–S6.4, sinais DSO/curtailment) é Fase-2+.

### Observabilidade/infra mínima de sustentação (V1 de suporte)

| ID | Enunciado | Tag | Relevância | Fonte |
|---|---|---|---|---|
| REQ-SW-20 | **Monitoring & Logging + Alerting (S14.1/S14.2)** — observabilidade da plataforma (Prometheus/Grafana/OTel). | [F] | **[V1] (mínimo)** | matriz S14 |
| REQ-SW-21 | **Encryption & Secrets + Audit Log (S15.1/S15.2)** — TLS/KMS + trilha append-only de comandos/acessos. | [F] | **[V1] (mínimo)** | matriz S15 |
| REQ-SW-22 | **Cloud-native Runtime + CI/CD (S16.1/S16.2)** — Kubernetes + pipeline/IaC; **Edge Runtime Distribution / OTA de software (S16.3)** para device. | [F] | **[V1] (base) / OTA-frota parcial** | matriz S16 |
| REQ-SW-23 | **API Gateway (S10.1)** — REST/GraphQL + rate limit (Kong/APISIX); **Webhooks (S10.2)** para integradores. | [F] | **[V1] (base API)** / SDK+Marketplace **FASE-2** | matriz S10 |

### Fase-2+ (fora do v1 deliberado — VPP, CCEE, agent-fabric, otimização, mercado)

| ID | Enunciado | Tag | Relevância | Fonte |
|---|---|---|---|---|
| REQ-SW-24 | **Forecasting S3** (Solar/Load/Price/Weather S3.1–S3.4) — físico+ML; forecasting-as-a-service p/ S4/S7/S12. Build-on pvlib/EMHASS. | [F] | **[FASE-2+]** (M1 "alcançar") | matriz S3 + spec §03.1 |
| REQ-SW-25 | **Otimização & Scheduling S4** (Optimization Engine MILP/MPC, Tariff Model, Multi-objective, RL, Plan/Schedule S4.1–S4.5). Build-on OR-Tools/PyPSA/EMHASS. | [F] | **[FASE-2+]** (explícito fora do v1) | matriz S4 + spec §03.1 + STATE |
| REQ-SW-26 | **EMS/Controle S5** (EMS Core/control loop, Safety guardrails, Scene/Mode Manager, Edge Policy S5.1–S5.4). Fork forte OpenEMS. | [F] | **[FASE-2+]** (M1) — *nota:* S5.2 guardrails pode subir se houver controle no v1 [H] | matriz S5 + spec §03.2 |
| REQ-SW-27 | **DERMS/Fleet Orchestration S6.2–S6.4** — group/cohort control, grid signal handler (RCR/§14a/DOE), curtailment orchestrator. | [F] | **[FASE-2+]** | matriz S6 |
| REQ-SW-28 | **VPP/Mercado/Trading S7** (Aggregation, Bidding, Market Connectors CCEE, Ancillary FCR/aFRR/mFRR, DR Program S7.1–S7.5). Build (OpenADR p/ sinalização DR). | [F] | **[FASE-2+]** (M2, monetização gradual) | matriz S7 + spec §03.3 |
| REQ-SW-29 | **CCEE/Liquidação/Billing BR S8** (CCEE Integration, Credit Allocation/Rateio Lei 14.300, Settlement ACL, Energy Billing S8.1–S8.4). **Build puro — moat regulatório, nenhuma fundação OSS.** | [F] | **[FASE-2+]** (M2 "ocupar BR") | matriz S8 + spec §04.1 + scoring D7 |
| REQ-SW-30 | **Agent-Fabric/AI-native S11** (Agent Runtime LLM, Tool Registry, Per-Persona Agents, Copilot/NL, Guardrails S11.1–S11.5). **Build inspirado em Volttron (paradigma) + frameworks LLM.** | [F] | **[FASE-2+]** (M3 "ocupar fronteira") | matriz S11 + spec §04.2 + scoring D9 |
| REQ-SW-31 | **Consumer App (S12.1)** e **Operator Dashboard (S12.3)** e **Engagement/Notifications (S12.4)**. | [F] | **[FASE-2+]** (Consumer App = persona CON, posterior)⁴ | matriz S12 |
| REQ-SW-32 | **White-label Theming (S9.4)** — marca/domínio por tenant. | [F] | **[FASE-2+]** (adiar até 2º tenant) | matriz S9 + pré-mortem 04 |
| REQ-SW-33 | **SDK & Docs (S10.3)** + **Module Marketplace (S10.4)** — ecossistema de devs/parceiros. | [F] | **[FASE-2+]** | matriz S10 |
| REQ-SW-34 | **MLOps S13** (Model Registry, Training Pipeline, Feature Store, Drift Monitoring S13.1–S13.4). Build-on MLflow/Feast. | [F] | **[FASE-2+]** (depende de forecasting/ML) | matriz S13 |
| REQ-SW-35 | **Comercial/Monetização S17** (Subscription Billing, Usage Metering, Revenue-share, CRM S17.1–S17.4). | [F] | **[FASE-2+]** (buy/build) | matriz S17 |
| REQ-SW-36 | **Data Lake (S1.3)** — histórico bruto p/ analytics/ML. | [F] | **[FASE-2+]** | matriz S1 |
| REQ-SW-37 | **Deployment Modes / self-hosted-híbrido (S16.4)** + **SLA & Uptime por tenant (S14.3)** + **Compliance SOC2/ISO (S15.3/S15.4)**. | [F] | **[FASE-2+]** (endurecimento pós-1º tenant) | matriz S14/S15/S16 |

⁴ *Ambiguidade:* o STATE define v1 como "produto do integrador" (INT), mas o portal de comissionamento habilita indiretamente cenários A0/B0/C0 de monitoramento. `docs/smart/01` lista **CON+INT como primárias no MVP** — ver §6.

### Requisitos de contexto/decisão

| ID | Enunciado | Tag | Relevância | Fonte |
|---|---|---|---|---|
| REQ-SW-38 | Regra "**forkar commodities, construir diferenciadores**": fork OSS em D1/D4/D8/D11; build em D7/D9; build-on matemática em D3. | [F] decisão | **[CONTEXTO]** | spec §01/§05 + scoring §5 |
| REQ-SW-39 | **Multi-tenant + cloud-edge + agent-fabric desde a fundação** (decisão de arquitetura nº3) — tenant-aware dia 1; controle no edge; agentes por persona como camada incremental sobre serviços determinísticos. | [F]/[H] | **[CONTEXTO]** (tenant-aware=V1; agent-fabric=Fase-2) | spec §05 + pré-mortem 02 |
| REQ-SW-40 | Roadmap de software em 4 ondas: **M0 herdar** (ingestão+DERMS+OSS) → **M1 alcançar** (D3/D4/D8/D10) → **M2 VPP+CCEE** (D6/D7) → **M3 agent-fabric** (D9). | [F] | **[CONTEXTO]** (M0≈v1) | spec §06 |

---

## 3 · Personas & cenários

### As 7 personas da cadeia (personas §1)

| Cód | Persona | Casos de uso exclusivos | Relevância v1 |
|---|---|---|---|
| **CON** | Consumidor/Prosumidor (dono da UC, varia pelos 18 cenários) | conta/tarifa, autoconsumo, backup, EV, economia R$/CO₂ | **Parcial/posterior** — Consumer App é Fase-2; monitoramento básico via portal do integrador toca A0/B0/C0 |
| **INT** | **Integrador/EPC — BEACHHEAD** | comissionamento, onboarding de ativos, diagnóstico remoto, RMA, portal multi-cliente | **✅ V1 — persona-alvo única** |
| **COM** | Comercializadora/Varejista (âncora adquire uma) | book, billing de energia, planos/contratos, app white-label, churn, liquidação CCEE da carteira | **Fase-2+** |
| **AGG** | Agregador/VPP | agregação de portfólio, bidding, qualificação ancilar, despacho, baseline, revenue-share | **Fase-2+** (VPP fora do v1) |
| **GER** | Gerador (usinas GD, geração compartilhada) | performance de geração, rateio de créditos GD, PPA, monetização | **Fase-2+** |
| **DSO** | Distribuidor | sinais de rede (RCR/§14a/DOE), curtailment, telecontrole, hosting capacity | **Fase-2+** |
| **ORQ** | Orquestrador/Operador da plataforma | operação multi-tenant, SLA, saúde de frota, MLOps, config, marketplace | **Parcial** — operação da infra multi-tenant base é V1; MLOps/marketplace são Fase-2 |

> Nota de arquitetura (personas §1): plataforma **multi-tenant desde a fundação**; COM/INT/AGG são *tenants* (não donos); ORQ opera a infra compartilhada. Lista é referência, **não teto** (seguradora/banco/poder concedente podem entrar).

### Os 18 cenários do consumidor (personas §2) — eixo A/B/C × N0–N5

- **Arranjos:** A = Cativo · B = GD compartilhada (Lei 14.300) · C = Mercado livre (ACL).
- **Níveis (acumulativos):** N0 só consumo → N1 +PV → N2 +bateria → N3 +EV → N4 +load shifting → N5 +grid services.

**Marcação V1 (integrador) vs depois** — os 18 cenários são **explicitamente FORA do v1** no STATE. O que o v1 toca é apenas a base de monitoramento/comissionamento:

| Cenários | Modos principais | v1? |
|---|---|---|
| **A0 / B0 / C0** (só consumo) | monitoramento, conta/tarifa; B0 + rateio/billing de créditos; C0 + medição CCEE | **Parcial** — monitoramento/telemetria via portal (o bundle mínimo "CON@A0 = ingestão+telemetria+app+billing" existe), mas **rateio (B) e medição CCEE (C) são Fase-2 (S8)** |
| **A1–A5, B1–B5, C1–C5** | autoconsumo→otimização→VPP; créditos; arbitragem/mercado | **Fase-2+** — exigem forecasting/otimização/EMS/VPP/CCEE, todos fora do v1 |

> **Ressalva regulatória (registrada em personas §2 e matriz §231):** *grid services* remunerado em BT (linha N5: A5/B5/C5) e mercado livre BT (coluna C) **dependem de evolução regulatória** → entram como **capacidade técnica pronta, monetização gradual** (coerente com bear case: receita de flexibilidade BR é hipótese, não fato). **[H]/[INPUT]**

---

## 4 · Decisão build/fork/buy por domínio (scoring §5 + spec §01)

| Domínio (macro) | Veredito | Fundação OSS |
|---|---|---|
| **D1 Ingestão** | **Fork / build-on** | **ThingsBoard / OpenEMS** (device mgmt, telemetria, drivers) |
| **D2 Dados & Twin** | Build-on infra | TimescaleDB / Kafka (TSDB+streaming); **modelo de ativo = build** |
| **D3 Inteligência (forecast+otim.)** | **Build-on a matemática** | EMHASS + PVLib / PyPSA / OR-Tools / HiGHS (produtizar p/ frota = build) |
| **D4 EMS/Controle** | **Fork forte** | **OpenEMS** (edge+backend, Apache 2.0, agnóstico, modular) |
| **D5 DERMS/Frota** | Build-on parcial (+ **ativo herdado**) | OpenEMS Backend / Volttron (agregação parcial; DERMS de mercado = build) |
| **D6 VPP/Mercado** | **Build** (com referência) | OpenADR / OpenLEADR (só sinalização DR; bidding/mercado = build) |
| **D7 CCEE/BR** | **Build puro — moat** | **nenhuma** (específico do Brasil) |
| **D8 Multi-tenant/API** | **Build-on infra** | ThingsBoard + Keycloak + Kong |
| **D9 Agent-fabric AI-native** | **Build (inspirado)** | Volttron (paradigma de agentes clássicos) + frameworks LLM abertos |
| **D10 Apps/UX** | Build (ref) | Home Assistant (referência de UX/integrações); app próprio = build |
| **D11 Infra/Sec/MLOps** | **Build-on (padrão)** | k8s / Prometheus / Grafana / Vault / OpenBao / MLflow |
| **D12 Comercial** | Buy/build | — (billing/CRM = build/buy) |

**Síntese (spec §01):** Fork/build-on OSS → **D1, D4, D8, D11** · build-on matemática → **D3** · build com referência → **D6, D10** · **build puro/moat → D7, D9**.

---

## 5 · Números/figuras-chave (scoring)

- **Os 2 tetos de mercado VAZIOS** (achado-âncora, repetido em STATE/README/scoring §4/§7 e spec):
  - **D7 CCEE/BR — teto de mercado = 0; "NINGUÉM" detém; EOS-DENO = 2 (único BR).** "Espaço vazio a ocupar — o fosso." **[F]** (scoring §4)
  - **D9 Agent-fabric AI-native (LLM) — teto real ≈ 0.** O teto "3" listado é do **Volttron em agentes *clássicos* (não-LLM)**; em LLM-agents "ninguém tem ainda — fronteira aberta". **[F]/[E]** (scoring §4, nota `*` linha 100)
- **D5 DERMS = único domínio de software com ativo herdado** (protótipo), EOS-DENO ≈ 2, teto 4. **[F]/[E]** (scoring §4/§7-2)
- **Scoring de completude (Méd 12 sobre D1–D12, escala 0–4):** Kraken **3.2** (líder) · Kiwigrid 3.0 · Eniris 2.8 · gridX 2.75 · AutoGrid 2.67 · Next Kraftwerke 2.58 · Intellihub 2.5 · Sympower 2.17 · Tibber 1.92 · ThingsBoard 1.92 · Zerofy 1.75 · OpenEMS 1.67 · Volttron 1.67 · Smappee 1.58 · HA+EMHASS 1.42 · OpenADR = *bloco* (não pontua). **[F]** (scoring §3). *Leitura:* a média mede largura/completude — penaliza OSS de nicho, que são **altos como fundação** no seu domínio, não ranking de "melhor".
- **Pontos-de-partida por domínio (EOS-DENO hoje, estim.):** D1 ingestão **3–4** (forte, medidor+edge); D5 DERMS **~2** (herdado); D7 **2** (único BR); demais **~0–1** (build). **[E]** (scoring §4)
- **Ameaça direta = Octopus Kraken** — OS de utility end-to-end, ~70M contas, 27 países, #1 Guidehouse Grid-Edge DERMS; **zero BR e não é AI-native (LLM)** — o relógio competitivo. **[F]** (scoring §1/§7-5)
- **Intellihub = paralelo mais próximo** (medidor+plataforma DeX+VPP em AU/NZ), sem camada AI-native e sem CCEE — "o que vira o EOS-DENO se não fizer os dois domínios vazios." **[F]/[H]** (scoring §7-4)
- **Contexto (matriz §231 / STATE):** S7 (VPP/ancilares) e parte de S8 (mercado livre BT) = **capacidade técnica pronta, monetização gradual**. **[H]**

---

## 6 · Conflitos/ambiguidades e reconciliação com `docs/smart`

O conjunto `docs/smart` (05, 08, 09, 10, 11 + 01-PRD, 03-arquitetura, 12-roadmap) é uma **elaboração de engenharia mais detalhada e coerente do mesmo produto** — mesmas 7 personas, mesmos 18 cenários, mesmas fundações OSS, mesmo veredito build/fork/buy. Pontos a conciliar:

1. **Escopo do MVP: INT-only (CONF) vs CON+INT (docs/smart).**
   - CONF/STATE: v1 = "produto do **integrador (P1)**"; CON e demais explicitamente posteriores.
   - `docs/smart/01-visao-e-prd.md:55,62`: INT = primária/beachhead, mas **"Primárias no MVP: CON + INT"**; COM/AGG/GER/DSO/ORQ "avançadas/posteriores".
   - **Reconciliação:** convergem no beachhead INT. A diferença é o **Consumer App/Mobile** (`docs/smart/09` Smart App): tratá-lo como **Fase-2** no build v1 (o portal do integrador — `Smart Web Pro` — é a superfície v1). O monitoramento que o consumidor "vê" no v1 chega via portal do integrador, não via app dedicado. **[INPUT] a confirmar.**

2. **Agent-fabric não aparece no roadmap de `docs/smart`.**
   - CONF: D9/S11 é diferenciador central (M3), embora **fora do v1**.
   - `docs/smart/12-roadmap` tem só Fase 0/1/2 (MVP → otimização → mercado) — **agent-fabric ausente do faseamento**; é citado apenas como nota de build em `08:63`. Sem conflito de v1 (ambos o excluem do MVP), mas há **lacuna de roadmap** em docs/smart que a spec-software preenche. **[H]**

3. **Nomenclatura de serviços diverge (mesma substância).**
   - `docs/smart/08` usa nomes de produto ("Serviço de Dispositivos/DAL", "Otimização+Forecast", "Billing/Rateio GD", "VPP/Agregação"); a matriz-software usa a taxonomia S0–S17. **Mapeamento direto:** DAL↔S2.3, Ingestão↔S0/S1, Otimização↔S3/S4, EMS↔S5, VPP↔S6/S7, Billing/Rateio↔S8, IAM↔S9, API↔S10, Observabilidade↔S14. Sem conflito.

4. **Device Abstraction / DAL — totalmente alinhado.** `docs/smart/05` inteiro é a especificação da DAL (capabilities telemetry/setpoint/mode/schedule/meta; local>cloud para controle; conectores cloud-to-cloud priorizados GoodWe/Deye/Sungrow/Growatt/Huawei/Solis) e `docs/smart/03:36` já coloca a DAL na arquitetura. **Reforça REQ-SW-10 (S2.3 desde a 1ª linha)** com detalhe de implementação (protocolos, matriz de compatibilidade, processo de certificação). Nenhum conflito.

5. **Stack de telemetria — nota de risco em docs/smart não presente no CONF.** `docs/smart/08:65` `[VERIFICAR]`: **Amazon Timestream for LiveAnalytics fechou p/ novos clientes (20/06/2025)** → usar Timestream-for-InfluxDB ou TimescaleDB. Isso **refina REQ-SW-05** (a matriz-software cita TimescaleDB/InfluxDB genericamente). Adotar TimescaleDB é a escolha segura. **[F] docs/smart / [INPUT] confirmar região sa-east-1.**

6. **Multi-tenant desde a fundação — consistente e explícito nos dois.** `docs/smart/08:120` mapeia as 7 personas → roles + matriz de atribuições (herda hierarquia SEMS até 5 níveis). Confirma REQ-SW-16/17. O faseamento "tenant-aware dia 1, white-label depois" (spec pré-mortem 04) é compatível.

**Sem conflitos duros.** As divergências são de **escopo-de-persona no MVP (item 1)** e **cobertura de roadmap (item 2)** — ambas resolvíveis mantendo o corte do STATE (INT-only, portal-first, agent-fabric/VPP/CCEE fora do v1).

---

## 7 · Itens [INPUT]/[H] a validar

1. **[INPUT] Consumer App no v1?** CONF diz INT-only; `docs/smart/01` diz "CON+INT primárias no MVP". Confirmar se o Mobile (S12.1) fica 100% fora do v1 ou se há um mínimo de visualização do consumidor. (Impacta REQ-SW-31.)
2. **[INPUT] Fronteira exata do S6 no v1.** Fleet Manager (S6.1) para o integrador é V1; confirmar que S6.2–S6.4 (group control, grid signals, curtailment) ficam integralmente Fase-2. (REQ-SW-13/27.)
3. **[H] S5.2 Safety & Guardrails no v1?** Se o portal do integrador emitir qualquer comando/config remota (comissionamento), os guardrails/interlocks podem precisar entrar antes do EMS completo. Validar se S5.2 sobe para v1 como pré-requisito de segurança de comando. (REQ-SW-04/26.)
4. **[H] Onde vive o protótipo de DERMS herdado (D5).** Spec §02.2 diz "já existe"; nenhum código/artefato localizado no repo (`repos/` tem `energy-connectors`, citado em `docs/smart/05:88`, mas não um DERMS). Confirmar o ativo real e seu estado de "consolidar para escala". **[INPUT]**
5. **[INPUT/H] Premissas regulatórias BR** (recorrentes): VPP/ancilares/mercado livre BT dependem de regulação (Lei 15.269/2025: BT comercial até nov/2027, residencial até nov/2028 — `docs/smart/11:78`). Receita de flexibilidade BR = hipótese, não fato. Só afeta Fase-2, mas **datas de M2 dependem disso**.
6. **[INPUT] Stack de time-series** (item 6 acima): confirmar TimescaleDB vs Timestream-for-InfluxDB e disponibilidade em sa-east-1.
7. **[H] Fork OpenEMS como fardo de manutenção** (pré-mortem 01) e **agent-fabric superdimensionado** (pré-mortem 02): mitigações registradas (fork disciplinado/contribuir upstream; agent-fabric como camada incremental nunca crítica) — validar como guardrails de arquitetura no build v1.
8. **[CONTEXTO] Marca "EOS-DENO" sem checagem de colisão** (decision-gate aberto no STATE) — não é software, mas está aberto.

---

**Arquivos-fonte (absolutos):**
- `/home/marcus/lab/sandbox/repo-teste/docs/smart/referencias/produto/eos-deno-requisitos-produto-2026-06-30-CONF/03-software/eos-deno-matriz-software.md`
- `…/03-software/eos-deno-personas-casos-de-uso.md`
- `…/03-software/eos-deno-scoring-software.md`
- `…/03-software/eos-deno-spec-software.md`
- `…/00-fundacao/04-MEMORIA-E-APRENDIZADO.md` (STATE) · `…/README-CLAUDE-CODE.md`
- Reconciliação: `/home/marcus/lab/sandbox/repo-teste/docs/smart/{01-visao-e-prd,03-arquitetura-de-sistema,05-integracao-e-conectividade,08-plataforma-cloud-e-apis,09-apps-web-mobile-e-ux,10-modos-de-operacao-e-features,11-matriz-de-cenarios,12-roadmap-e-faseamento}.md`
