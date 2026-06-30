# Referências — Absorção e Ajustes (estudos EOS-DENO + Discovery HEMS BR)

> Nota de **absorção e reconciliação** dos estudos curados anexados pelo usuário. Mapeia o material **EOS-DENO** e o **Discovery técnico-competitivo** contra a suite Smart, e registra os **ajustes adotados / propostos / adiados**. Conteúdo dos estudos = **curado e revisado pelo usuário**; tratado como fonte de alta confiança.

## 1. Estudos nesta pasta

| Arquivo | O que é |
|---|---|
| `eos-deno-personas-casos-de-uso.md` | 7 personas da cadeia + matriz dos 18 cenários do consumidor |
| `eos-deno-matriz-software.md` | Catálogo de microsserviços do "Energy OS" (S0–S17) + fundações OSS |
| `eos-deno-matriz-funcionalidades.md` | Árvore completa de capacidades EMS/HEMS/VPP/DER (mapa de engenharia, 00–09 + C&I + horizonte 2030) |
| `eos-deno-spec-produto-passo3.md` | Spec de **hardware** (herdar/alcançar/ocupar; medidor-sensor como moat) |
| `eos-deno-spec-software.md` | Spec de **software** (build/fork/buy por domínio; CCEE + agent-fabric = moat) |
| `eos-deno-scoring-software.md` | Scoring de 16 players (dupla lente: comparável + fundação build-on) |
| `discovery-tecnico-competitivo-hems-br.md` | Discovery técnico do HEMS BR derivado do GoodWe EzManager3000 (ADRs, regulação 2026, AWS IoT, OEM) |

> **EOS-DENO ≈ Smart.** Os estudos são a **mesma linha de produto** da nossa suite, com granularidade maior. A suite Smart é a documentação de produto/engenharia; o EOS-DENO acrescenta a lente de **scoring competitivo**, **build/fork/buy** e **agent-fabric AI-native**. Esta nota concilia os dois.

## 2. Mapa EOS-DENO ↔ Smart

| EOS-DENO | Equivalente na suite Smart |
|---|---|
| Personas CON/INT/COM/AGG/GER/DSO/ORQ | [01 Personas](../01-visao-e-prd.md) / [08 RBAC](../08-plataforma-cloud-e-apis.md) (hoje 4 — ver §4) |
| Matriz 18 cenários (níveis × arranjos) | [11 Matriz de cenários](../11-matriz-de-cenarios.md) — **idêntica** |
| Catálogo microsserviços S0–S17 | [08 Plataforma cloud](../08-plataforma-cloud-e-apis.md) (decomposição mais fina — ver §3) |
| S0.1/S0.2 (Gateway/Connector + Adapter Registry) | **repos** [`energy-connectors`](../../../repos/energy-connectors/) + [`energy-device-maps`](../../../repos/energy-device-maps/) |
| Mapa de funcionalidades 00–09 | [06 Hardware](../06-especificacao-hardware.md) + [10 Modos](../10-modos-de-operacao-e-features.md) |
| S8/D7 CCEE/BR + S11/D9 Agent-fabric | **moats** — ver §5 (novos diferenciais a registrar) |

## 3. Build / Fork / Buy por domínio (adotado do EOS-DENO)

Decisão estratégica de **não reescrever o que o OSS já resolve**; construir só os diferenciadores:

| Domínio | Veredito | Fundação OSS | Onde aplicar na suite |
|---|---|---|---|
| Ingestão/IoT/multi-tenant | **fork/build-on** | ThingsBoard, OpenRemote | [08](../08-plataforma-cloud-e-apis.md), repo `energy-connectors` |
| EMS/controle | **fork forte** | **OpenEMS** (Apache 2.0, edge+backend) | [07 edge](../07-especificacao-firmware-edge.md), [08](../08-plataforma-cloud-e-apis.md) |
| Otimização/forecast | **build-on a matemática** | EMHASS, PyPSA, OR-Tools, HiGHS, pvlib | [08 motor de otimização](../08-plataforma-cloud-e-apis.md) |
| DERMS/frota | **build-on parcial** | OpenEMS Backend, Volttron | [08 VPP](../08-plataforma-cloud-e-apis.md) |
| VPP/mercado | **build** (+OpenADR p/ DR) | OpenADR/OpenLEADR | [08](../08-plataforma-cloud-e-apis.md) |
| Multi-tenant/API/identidade | **build-on infra** | Keycloak/Ory, Kong/APISIX | [08 IAM](../08-plataforma-cloud-e-apis.md) |
| Infra/observabilidade/MLOps | **build-on padrão** | k8s, Prometheus/Grafana/OTel, MLflow, Vault | [08 §8](../08-plataforma-cloud-e-apis.md) |
| **CCEE/BR** | **build puro — moat** | nenhuma | §5 |
| **Agent-fabric AI-native** | **build (inspirado em Volttron)** | frameworks LLM | §5 |
| Drivers locais Modbus | build-on | pymodbus/libmodbus + SunSpec | repo `energy-device-maps` |

> **Ação:** referenciar estas fundações OSS como candidatas de build-on na [plataforma cloud](../08-plataforma-cloud-e-apis.md) e nos repos (já feito nos READMEs dos repos). `[PREMISSA: validar fork vs build no início do build de cada serviço]`.

## 4. Reconciliação de personas (4 → 7) — **proposta**

A suite Smart usa **4 personas**; o EOS-DENO usa **7** (mais granular e curado):

| EOS-DENO | Smart (atual) |
|---|---|
| CON consumidor/prosumidor | Morador ✅ |
| INT integrador/EPC | Instalador ✅ |
| COM comercializadora | (dentro de "agregador/comercializadora") |
| AGG agregador/VPP | Agregador ✅ |
| GER gerador | (dentro de "gestor de GD") |
| DSO distribuidor | **ausente** |
| ORQ orquestrador/operador da plataforma | Admin (parcial) |

**✅ Confirmado pelo usuário:** **7 personas adotadas** (CON, INT, COM, AGG, GER, DSO, ORQ) — aplicadas em [01](../01-visao-e-prd.md), [08](../08-plataforma-cloud-e-apis.md) (RBAC) e [13](../13-gaps-riscos-e-decisoes.md) D4. Primárias no MVP: CON + INT; habilita os "bundles por persona".

## 5. Novos diferenciais estratégicos a registrar (dos estudos)

1. **Medidor-sensor como moat** — o hardware Smart **é** o medidor (não um controlador que depende de medidor externo). Já refletido na família Gateway+Meter ([06](../06-especificacao-hardware.md)); reforçar como vantagem competitiva em [01](../01-visao-e-prd.md).
2. **CCEE/BR como fosso** — integração de medição/contabilização/liquidação CCEE + rateio GD: build puro, sem incumbente estrangeiro. Elevar de "billing/rateio" ([08](../08-plataforma-cloud-e-apis.md)) a **diferencial central**.
3. **Agent-fabric AI-native** — runtime de agentes LLM por persona + copilot operacional + guardrails, como **camada incremental sobre serviços determinísticos** (nunca dependência crítica). **Novo** na suite → registrar como capacidade-fronteira (roadmap Fase 3).
4. **Janela competitiva** — abertura do Grupo B (2027–2028) é a janela; velocidade no MVP→VPP é mitigação. Coerente com [12 Roadmap](../12-roadmap-e-faseamento.md).

## 6. Ajustes técnicos concretos (do Discovery HEMS BR)

Aplicados às specs (✅) ou propostos (▫️):

| # | Achado | Ação | Onde |
|---|---|---|---|
| A1 | **REN ANEEL 1.098/2024**: zero-export ("grid zero") **dispensa** análise de inversão de fluxo (favorável) | ✅ adicionar | [02](../02-contexto-regulatorio-mercado-br.md) |
| A2 | **INMETRO Portaria 657/2025** (vig. 01/01/2026): Declaração de Conformidade do fornecedor substitui verificação inicial — favorece **medidor OEM** | ✅ adicionar | [02](../02-contexto-regulatorio-mercado-br.md), [06](../06-especificacao-hardware.md) |
| A3 | **Medidores OEM** candidatos: Eastron SDM630 (classe 0.5S)/SDM120, Acrel ADL200/ADL400 (~R$100, Modbus RTU, split-phase BR) | ✅ adicionar | [06 Smart Meter](../06-especificacao-hardware.md) |
| A4 | **SoC dois domínios** (Linux Cortex-A + MCU Cortex-M safety): NXP i.MX, **TI Sitara AM62x**, **ST STM32MP2** | ✅ ampliar | [06](../06-especificacao-hardware.md), [07](../07-especificacao-firmware-edge.md) |
| A5 | **4G**: módulo **Quectel EG915U-LA** (LTE Cat 1, variante LatAm, ANATEL) | ✅ adicionar | [06](../06-especificacao-hardware.md) |
| A6 | **Loop de safety zero-export 100% no edge**, independente de RTT à nuvem | ✅ reforçar | [07](../07-especificacao-firmware-edge.md) |
| A7 | **Telemetria:** Amazon Timestream **LiveAnalytics fechou p/ novos clientes (20/06/2025)** → usar **Timestream for InfluxDB** ou **TimescaleDB** | ✅ nota | [08](../08-plataforma-cloud-e-apis.md) |
| A8 | **AWS IoT**: Fleet Provisioning by claim/trusted-user, X.509/device, Greengrass stream manager (store-and-forward) | ▫️ opção de implantação | [03](../03-arquitetura-de-sistema.md)/[08](../08-plataforma-cloud-e-apis.md) |
| A9 | **GoodWe Open-API = 3 tipos**: OpenAPI (business, HTTPS, ~3600 req/h), Real-time Data (raw/Kafka), **Batch Remote Control (Kafka) → VPP/microgrid**. Doc oficial: openapi.goodwe.com (1º conector) | ✅ detalhar | [05](../05-integracao-e-conectividade.md), repo `energy-connectors` |
| A10 | **Tarifa Branca**: ponta ~18–21h; intermediário 1h antes/depois; sem mercado spot residencial | ✅ precisar | [02](../02-contexto-regulatorio-mercado-br.md) |
| A11 | **Troca nacional de medidores BT até 2035** (Portaria Normativa 126/2026, 2%/ano) — habilitador de dados | ✅ adicionar | [02](../02-contexto-regulatorio-mercado-br.md) |
| A12 | **BESS**: 269 MWh novos em 2024 (685 MWh acum.), leilão dedicado 2025 | ▫️ contexto de mercado | [02](../02-contexto-regulatorio-mercado-br.md)/[01](../01-visao-e-prd.md) |
| A13 | **SCEE**: créditos expiram em **60 meses** (REN 1.059/2023, Art. 655-L) | ✅ confirmar | [02](../02-contexto-regulatorio-mercado-br.md)/[04](../04-modelo-de-dominio-e-dados.md) |
| A14 | **Padrões**: SunSpec (local), IEEE 2030.5/CSIP (DER-utility), OpenADR (DR), IEEE 1547 — "VPP-ready" sem implementar agora | ✅ já previsto | [05](../05-integracao-e-conectividade.md) |

> Itens ✅ aplicados nas specs (ver commits subsequentes). Itens ▫️ ficam como opções/contexto. Tudo sensível a tempo permanece `[VERIFICAR]`.

## 7. Caveats herdados (do Discovery)
- VPP/agregador residencial BT: **sem marco regulatório** — monetização prospectiva (coerente com nossa ressalva N5).
- GoodWe Open-API: doc oficial parcialmente restrita — validar campos reais (projeto externo / repo `energy-connectors`).
- Métricas de otimização e cifras de mercado: citar fonte primária/data antes de usar como fato.
