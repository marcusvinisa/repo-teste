# EOS-DENO · Scoring de Software — 16 Players contra o Catálogo de Microsserviços

> **Estudo de referência curado pelo usuário.** Reproduzido em `referencias/`. Ver [00-absorcao-e-ajustes.md](00-absorcao-e-ajustes.md).

> **Dupla lente:** cada player é avaliado como **comparável competitivo** *e* como **fundação de build-on** (especialmente os open-source). Pontuação **0–4** de maturidade, no nível de **macro-domínio**, com `—` onde a fonte não confirma. Disciplina de fato-confirmado; pesquisa web nas fontes oficiais.

**Escala:** 0 ausente · 1 observa/básico · 2 controla/funcional · 3 otimiza/maduro · 4 líder/completo.

**Tiers (banana-com-banana):** `PLAT` plataforma utility-grade · `VPP-OP` operador de VPP (+ software) · `APP` app de consumidor · `OSS` framework open-source.

**Macro-domínios:** **D1** Ingestão · **D2** Dados & Twin · **D3** Inteligência (forecast+otim.) · **D4** EMS/Controle · **D5** DERMS/Frota · **D6** VPP/Mercado · **D7** CCEE/BR · **D8** Multi-tenant/API · **D9** Agent-fabric AI-native · **D10** Apps/UX · **D11** Infra/Sec/MLOps · **D12** Comercial.

---

## 1 · Os 16 players (tier + uma linha)

| Player | Tier | Uma linha |
|---|---|---|
| **Octopus Kraken** | PLAT | OS de utility end-to-end (CRM+billing+trading+DERMS via Kraken Flex); #1 Guidehouse Grid-Edge DERMS; ~70M contas, 27 países; white-label per-account |
| **AutoGrid** (Uplight) | PLAT | DERMS/VPP/DR AI-powered, líder histórico (Guidehouse #1); IEEE 2030.5; EcoStruxure; 8.300MW geridos. Sem retail nativo |
| **gridX** (XENON) | PLAT | HEMS white-label agnóstico; forte plataforma/API multi-tenant; E.ON. UE |
| **Kiwigrid** (KiwiOS) | PLAT | Plataforma IoT-energia white-label; Matua AI; VPP via Energy Hub Alliance. DACH |
| **Eniris** (SmartgridX) | PLAT | EMS+VPP agnóstico, Open API, mercados de balanceamento. BE |
| **Intellihub** (DeX) | PLAT | **Medidor + plataforma DeX** de interoperabilidade DER/VPP (registro+controle CER, "many-to-many"); paralelo direto ao EOS-DENO. AU/NZ |
| **Next Kraftwerke** (NEMOCS) | VPP-OP | Um dos maiores VPPs da Europa; trading spot/intraday/balanceamento + FCR/aFRR/mFRR; licencia NEMOCS. Shell |
| **Sympower** | VPP-OP | Agregador de flexibilidade (DR industrial/comercial) p/ serviços ancilares na Europa |
| **Tibber** | APP | Varejista digital + app + **API GraphQL aberta**; preço dinâmico, smart charging. UX forte. Nórdicos |
| **Smappee** | APP | Monitoramento (NILM) + EV + plataforma; behind-the-meter. BE |
| **Zerofy** | APP | App HEMS agnóstico (800+ devices), scheduling por preço; **UX líder**, sem VPP. EE/CH |
| **OpenEMS** (Fenecon) | OSS | **EMS open-source** (Apache 2.0) edge+backend, agnóstico, modular; a base de EMS mais forte |
| **Volttron** (Eclipse/DOE) | OSS | **Plataforma de agentes** p/ controle distribuído da rede + transactive energy; legado Python, foco building |
| **Home Assistant + EMHASS** | OSS | Automação residencial (milhares de integrações) + **EMHASS** (otim. LP/MPC + forecast PVLib/ML). Escala doméstica |
| **ThingsBoard** | OSS | **Plataforma IoT** open-source multi-tenant (ingestão, regras, dashboards). Não específica de energia |
| **OpenADR / OpenLEADR** | OSS | **Padrão + impl.** open-source de sinalização de Demand Response (LF Energy). É bloco, não plataforma |

---

## 2 · Matriz de scoring — Domínios de energia (D1–D7)

| Player | D1 Ingestão | D2 Dados/Twin | D3 Inteligência | D4 EMS | D5 DERMS | D6 VPP/Mercado | D7 CCEE/BR |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Kraken | 3 | 3 | **4** | 2 | **4** | **4** | 0 |
| AutoGrid | 3 | 3 | **4** | 2 | **4** | **4** | 0 |
| gridX | 3 | 3 | **4** | 3 | 3 | 3 | 0 |
| Kiwigrid | 3 | 3 | 3 | 3 | **4** | **4** | 0 |
| Eniris | 3 | 3 | 3 | **4** | 3 | **4** | 0 |
| Intellihub | **4** | 3 | 2 | 2 | **4** | 3 | 0 |
| Next Kraftwerke | 3 | 3 | 3 | 2 | **4** | **4** | 0 |
| Sympower | 2 | 2 | 3 | 2 | 3 | **4** | 0 |
| Tibber | 2 | 2 | 3 | 2 | 0 | 1 | 0 |
| Smappee | 3 | 2 | 2 | 2 | 1 | 0 | 0 |
| Zerofy | 2 | 2 | 3 | 2 | 0 | 0 | 0 |
| **OpenEMS** | 3 | 2 | 2 | **4** | 2 | 1 | 0 |
| **Volttron** | 3 | 2 | 2 | 3 | 2 | 2 | 0 |
| **HA + EMHASS** | 3 | 2 | 3 | 3 | 0 | 0 | 0 |
| **ThingsBoard** | **4** | 3 | 1 | 2 | 1 | 0 | 0 |
| **OpenADR/LEADR** | 2 | — | — | — | — | 3 | 0 |

## 3 · Matriz de scoring — Plataforma & negócio (D8–D12)

| Player | D8 Multi-tenant/API | D9 Agent-fabric | D10 Apps/UX | D11 Infra/Sec | D12 Comercial | **Méd 12** |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| Kraken | **4** | 2 | **4** | **4** | **4** | **3.2** |
| Kiwigrid | **4** | 2 | 3 | **4** | 3 | **3.0** |
| Eniris | **4** | 1 | 3 | 3 | 3 | **2.8** |
| gridX | **4** | 1 | 3 | 3 | 3 | **2.75** |
| AutoGrid | 3 | 2 | 2 | 3 | 2 | **2.67** |
| Next Kraftwerke | 3 | 1 | 2 | 3 | 3 | **2.58** |
| Intellihub | 3 | 1 | 2 | 3 | 3 | **2.5** |
| Sympower | 2 | 1 | 2 | 2 | 3 | **2.17** |
| Tibber | 3 | 1 | **4** | 2 | 3 | **1.92** |
| ThingsBoard | **4** | 1 | 3 | 3 | 1 | **1.92** |
| Zerofy | 3 | 1 | **4** | 1 | 3 | **1.75** |
| OpenEMS | 2 | 0 | 2 | 2 | 0 | **1.67** |
| Volttron | 1 | **3** | 1 | 1 | 0 | **1.67** |
| Smappee | 2 | 0 | 3 | 2 | 2 | **1.58** |
| HA + EMHASS | 1 | 1 | 3 | 1 | 0 | **1.42** |
| OpenADR/LEADR | — | — | — | — | — | *bloco* |

**Leitura:** a média mede **completude/largura** — penaliza OSS de nicho e apps, fortes só onde atuam. **Não** é ranking de "melhor": é mapa de cobertura. Kraken lidera completude (é um OS de utility). Os OSS aparecem baixo aqui, mas são **altos como fundação** no seu domínio (ver §5).

---

## 4 · Teto de mercado por domínio — e o ponto de partida do EOS-DENO

| Domínio | Teto | Quem detém | EOS-DENO hoje (estim.) | Leitura |
|---|:--:|---|:--:|---|
| D1 Ingestão | 4 | Intellihub, ThingsBoard, Kraken | **3–4** | Forte — medidor + edge (do mapa de hardware) |
| D2 Dados & Twin | 3 | maioria | ~1 | Build (infra padrão) |
| D3 Inteligência | 4 | Kraken, AutoGrid, gridX | ~0–1 | Build-on EMHASS/PyPSA; degrau central |
| D4 EMS/Controle | 4 | **OpenEMS**, Eniris | ~1 | **Build-on OpenEMS** |
| D5 DERMS/Frota | 4 | AutoGrid, Kraken, Kiwigrid, Intellihub, Next Kraftwerke | **~2** | **Herdar parcial — protótipo de DERMS** |
| D6 VPP/Mercado | 4 | Kraken, AutoGrid, Kiwigrid, Eniris, Next Kraftwerke, Sympower | ~0 | Build + tropicalizar CCEE |
| **D7 CCEE/BR** | **0** | **NINGUÉM** | **2** (único BR) | **Espaço vazio a ocupar — o fosso** |
| D8 Multi-tenant/API | 4 | Kraken, gridX, Kiwigrid, Eniris, ThingsBoard | ~1 | Build (multi-tenant desde a fundação) |
| **D9 Agent-fabric AI-native** | **~3\*** | Volttron (paradigma, legado) | ~0 | **Fronteira quase vazia — LLM-agents ninguém tem** |
| D10 Apps/UX | 4 | Kraken/Octopus, Tibber, Zerofy, HA | ~1 | Build (ref Zerofy/Tibber) |
| D11 Infra/Sec/MLOps | 4 | Kraken, Kiwigrid | ~1 | Build (stack OSS padrão) |
| D12 Comercial | 4 | Kraken | ~1 | Build/buy |

\* *D9: o teto "3" do Volttron é de **agentes clássicos** (não-LLM). Em agent-fabric **AI-native (LLM)**, o teto real do mercado é ~0 — fronteira aberta.*

**Dois espaços vazios:** **D7 (CCEE/BR)** e **D9 (agent-fabric AI-native LLM)** — onde o EOS-DENO nasce à frente. **D5 (DERMS)** é o único domínio com **ativo herdado** (o protótipo).

---

## 5 · Assessment open-source — build vs. fork vs. buy *(por domínio)*

| Domínio | Melhor fundação OSS | Maturidade como base | O que se herda vs. constrói | Veredito |
|---|---|:--:|---|---|
| D1 Ingestão | ThingsBoard / OpenEMS | Alta | Device mgmt, telemetria, drivers | **Fork/build-on** |
| D2 Dados & Twin | (infra: Timescale/Kafka) | Alta (infra) | TSDB, streaming; modelo de ativo = build | Build-on infra |
| D3 Inteligência | EMHASS + PVLib / PyPSA / OR-Tools | Média-alta | A matemática (LP/MPC, forecast); produtizar/escalar = build | **Build-on a matemática** |
| D4 EMS/Controle | **OpenEMS** | **Alta** | EMS edge+backend, agnosticismo, modular | **Fork forte** |
| D5 DERMS/Frota | OpenEMS Backend / Volttron | Média | Agregação parcial, controle distribuído; DERMS de mercado = build | Build-on parcial |
| D6 VPP/Mercado | OpenADR/OpenLEADR | Baixa (só DR) | Sinalização de DR; bidding/mercado = build | **Build** |
| **D7 CCEE/BR** | **nenhuma** | — | Tudo | **Build puro — moat** |
| D8 Multi-tenant/API | ThingsBoard + Keycloak + Kong | Alta | Multi-tenancy, identidade, API gateway | **Build-on infra** |
| **D9 Agent-fabric** | Volttron + frameworks LLM abertos | Média (conceito) / baixa (impl. moderna) | Paradigma de agentes; runtime LLM moderno = build | **Build (com inspiração)** |
| D10 Apps/UX | Home Assistant (referência) | Média | Padrão de UX/integrações; app próprio = build | Build (ref) |
| D11 Infra/Sec/MLOps | k8s / Prometheus / Vault / MLflow | Alta | Stack cloud-native inteiro | **Build-on (padrão)** |
| D12 Comercial | — | — | Billing/CRM = build/buy | Buy/build |

**Tese de build:** **fork/build-on o open-source nas camadas commodity e de EMS de borda** (D1, D4, D8, D11) e **construir os diferenciadores** (D7 CCEE, D9 agent-fabric, e D5/D6 tropicalizado para o BR).

---

## 6 · Findings

1. **O padrão do hardware se repete, deslocado:** tetos vazios em **D7 (CCEE/BR)** e **D9 (agent-fabric AI-native LLM)**.
2. **Há um ativo herdado no software:** **D5 (DERMS) já tem protótipo.**
3. **Open-source é fundação real em ~metade dos domínios** (D1/D3/D4/D8/D11), **não no moat** (D7/D9). Fork as commodities, construa os diferenciadores.
4. **Intellihub é a prova de conceito** da tese medidor+plataforma+VPP — sem AI-native e sem CCEE. O diferencial está nos dois domínios vazios.
5. **A ameaça (Kraken) é a mais completa, mas tem zero BR e não é AI-native (LLM).** O moat duplo (CCEE + agent-fabric) não vem de prateleira.

---

*Scoring de software · 16 players · dupla lente (comparável + build-on) · 0–4 no nível de macro-domínio. Tiers tagueados. Fontes oficiais. Projeto EOS-DENO.*
