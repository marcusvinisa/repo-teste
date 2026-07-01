# 03 · Engenharia de CLOUD — HEMS CORRENTE

> **Status:** Draft v0.1 · **2026-06-26** · Camada: Nuvem · Obedece aos contratos de `00-ARQUITETURA`.
> **Objeto:** reimplementar a stack SEMS da GoodWe — ingestão de telemetria, otimização/AI/forecast, motor de tarifa, Open-API, multi-tenant, OTA manager.

## 1 · Objetivo e escopo

**Dentro:** ingestão MQTT, armazenamento (time-series + relacional), otimização/forecast, motor de tarifa, comando assinado, Open-API, RBAC multi-tenant, gestão de frota/OTA.
**Fora:** UI (vive em `04`); firmware (`02`).

## 2 · Requisitos

### Funcionais (paridade SEMS + Open-API GoodWe — [F], fonte white paper/datasheet)
- **Ingestão** de telemetria de frota via MQTT/TLS (mTLS por device).
- **Otimização AI** de autoconsumo + tarifa + **forecast habit-based** de geração/carga; **scheduling** despachado à borda. *(datasheet: "AI learns and forecasts", "AI-Optimized Scheduling")*
- **Motor de tarifa**: tarifa dinâmica/negativa, auto-conexão a plataformas de trading. *(datasheet)*
- **Open-API** p/ terceiros: **raw data · processed data · batch control** *(white paper, Fig. 4)*.
- **Comando** assinado p/ a borda (setpoints, zero-export, SG-Ready, shutdown).
- **Gestão de frota**: provisioning, OTA manager, saúde de device/integração.
- **Multi-tenant**: gerador, distribuidor, agregador/orquestrador, integrador/instalador, consumidor.

### Não-funcionais
| Parâmetro | Alvo | Origem |
|---|---|---|
| Escala de frota | **200 → 20.000 devices/mês** de ingestão | [F] memória do projeto |
| Ingestão sustentada | N devices × (1–5 s) sem perda; backpressure | [E] derivado de §2 |
| Retenção telemetria | quente 90 d / frio ≥ 5 anos | [H] |
| Disponibilidade ingestão | ≥ 99,9 % | [H] |
| Latência comando→borda | ≤ 2 s p95 (online) | [H] |
| Isolamento entre tenants | lógico + por-linha (RLS) | [F-decisão] |

## 3 · Especificação técnica

### 3.1 Arquitetura
```
        MQTT/TLS (mTLS X.509 por device)
 borda ───────────────►  Broker  ──►  Ingest svc  ──►  TSDB (telemetria)
                          (IoT Core /        │               │
                           EMQX)             ▼               ▼
                                      Stream/ETL      Postgres (metadados,
                                          │            tenants, devices, RBAC)
                       ┌──────────────────┼───────────────────┐
                       ▼                   ▼                   ▼
                Forecast (ML)      Otimizador          Motor de tarifa
                geração/carga      (autoconsumo +      (dinâmica/negativa,
                       │            tarifa + restr.)    trading)
                       └─────────────►  Scheduler  ──► comando assinado ──► borda
                                            │
                       REST/WS  ◄───────────┴──────────►  App/Web (04)
                       Open-API ◄──────────────────────►  Terceiros (raw/proc/batch)
```

### 3.2 Identidade e provisioning de frota (decisão transversal `00` §4)
- **AWS IoT Fleet Provisioning by claim** (ou equivalente) — caminho de migração **já confirmado** no smartmeter.
- **X.509 único por device** — elimina o **cert de frota compartilhado** (achado anterior). Política IoT por device limita tópicos (telemetria own-device, comando own-device).

### 3.3 Caminho de comando (fecha o blind relay path)
- Comando nasce no scheduler/operador → **assinado** pela nuvem → publicado no tópico do device-alvo → **validado na borda** (`02` §3.4) antes de virar Modbus write.
- Toda escrita é auditada (quem, quando, device, registrador, valor, resultado).

### 3.4 Dados
| Domínio | Store | Notas |
|---|---|---|
| Telemetria (séries) | **TSDB** (Timescale / Timestream) | downsampling + retenção quente/frio |
| Metadados/multi-tenant | **Postgres** | tenant, planta, device, usuário, RBAC, **RLS** |
| Auditoria de comando | append-only | imutável |
| Forecast/otimização | feature store + artefatos de modelo | versionado |

### 3.5 Multi-tenant & RBAC
Hierarquia de papéis reaproveitando o modelo do FieldOps (**Distribuidor → Revendedor → Instalador**) + papéis de plataforma (operador/agregador, consumidor). Isolamento por **Row-Level Security** no Postgres + escopo de tópico MQTT por device.

### 3.6 Delta Brasil (nuvem)
- **SCEE / compensação**: o motor econômico modela **autoconsumo + compensação**, não spot residencial. Tarifa dinâmica entra como **opcionalidade** (valor presente ~0 no caso-base, vide `00` §1).
- **Zero-export ANEEL RN 1000/2021** como modo de controle de injeção primário (não RCR alemão).

## 4 · Interfaces
- **↔ Borda (`02`):** MQTT/TLS, envelope canônico (`00` §3), comando assinado, ACK.
- **↔ App/Web (`04`):** **REST** (config/CRUD) + **WebSocket** (tempo real).
- **↔ Terceiros:** **Open-API** (raw/processed/batch control) com OAuth2 + rate-limit por tenant.

## 5 · Decisões e trade-offs
| Decisão | Opções | Veredicto |
|---|---|---|
| Broker MQTT | **AWS IoT Core** (gerenciado, fleet provisioning pronto) vs **EMQX self-hosted** (custo/controle) | **IoT Core no v1** (alinha ao que você já roda); reavaliar custo em escala → gate `00` §6.4 |
| TSDB | Timestream (serverless) vs **Timescale** (Postgres-native, joins) | Timescale por afinidade relacional [H] |
| Otimização | regras → **MILP/heurística** → ML | começar regras+heurística; ML quando houver dado de frota |
| Forecast | comprar vs treinar | treinar quando a frota gerar volume; placeholder estatístico no v1 |

## 6 · Riscos técnicos
- **Custo de IoT gerenciado em 20k devices**: modelar US$/device/mês antes de travar broker (gate).
- **Frota heterogênea** (mapas Modbus por modelo/versão): catálogo de drivers versionado na nuvem, empurrado por OTA.
- **Multi-tenant leak**: RLS + testes de isolamento automatizados como gate de release.
- **Comando malicioso/replay**: assinatura + nonce + validação na borda; auditoria imutável.
- **Regra que não existe** (tarifa dinâmica/trading BR): tratar como opcionalidade, nunca caso-base — não construir P&L em cima.

## 7 · Definition of Done (Cloud — `engineering-process`, Backend/Integração)
```
[ ] Contrato de schema (envelope + Open-API) versionado e publicado
[ ] Ingestão testada sob carga de frota-alvo (backpressure, sem perda)
[ ] Fleet provisioning by claim + X.509 por device funcionando E2E
[ ] Comando assinado validado na borda (teste de write fora de faixa/replay)
[ ] Isolamento multi-tenant (RLS) com teste automatizado de vazamento
[ ] Open-API (raw/processed/batch) com OAuth2 + rate-limit + docs (Swagger)
[ ] OTA manager: rollout faseado + rollback de frota testado
[ ] Observabilidade: saúde de device/integração + alertas configurados
[ ] Rollback plan documentado p/ serviços de risco · deploy em staging testado
```
