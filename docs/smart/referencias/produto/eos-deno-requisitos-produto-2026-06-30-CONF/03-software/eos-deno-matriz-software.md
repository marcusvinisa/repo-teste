# EOS-DENO · Matriz de Software — Catálogo de Microsserviços do Energy OS

> **O que é:** a plataforma ideal de software de energia decomposta em **microsserviços** — para que o produto seja **personalizável por persona/cenário** (cada bundle ativa um subconjunto). Complementa o mapa de hardware (`eos-deno-matriz-funcionalidades.md`); aqui **o device é insumo**. Escopo combinado **1+2+3**: plataforma de orquestração (cérebro acima do medidor) + OS completo (edge↔cloud↔mercado↔apps↔agentes) + grid/mercado (DERMS/VPP + CCEE/ACL).

**Como ler cada serviço:** `#` numeração de domínio · **o que faz** (destino) · **como é feito** (mecanismo/tech) · **personas** que consomem · ao fim de cada domínio, a **fundação OSS candidata** (open-source como comparável **e** base de build-on — detalhe no scoring/spec).

**Personas:** CON consumidor · INT integrador · COM comercializadora · AGG agregador/VPP · GER gerador · DSO distribuidor · ORQ orquestrador · *todas* = núcleo comum. (Ver `eos-deno-personas-casos-de-uso.md`.)

**Dois blocos:** **domínios de energia** (S0–S12, a lógica do setor) e **plataforma & operação** (S13–S17, cross-cutting de qualquer SaaS sério). `★` = domínio de alto valor estratégico / diferenciador.

---

## Bloco I — Domínios de energia

### S0 · Ingestão & Conectividade
*A porta de entrada — leva dado do device para a plataforma e comando de volta.*

| # | Microsserviço | O que faz | Como é feito | Personas |
|---|---|---|---|---|
| S0.1 | Device Gateway / Connector | Ingere telemetria de medidores/inversores/baterias | Adaptadores de protocolo (Modbus/MQTT/REST) + fila de mensagens | todas |
| S0.2 | Protocol Adapter Registry | Biblioteca de drivers por fabricante (agnosticismo no dado) | Plugins versionados, mapeamento p/ modelo canônico | todas |
| S0.3 | Edge Sync / Store-and-forward | Sincroniza estado edge↔cloud, buffer offline | Protocolo de sync + reconciliação + idempotência | todas |
| S0.4 | Command Dispatch Bus | Entrega setpoints/comandos ao edge com confirmação | Command queue + ack + retry idempotente | CON, AGG, DSO, ORQ |

*Fundação OSS candidata:* **OpenEMS** (camada edge/connector), **ThingsBoard / OpenRemote** (gateway IoT).

### S1 · Plataforma de Dados & Telemetria
*A memória — onde todo dado vive e flui.*

| # | Microsserviço | O que faz | Como é feito | Personas |
|---|---|---|---|---|
| S1.1 | Time-Series Store | Armazena medição em alta resolução | TSDB (TimescaleDB/InfluxDB), retenção configurável | todas |
| S1.2 | Event Bus / Streaming | Pub/sub de eventos p/ serviços reativos | Kafka/NATS | todas |
| S1.3 | Data Lake | Histórico bruto p/ analytics e ML | Object store + catálogo | ORQ, AGG, COM |
| S1.4 | Telemetry API | Consulta de telemetria por serviços/apps | REST/GraphQL + cache | todas |

*Fundação OSS candidata:* **TimescaleDB**, **Apache Kafka/NATS** (infra aberta).

### S2 · Modelo de Ativos & Digital Twin
*A verdade sobre o que existe e em que estado.*

| # | Microsserviço | O que faz | Como é feito | Personas |
|---|---|---|---|---|
| S2.1 | Asset Registry | Cadastro de UCs, medidores, inversores, baterias, VE, cargas | Modelo de dados canônico de ativos | todas |
| S2.2 | Topology Model | Relação elétrica (fase, circuito, ponto de conexão, UC↔usina em GD) | Grafo de topologia | INT, GER, DSO, AGG |
| S2.3 | Device Abstraction | Modelo canônico que abstrai fabricantes (agnosticismo na plataforma) | Capability model + tradução | todas |
| S2.4 | Digital Twin State | Estado em tempo real de cada ativo/site | State store + projeções de eventos | CON, AGG, ORQ |

*Fundação OSS candidata:* modelagem própria (CIM/IEC 61968 como referência de modelo).

### ★ S3 · Forecasting (Previsão)
*Olhar para frente — geração, carga, preço.*

| # | Microsserviço | O que faz | Como é feito | Personas |
|---|---|---|---|---|
| S3.1 | Solar Forecast | Prevê geração por site (intraday→multi-dia) | Físico (clear-sky) + ML, ajustado por histórico | CON, AGG, GER |
| S3.2 | Load Forecast | Prevê consumo por UC | ML (boosting/LSTM) sobre histórico + clima/calendário | CON, AGG, COM |
| S3.3 | Price Forecast | Prevê preço (PLD/spot) | Série temporal + sinais de mercado | AGG, COM, GER |
| S3.4 | Weather Ingestion | Ingere meteorologia/irradiância | Conectores de API meteorológica/satélite | todas (via S3) |

*Fundação OSS candidata:* **pvlib** (modelo solar físico), libs ML abertas (scikit-learn, etc.). *Forecasting-as-a-service* — consumido por S4/S7/S12.

### ★ S4 · Otimização & Scheduling
*O cérebro econômico — decidir o melhor despacho.*

| # | Microsserviço | O que faz | Como é feito | Personas |
|---|---|---|---|---|
| S4.1 | Optimization Engine | Resolve despacho ótimo (carga/descarga, cargas) | Solver MILP/MPC, horizonte rolante | CON, AGG, GER |
| S4.2 | Tariff & Price Model | Modela tarifa branca/bandeiras/dinâmica/PLD | Regras + ingestão de estrutura tarifária BR | CON, COM |
| S4.3 | Multi-objective Policy | Pondera custo × bateria × CO₂ × crédito | Função-objetivo configurável | CON, GER |
| S4.4 | RL Policy Service | Políticas adaptativas aprendidas | Aprendizado por reforço | AGG, ORQ |
| S4.5 | Plan / Schedule Service | Gera e versiona o plano 24–48h | Receding horizon, re-otimiza 15min | CON, AGG |

*Fundação OSS candidata:* **OR-Tools**, **PyPSA**, **oemof** (otimização de sistemas de energia); **EMHASS** (otimização residencial via Home Assistant).

### ★ S5 · Controle & EMS Orchestration
*As mãos na nuvem — aplicar as estratégias com segurança.*

| # | Microsserviço | O que faz | Como é feito | Personas |
|---|---|---|---|---|
| S5.1 | EMS Core / Control Loop | Aplica estratégias (autoconsumo, zero-export, peak shaving) | Rule engine + setpoints em malha | CON, GER |
| S5.2 | Safety & Guardrails | Limites de proteção (anti-backfeed, anti-trip, SOC) | Validação pré-comando + interlocks | todas |
| S5.3 | Scene / Mode Manager | Modos e cenas por usuário (SG-Ready, cenas A4) | Regras nomeadas + agendamento | CON |
| S5.4 | Edge Policy Distribution | Empacota plano/regras p/ o edge operar offline | Bundle versionado + sync | CON, ORQ |

*Fundação OSS candidata:* **OpenEMS** (EMS edge+backend, a base mais forte).

### ★ S6 · DERMS / Fleet Orchestration
*Coordenar muitos ativos como um só.*

| # | Microsserviço | O que faz | Como é feito | Personas |
|---|---|---|---|---|
| S6.1 | Fleet Manager | Gere frota de devices/sites em escala | Agrupamento + rollout em ondas + health | INT, ORQ, AGG |
| S6.2 | Group / Cohort Control | Comando coordenado de grupos (multi-UC, multi-site) | Dispatch em massa + confirmação | AGG, DSO |
| S6.3 | Grid Signal Handler | Recebe sinais do DSO (RCR/§14a/DOE) e traduz em ordens | Conectores + tradução p/ setpoints | DSO, AGG |
| S6.4 | Curtailment Orchestrator | Corta geração/carga por ordem, com auditoria | Dispatch + trilha de auditoria | DSO, AGG |

*Fundação OSS candidata:* sem base OSS madura de DERMS (espaço de build); **Volttron** cobre controle distribuído.

### ★ S7 · VPP / Mercado / Trading
*Onde a flexibilidade vira receita.*

| # | Microsserviço | O que faz | Como é feito | Personas |
|---|---|---|---|---|
| S7.1 | Aggregation Engine | Agrega flexibilidade da frota como recurso único | Somatório + qualificação de recurso | AGG |
| S7.2 | Bidding / Market Optimization | Posiciona ofertas em mercados (DA/ID/imbalance) | Algoritmo de bidding | AGG, COM |
| S7.3 | Market Connectors | Integra a mercados/operadores | Adaptadores (CCEE, futuros padrões BR) | AGG, COM |
| S7.4 | Ancillary Services | FCR/aFRR/mFRR, reserva, suporte de tensão | Resposta a sinal (droop/AGC) + medição de baseline | AGG, DSO |
| S7.5 | DR Program Manager | Programas de resposta da demanda | Eventos + incentivo + medição | AGG, DSO, COM |

*Fundação OSS candidata:* **OpenADR / OpenLEADR** (sinalização de DR). Mercado/bidding = build.

### ★ S8 · CCEE / Liquidação / Billing BR
*O fosso brasileiro — onde o mercado de energia BR se fecha.*

| # | Microsserviço | O que faz | Como é feito | Personas |
|---|---|---|---|---|
| S8.1 | CCEE Integration | Medição p/ contabilização/liquidação CCEE | Conectores CCEE + medição p/ faturamento | COM, GER, AGG |
| S8.2 | Credit Allocation / Rateio | Rateio de créditos de GD compartilhada (Lei 14.300) entre UCs | Motor de rateio por UC/percentual | GER, COM, CON(B) |
| S8.3 | Settlement Service | Liquidação no mercado livre (ACL) | Contabilização + conciliação | COM, AGG |
| S8.4 | Energy Billing | Fatura de energia/assinatura por UC | Rating + invoice + integração fiscal | COM |

*Fundação OSS candidata:* **nenhuma** — específico do Brasil. É **build puro e moat regulatório** (ninguém estrangeiro tem).

### ★ S11 · Agent-Fabric / AI-native
*O diferencial — operar por agentes, não por telas.* (numerado fora de ordem para manter S9/S10 como plataforma)

| # | Microsserviço | O que faz | Como é feito | Personas |
|---|---|---|---|---|
| S11.1 | Agent Runtime | Executa agentes LLM com ferramentas | Runtime + orquestração de tools | todas |
| S11.2 | Tool Registry | Ferramentas que leem/escrevem ativos/mercados sob política | Schema de tool + auth + escopo | ORQ |
| S11.3 | Per-Persona Agents | Agentes por persona (consumidor, agregador, integrador…) | Prompt + política + memória por persona | todas |
| S11.4 | Copilot / NL Interface | Interface conversacional operacional | LLM + RAG sobre dados/controles | todas |
| S11.5 | Agent Guardrails & Policy | Limites do que cada agente pode fazer | Policy engine + human-in-the-loop | ORQ |

*Fundação OSS candidata:* **Volttron** (DOE — plataforma de agentes p/ controle distribuído, análogo mais próximo); frameworks de agentes LLM abertos.

### S12 · Apps & Experiência
*A face — onde cada persona toca o produto.*

| # | Microsserviço | O que faz | Como é feito | Personas |
|---|---|---|---|---|
| S12.1 | Consumer App | App do dono (consumo, economia, controle) | Front-end sobre API | CON |
| S12.2 | Installer Portal | Comissionamento, diagnóstico, frota do integrador | Portal web | INT |
| S12.3 | Operator Dashboard | Dashboard do agregador/orquestrador | Dashboard sobre API | AGG, ORQ, DSO |
| S12.4 | Engagement & Notifications | Economia em R$/CO₂, gamificação, alertas | Eventos + push/email | CON, COM |

*Fundação OSS candidata:* **Home Assistant** (referência de UX residencial + EMHASS), frameworks de front-end abertos.

---

## Bloco II — Plataforma & Operação *(cross-cutting)*

### S9 · Identidade, Multi-tenant & RBAC
| # | Microsserviço | O que faz | Como é feito | Personas |
|---|---|---|---|---|
| S9.1 | Auth & Identity | Autenticação (OAuth/OIDC) | Provedor de identidade | todas |
| S9.2 | Tenant Isolation | Isolamento multi-tenant | Tenant context + partição de dados | ORQ, COM, INT, AGG |
| S9.3 | RBAC & Permissions | Papéis e permissões por persona | Policy engine | ORQ |
| S9.4 | White-label Theming | Marca/domínio por tenant | Config por tenant | COM, INT, AGG |

*Fundação OSS candidata:* **Keycloak / Ory** (identidade aberta).

### ★ S10 · API, SDK & Ecossistema de Devs
| # | Microsserviço | O que faz | Como é feito | Personas |
|---|---|---|---|---|
| S10.1 | API Gateway | REST/GraphQL público + rate limit | Gateway + autenticação | todas (externos) |
| S10.2 | Webhooks / Events | Assinaturas de eventos para terceiros | Entrega de webhook | INT, COM, AGG |
| S10.3 | SDK & Docs | SDK + documentação OpenAPI | Geração a partir do schema | INT, COM, AGG |
| S10.4 | Module Marketplace | Catálogo de módulos/apps de parceiros | Registry + billing de módulo | ORQ, INT |

*Fundação OSS candidata:* **Kong / APISIX** (gateway aberto).

### S13 · MLOps & Plataforma de Dados Científicos
| # | Microsserviço | O que faz | Como é feito | Personas |
|---|---|---|---|---|
| S13.1 | Model Registry | Versiona modelos de previsão/otimização | Registry de modelos | ORQ |
| S13.2 | Training Pipeline | Treina com dados da frota | Pipeline de treino agendado | ORQ |
| S13.3 | Feature Store | Features compartilhadas entre modelos | Store online/offline | ORQ |
| S13.4 | Drift Monitoring | Monitora degradação de modelo | Métricas de drift + alerta | ORQ |

*Fundação OSS candidata:* **MLflow**, **Feast** (MLOps aberto).

### S14 · Observabilidade, Confiabilidade & SRE
| # | Microsserviço | O que faz | Como é feito | Personas |
|---|---|---|---|---|
| S14.1 | Monitoring & Logging | Métricas/logs da plataforma | Stack de observabilidade | ORQ |
| S14.2 | Alerting & Incident | Alertas + resposta a incidente | Regras de alerta + runbook | ORQ |
| S14.3 | SLA & Uptime | Garantia de serviço por tenant | SLO/SLA + relatório | ORQ, COM |
| S14.4 | Fleet Health | Saúde dos devices (RMA, falhas) | Health checks + telemetria | INT, ORQ |

*Fundação OSS candidata:* **Prometheus / Grafana / OpenTelemetry**.

### S15 · Segurança & Compliance
| # | Microsserviço | O que faz | Como é feito | Personas |
|---|---|---|---|---|
| S15.1 | Encryption & Secrets | TLS, encriptação, secrets | KMS + TLS em trânsito | ORQ |
| S15.2 | Audit Log | Trilha de auditoria (comandos, acessos) | Log append-only imutável | ORQ, DSO |
| S15.3 | Compliance | LGPD, SOC 2 / ISO 27001 | Controles + evidência + relatório | ORQ |
| S15.4 | Secure SDLC | Assinatura, pen-test, supply chain | Pipeline seguro + SBOM | ORQ |

*Fundação OSS candidata:* **HashiCorp Vault / OpenBao**, OpenTelemetry p/ auditoria.

### S16 · Deploy & Infra
| # | Microsserviço | O que faz | Como é feito | Personas |
|---|---|---|---|---|
| S16.1 | Cloud-native Runtime | Orquestração de contêineres, multi-region | Kubernetes | ORQ |
| S16.2 | CI/CD & IaC | Entrega contínua + infra como código | Pipeline + IaC | ORQ |
| S16.3 | Edge Runtime Distribution | Distribui runtime ao edge (OTA de software) | OTA + versionamento | ORQ |
| S16.4 | Deployment Modes | SaaS / self-hosted / híbrido | Empacotamento por modo | ORQ, COM |

*Fundação OSS candidata:* **Kubernetes**, **ArgoCD / Terraform** (infra aberta).

### S17 · Comercial & Monetização
| # | Microsserviço | O que faz | Como é feito | Personas |
|---|---|---|---|---|
| S17.1 | Subscription Billing | Cobrança recorrente por device/seat | Billing engine | COM, ORQ |
| S17.2 | Usage Metering | Mede uso (API, dispatch) p/ cobrança | Metering de uso | ORQ |
| S17.3 | Revenue-share | Partilha de receita de flexibilidade | Split por contrato | AGG, ORQ |
| S17.4 | CRM / Partner Mgmt | Gestão de clientes/parceiros | Integração CRM | COM, INT |

*Fundação OSS candidata:* integração (não core); build/buy conforme caso.

---

## Notas de fechamento

- **O diferencial é S11 (agent-fabric) + S8 (CCEE/BR).** O resto do mundo tem S0–S7 e S9–S17 em alguma maturidade; o agent-fabric AI-native e a camada CCEE/ACL brasileira são onde o EOS-DENO nasce à frente — e onde **não há fundação OSS pronta** (build puro).
- **Open-source é fundação real em ~metade dos domínios** (OpenEMS em S0/S5, Volttron em S6/S11, OR-Tools/PyPSA/EMHASS em S4, OpenADR em S7, ThingsBoard em S0, e a stack de infra/observabilidade em S13–S16). O scoring e a spec vão decidir, **por domínio**, build vs. fork vs. buy.
- **A modularização micro é o que viabiliza a personalização por persona/cenário** (ver os bundles em `eos-deno-personas-casos-de-uso.md`): ativar/desativar serviços em vez de reescrever o produto.
- **Ressalva regulatória:** S7 (VPP/ancilares) e parte de S8 (mercado livre BT) entram como **capacidade técnica pronta, monetização gradual** — alinhado à matriz dos 18 cenários.

---

*Catálogo de microsserviços · camada de software · Projeto EOS-DENO. Complementa o mapa de hardware. Domínios de energia (S0–S12) + plataforma/operação (S13–S17). Fundações OSS são candidatas de build-on a validar no scoring. A coluna "como" é nível-arquitetural, não datasheet.*
