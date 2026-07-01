# EOS-DENO · Scoring de Software — 16 Players contra o Catálogo de Microsserviços

> **Dupla lente** (como você pediu): cada player é avaliado como **comparável competitivo** *e* como **fundação de build-on** (especialmente os open-source). Pontuação **0–4** de maturidade, no nível de **macro-domínio**, com `–` onde a fonte não confirma. Disciplina de fato-confirmado; pesquisa web nas fontes oficiais.

**Escala:** 0 ausente · 1 observa/básico · 2 controla/funcional · 3 otimiza/maduro · 4 líder/completo.

**Tiers (banana-com-banana — não comparar entre tiers cegamente):**
`PLAT` plataforma utility-grade · `VPP-OP` operador de VPP (+ software) · `APP` app de consumidor · `OSS` framework open-source.

**Macro-domínios** (consolidam os ~18 do catálogo): **D1** Ingestão · **D2** Dados & Twin · **D3** Inteligência (forecast+otim.) · **D4** EMS/Controle · **D5** DERMS/Frota · **D6** VPP/Mercado · **D7** CCEE/BR · **D8** Multi-tenant/API · **D9** Agent-fabric AI-native · **D10** Apps/UX · **D11** Infra/Sec/MLOps · **D12** Comercial.

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
| **OpenADR/LEADR** | 2 | – | – | – | – | 3 | 0 |

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
| OpenADR/LEADR | – | – | – | – | – | *bloco* |

**Leitura:** a média mede **completude/largura** — penaliza OSS de nicho e apps, que são fortes só onde atuam. Como no hardware, isso **não** é ranking de "melhor": é mapa de cobertura. Kraken lidera completude (era esperado — é um OS de utility). Os OSS aparecem baixo aqui, mas são **altos como fundação** no seu domínio (ver §5).

---

## 4 · Teto de mercado por domínio — e o ponto de partida do EOS-DENO

| Domínio | Teto | Quem detém | EOS-DENO hoje (estim.) | Leitura |
|---|:--:|---|:--:|---|
| D1 Ingestão | 4 | Intellihub, ThingsBoard, Kraken | **3–4** | Forte — temos medidor + edge (do mapa de hardware) |
| D2 Dados & Twin | 3 | maioria | ~1 | Build (infra padrão) |
| D3 Inteligência | 4 | Kraken, AutoGrid, gridX | ~0–1 | Build-on EMHASS/PyPSA; é o degrau central |
| D4 EMS/Controle | 4 | **OpenEMS**, Eniris | ~1 | **Build-on OpenEMS** (fundação OSS forte) |
| D5 DERMS/Frota | 4 | AutoGrid, Kraken, Kiwigrid, Intellihub, Next Kraftwerke | **~2** | **Herdar parcial — temos protótipo de DERMS** |
| D6 VPP/Mercado | 4 | Kraken, AutoGrid, Kiwigrid, Eniris, Next Kraftwerke, Sympower | ~0 | Build + tropicalizar CCEE |
| **D7 CCEE/BR** | **0** | **NINGUÉM** | **2** (único BR) | **Espaço vazio a ocupar — o fosso** |
| D8 Multi-tenant/API | 4 | Kraken, gridX, Kiwigrid, Eniris, ThingsBoard | ~1 | Build (multi-tenant desde a fundação) |
| **D9 Agent-fabric AI-native** | **~3*** | Volttron (paradigma, legado) | ~0 | **Fronteira quase vazia — LLM-agents ninguém tem** |
| D10 Apps/UX | 4 | Kraken/Octopus, Tibber, Zerofy, HA | ~1 | Build (ref Zerofy/Tibber) |
| D11 Infra/Sec/MLOps | 4 | Kraken, Kiwigrid | ~1 | Build (stack OSS padrão) |
| D12 Comercial | 4 | Kraken | ~1 | Build/buy |

\* *D9: o teto "3" do Volttron é de **agentes clássicos** (não-LLM). Em agent-fabric **AI-native (LLM)**, o teto real do mercado é ~0 — é fronteira aberta.*

**Dois espaços vazios, como no hardware:** **D7 (CCEE/BR)** — ninguém estrangeiro tem; e **D9 (agent-fabric AI-native LLM)** — ninguém tem ainda. São os dois lugares onde o EOS-DENO nasce à frente. E **D5 (DERMS)** é o único domínio de software onde já há **ativo herdado** (o protótipo).

---

## 5 · Assessment open-source — build vs. fork vs. buy *(por domínio)*

O ângulo central que você pediu: onde o open-source é **fundação real** (build-on) e onde é **build puro**.

| Domínio | Melhor fundação OSS | Maturidade como base | O que se herda vs. constrói | Veredito |
|---|---|:--:|---|---|
| D1 Ingestão | ThingsBoard / OpenEMS | Alta | Device mgmt, telemetria, drivers | **Fork/build-on** |
| D2 Dados & Twin | (infra: Timescale/Kafka) | Alta (infra) | TSDB, streaming; modelo de ativo = build | Build-on infra |
| D3 Inteligência | EMHASS + PVLib / PyPSA / OR-Tools | Média-alta | A matemática (LP/MPC, forecast); produtizar e escalar p/ frota = build | **Build-on a matemática** |
| D4 EMS/Controle | **OpenEMS** | **Alta** | EMS edge+backend, agnosticismo, modular | **Fork forte** |
| D5 DERMS/Frota | OpenEMS Backend / Volttron | Média | Agregação parcial, controle distribuído; DERMS de mercado = build | Build-on parcial |
| D6 VPP/Mercado | OpenADR/OpenLEADR | Baixa (só DR) | Sinalização de DR; bidding/mercado = build | **Build** |
| **D7 CCEE/BR** | **nenhuma** | — | Tudo | **Build puro — moat** |
| D8 Multi-tenant/API | ThingsBoard + Keycloak + Kong | Alta | Multi-tenancy, identidade, API gateway | **Build-on infra** |
| **D9 Agent-fabric** | Volttron + frameworks LLM abertos | Média (conceito) / baixa (impl. moderna) | Paradigma de agentes; runtime LLM moderno = build | **Build (com inspiração)** |
| D10 Apps/UX | Home Assistant (referência) | Média | Padrão de UX/integrações; app próprio = build | Build (ref) |
| D11 Infra/Sec/MLOps | k8s / Prometheus / Vault / MLflow | Alta | Stack cloud-native inteiro | **Build-on (padrão)** |
| D12 Comercial | — | — | Billing/CRM = build/buy | Buy/build |

**A tese de build emergente:** **fork/build-on o open-source nas camadas commodity e de EMS de borda** (D1, D4, D8, D11 — onde OpenEMS, ThingsBoard e a stack cloud-native dão fundação madura) e **construir os diferenciadores** (D7 CCEE, D9 agent-fabric, e o D5/D6 tropicalizado para o BR). Não reescrever o que o open-source já resolveu; investir o time onde está o moat.

---

## 6 · Perfis (tier · força · valor de build-on)

- **Kraken** [PLAT] — o mais completo e a ameaça direta: retail+billing+DERMS+VPP+UX. **Build-on: zero** (proprietário). É o benchmark de "produto inteiro".
- **AutoGrid** [PLAT] — referência de DERMS/VPP/DR utility-grade + IEEE 2030.5. Build-on: zero.
- **gridX / Kiwigrid / Eniris** [PLAT] — plataformas white-label fortes em multi-tenant/API + EMS/DERMS/VPP. Referência de arquitetura de plataforma. Build-on: zero.
- **Intellihub** [PLAT] — **o paralelo mais próximo**: medidor + plataforma DeX de interoperabilidade/VPP, agnóstica, "many-to-many". Valida a tese medidor+software. Build-on: zero.
- **Next Kraftwerke / Sympower** [VPP-OP] — referência de VPP/mercado/ancilares reais; NEMOCS licenciável. Build-on: zero.
- **Tibber** [APP] — referência de UX + **API aberta** (o padrão de developer-experience a imitar). Build-on: zero, mas inspiração de API.
- **Zerofy** [APP] — referência de UX/scheduling residencial (a lição do hardware se repete). Build-on: zero.
- **Smappee** [APP] — monitoramento/NILM + EV. Build-on: zero.
- **OpenEMS** [OSS] — **a fundação de EMS mais forte** (D4 alto). Apache 2.0, edge+backend, agnóstico. **Build-on: alto.**
- **Volttron** [OSS] — **o análogo de agent-fabric** (D9 = 3 em agentes clássicos) + controle distribuído. Legado Python, foco building, agentes não-LLM. **Build-on: médio** (paradigma sim, arquitetura moderna não).
- **HA + EMHASS** [OSS] — **otimização residencial open-source** (LP/MPC + forecast). Escala doméstica, não frota. **Build-on: alto p/ a matemática** de D3/D4.
- **ThingsBoard** [OSS] — **base de plataforma IoT** multi-tenant (D1/D8/D10 fortes). Não específica de energia. **Build-on: alto p/ infra.**
- **OpenADR / OpenLEADR** [OSS] — **bloco** de sinalização de DR (D6.DR). Não é plataforma. **Build-on: pontual.**

---

## 7 · Findings & ponte para a spec de software

1. **O padrão do hardware se repete, deslocado.** No hardware, o teto vazio era VPP/CCEE + medição/hardware era o trunfo. No software, os tetos vazios são **D7 (CCEE/BR — ninguém)** e **D9 (agent-fabric AI-native LLM — ninguém)**. São os dois lugares de "ocupar".

2. **Há um ativo herdado no software, diferente do hardware.** **D5 (DERMS) já tem protótipo** — é o ponto de partida mais forte do lado software, e está num domínio onde o teto é 4 e há fundação OSS parcial (OpenEMS Backend, Volttron).

3. **Open-source é fundação real em ~metade dos domínios** (D1/D3/D4/D8/D11), mas **não no moat** (D7/D9). A decisão build/fork/buy é nítida: **fork as commodities, construa os diferenciadores.** OpenEMS (EMS), ThingsBoard (IoT/multi-tenant), EMHASS/PyPSA (otimização) e a stack cloud-native cortam meses de trabalho não-diferenciado.

4. **Intellihub é a prova de conceito da tese** medidor+plataforma+VPP — só que em AU/NZ, sem a camada AI-native e sem CCEE. É o "e se a gente não fizesse o agent-fabric nem o BR?" — vira mais um Intellihub. O diferencial está exatamente nos dois domínios vazios.

5. **A ameaça (Kraken) é a mais completa, mas tem zero BR e não é AI-native (LLM).** Ela tropicaliza rápido se quiser — daí o relógio competitivo. Mas o moat duplo (CCEE + agent-fabric) é o que ela não traz de prateleira.

**Para a spec de software (próximo `.md`), os três movimentos ficam:**
- **Herdar:** medidor/ingestão (D1) + **protótipo de DERMS (D5)** + o que o OSS dá de graça (OpenEMS, ThingsBoard, EMHASS, stack cloud-native).
- **Alcançar:** inteligência (D3), EMS completo (D4), VPP/mercado (D6), multi-tenant/API (D8), UX (D10) — tudo com fundação OSS + referência de incumbente.
- **Ocupar:** **CCEE/BR (D7)** e **agent-fabric AI-native (D9)** — os dois domínios onde o teto de mercado é vazio.

---

*Scoring de software · 16 players · dupla lente (comparável + build-on) · 0–4 no nível de macro-domínio · `–` = não documentado. Tiers tagueados (banana-com-banana). Fontes oficiais (Kraken, AutoGrid, Volttron, Intellihub, EMHASS pesquisados; demais por conhecimento + pesquisa do hardware). Projeto EOS-DENO. Próximo: spec de software (herdar/alcançar/ocupar) em `.md`.*
