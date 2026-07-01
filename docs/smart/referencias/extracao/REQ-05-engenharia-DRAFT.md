> Extração fiel (subagente) do bloco. Fonte: docs/smart/referencias/produto/eos-deno-requisitos-produto-2026-06-30-CONF/. Preserva taxonomia [F]/[E]/[H]/[INPUT].

I now have complete context: the framing docs (README, STATE, _LEIA) and all five DRAFT engineering block files. I have everything needed to produce the faithful extraction. Here is the result.

---

# Extração FIEL — Bloco `05-engenharia-ref-DRAFT`

## 1 · Resumo do bloco

⚠ **AVISO DRAFT:** Todo este bloco é **Draft v0.1 (2026-06-26), marca "CORRENTE", ANTERIOR à recalibração de jun/2026** — **NÃO é requisito confirmado**. É **ponto de partida de engenharia**, não spec. A **premissa-âncora do DRAFT** é agressiva e hoje questionável: *clonar/reimplementar do zero o GoodWe EzManager3000* (HW de borda + FW + cloud + app), substituindo gateway + stack SEMS. O próprio doc traz o *bear case* (clonar HW certificado = aposta mais cara; risco de subinvestir no moat de dados/AI/regulatório). São 4 camadas amarradas por `00-ARQUITETURA` via **contratos de fronteira** (Modbus device-side; MQTT/mTLS telemetria; comando assinado+validado na borda; REST/WS para app; Open-API para terceiros; BLE para comissionamento). Princípio central sólido e reaproveitável: **autonomia de borda** (modo seguro autônomo — autoconsumo + zero-export — sem depender da nuvem) e correção de anti-padrões de segurança já mapeados (cert de frota compartilhado, blind Modbus relay, senha default `1234`). O DRAFT assume **HW+FW próprio desde já**, o que **conflita frontalmente** com o escopo v1 confirmado (integrador sobre smart-meter **existente**, device-abstraction desde a 1ª linha) e com a decisão de **fork OpenEMS / build-on ThingsBoard** (o DRAFT propõe cloud/EMS *from scratch*).

## 2 · Decisões / pontos de arquitetura

Legenda relevância: **V1** = pertinente ao v1 confirmado (integrador/smart-meter/abstração/ingestão) · **FASE-2+** = ODM próprio/VPP/otimização/edge safety · **CONTEXTO** = premissa de clone/paridade GoodWe, herança de decisão.

| ID | Item · `[DRAFT]` | Camada | Relevância | O que reconciliar | Fonte |
|---|---|---|---|---|---|
| ENG-01 | **Premissa-âncora: clonar EzManager3000** (HW+FW+cloud+app próprios, substituir SEMS) `[DRAFT]` | arquitetura | CONTEXTO | Contradiz v1 (integrador sobre smart-meter **existente**, sem ODM ainda). Rebaixar de "clone total" para "device-abstraction + ingestão"; clone vira FASE-2+ (moat ODM) | `00` §1, Premissa |
| ENG-02 | **Bear case / pre-mortem explícito** do clone (HW vira âncora de custo, moat real = dados/AI/regulatório) `[DRAFT]` | arquitetura | CONTEXTO | Já **alinhado** com a recalibração (moat = dado+DERMS+CCEE). Preservar como justificativa do sequenciamento v1-first | `00` §1 |
| ENG-03 | **4 camadas + contratos de fronteira** (borda↔device, borda↔nuvem tel/cmd, nuvem↔app, nuvem↔3os, app↔borda) `[DRAFT]` | arquitetura | V1 (parcial) | Manter contratos borda↔nuvem↔app; borda↔device passa a **abstração de device (S2.3)** genérica, não Modbus-GoodWe hard-coded | `00` §3 |
| ENG-04 | **Envelope canônico de telemetria** versionado (`schema_version`, `device_id`, `ts`, `kind`, `seq`, `payload`, `sig`) `[DRAFT]` | arquitetura/cloud | **V1** | Reusável quase direto; reconciliar com o schema do ThingsBoard/OpenEMS e com o modelo de ativo do v1 | `00` §3 |
| ENG-05 | **Autonomia de borda** = modo seguro autônomo (autoconsumo + zero-export) sem nuvem `[DRAFT]` | arquitetura/FW | FASE-2+ | Depende de HW/FW próprio (ODM). No v1 (smart-meter de terceiro) não há borda própria — é leitura/ingestão. Guardar p/ device ODM | `00` §2/§4, `02` §3.3 |
| ENG-06 | **Identidade X.509 única por device + Fleet Provisioning by claim** (fim do cert de frota compartilhado) `[DRAFT, F-decisão]` | cloud/FW | **V1** | Princípio confirmado ("já confirmado no smartmeter"). Reconciliar com o provisioning do ThingsBoard / IoT do v1 | `00` §4, `02` §3.4, `03` §3.2 |
| ENG-07 | **Command validator / safety envelope na borda** (todo write da nuvem validado: device-alvo, faixa, assinatura → fecha blind relay path) `[DRAFT, F-decisão]` | FW/cloud | FASE-2+ | Requer FW próprio; no v1 (monitoramento + diagnóstico, sem controle) é menos central. Auditoria imutável de comando é aproveitável já | `00` §4, `02` §3.4, `03` §3.3 |
| ENG-08 | **Provisioning sem senha default global** (`1234` proibido; BLE + PoP + rotação) `[DRAFT, F-decisão]` | FW/SW | V1 (princípio) | Vira política de segurança geral; parte BLE/comissionamento local é FASE-2+ (device próprio) | `00` §4, `02` §3.4, `04` §3.1 |
| ENG-09 | **OTA A/B + rollback + imagem assinada + canal USB FAT32** `[DRAFT, F-decisão]` | FW/cloud | FASE-2+ | Só faz sentido com FW próprio (ODM). OTA-manager de frota na nuvem pode antecipar parcialmente | `00` §4, `02` §3, `03` DoD |
| ENG-10 | **Dois processadores: Linux AP + MCU de safety** (Cortex-M/RP2040, laço hard-real-time) `[DRAFT, recomendado v1]` | HW/FW | FASE-2+ | Decisão de HW do ODM próprio — fora do v1. É candidato a ADR quando o ODM entrar | `00` §6.1, `01` §3.1/§5, `02` §3.1 |
| ENG-11 | **Ingestão MQTT/TLS → TSDB + Postgres (metadados)** `[DRAFT]` | cloud | **V1** | Núcleo do v1 (smart→ingestão→time-series→modelo de ativo). Reconciliar com ThingsBoard (já traz ingestão/telemetria) — evitar reconstruir | `03` §3.1/§3.4 |
| ENG-12 | **TSDB: Timescale** (vs Timestream) para telemetria `[DRAFT, H]` | cloud | **V1** | Decidir à luz do que ThingsBoard usa nativamente (Postgres/Cassandra/Timescale) — pode ser herdado, não escolhido do zero | `03` §3.4/§5 |
| ENG-13 | **Multi-tenant + RBAC + Row-Level Security no Postgres** (hierarquia Distribuidor→Revendedor→Instalador + operador/consumidor) `[DRAFT, F-decisão]` | cloud | **V1** | Multi-tenant é obrigatório na recalibração. Reconciliar RLS-próprio vs modelo multi-tenant nativo do ThingsBoard | `03` §3.5 |
| ENG-14 | **Otimização/Forecast AI cloud-side** (regras→MILP/heurística→ML; forecast habit-based) `[DRAFT, E]` | cloud | FASE-2+ | Fora do v1 (otimização é fase-2 = EMHASS/PyPSA). Placeholder estatístico. Reconciliar com EMHASS/PyPSA/OpenEMS | `00` A3, `02` §1, `03` §2/§5 |
| ENG-15 | **Motor de tarifa** (dinâmica/negativa, trading auto) `[DRAFT]` | cloud | CONTEXTO | Herança GoodWe/UE; DRAFT já marca "valor presente ~0 no BR, opcionalidade". Fora do caso-base v1 | `00` §5, `03` §2/§3.6 |
| ENG-16 | **Open-API p/ terceiros** (raw · processed · batch control; OAuth2 + rate-limit por tenant) `[DRAFT]` | cloud | FASE-2+ | Paridade GoodWe; útil como norte de plataforma, não é escopo do portal-integrador v1 | `00` §3, `03` §2/§4 |
| ENG-17 | **Driver model = 1 mapa de registradores por modelo, carregável por OTA (YAML)** `[DRAFT, F-decisão]` | FW/cloud | **V1 (conceito)** | É exatamente a **abstração de device (S2.3)**: catálogo versionado de drivers empurrado pela nuvem. Reconciliar com a S2.3 confirmada e com conectores do ThingsBoard | `02` §3.2, `03` §6 |
| ENG-18 | **Colisão de endereço Modbus default 247** como caso de teste obrigatório de provisioning `[DRAFT, F, evidência prática]` | FW | V1 (se integração Modbus) | Conhecimento real (mapeou GoodWe ES-LD / SDT-G3). Vira teste da camada de abstração se o smart-meter falar Modbus | `02` §3.2/§6 |
| ENG-19 | **Delta Brasil: split-phase 127/254 V + zero-export ANEEL RN 1000/2021** (substitui RCR §14a alemão) `[DRAFT, E]` | HW/FW/cloud/SW | V1 (regulatório) · FASE-2+ (HW) | Zero-export/SCEE como cidadão de 1ª classe é confirmado-BR; parte HW (front-end split-phase) é FASE-2+ | `00` §5, `01` §3.4, `02` §3.3, `03` §3.6, `04` §3.3 |
| ENG-20 | **SCEE / compensação** como motor econômico (não spot residencial) `[DRAFT, E]` | cloud/SW | V1 (contexto BR) | Alinhado ao mercado BR. CCEE/ACL é teto vazio (fase-2). Manter rótulos pt-BR de compensação | `03` §3.6, `04` §3.3 |
| ENG-21 | **App/Web thin-client transport-agnostic** (mesmo envelope p/ REST-WS-nuvem e BLE-borda; padrão FieldOps) `[DRAFT, H]` | SW | **V1 (web)** · FASE-2+ (BLE) | Portal do integrador (web) é o v1; adapter BLE/comissionamento local é FASE-2+ (device próprio). Reusar padrão de protocolo | `04` §3.1 |
| ENG-22 | **Um app com modos por RBAC** (vs apps por papel) + **SPA web separada** p/ operador/agregador `[DRAFT]` | SW | V1 (web SPA) | Portal do integrador = SPA. App mobile/consumidor mais tarde | `04` §5 |
| ENG-23 | **Comissionamento BLE offline** (instalador em telhado sem 4G) `[DRAFT, F-decisão]` | SW/FW | FASE-2+ | Exige device próprio + BLE; não aplicável ao smart-meter de terceiro no v1 | `04` §3.2/§5/§6 |
| ENG-24 | **i18n pt-BR primeiro** (en/es depois); mobile Android 7.0+/iOS 15.1+ `[DRAFT, E/F]` | SW | V1 | pt-BR confirmado. Alvos de versão mobile revisitar quando houver app | `04` §2 |
| ENG-25 | **Decision-gates abertos no DRAFT**: SoC do gateway; naming; estratégia de certificação; **build vs buy do broker MQTT (IoT Core vs EMQX)** `[DRAFT]` | arquitetura/cloud | V1 (broker/naming) · FASE-2+ (SoC/cert) | Naming resolvido (EOS-DENO). Broker: reavaliar dado ThingsBoard. SoC/certificação = ODM (fase-2) | `00` §6, `03` §5 |
| ENG-26 | **Fila store-and-forward offline** na borda (SQLite; ≥72 h buffer) `[DRAFT, E/H]` | FW | FASE-2+ | Depende de borda própria. No v1 a resiliência de ingestão é cloud-side / no coletor do smart-meter | `02` §2/§3.1/§5 |

## 3 · Stack técnico citado

| Camada | Tecnologia / OSS / infra | Papel no DRAFT | Rótulo | Fonte |
|---|---|---|---|---|
| HW · SoC AP | i.MX 6ULL / Allwinner T113-S3 / Rockchip RK3308 (Linux) | Application Processor do gateway | `[H]` recomendação | `01` §3.1/§5 |
| HW · MCU safety | STM32G0/G4 (Cortex-M) ou RP2040 | Laço hard-real-time (zero-export/shutdown) | `[H]` | `01` §3.1, `02` §3.1 |
| HW · protótipo | ESP32-S3 / ESP32 clássico | Spike v0 (Modbus×4 + nuvem) | `[H]` | `01` §5 |
| FW · AP | **Go** ou **Rust** | Agente de borda (Modbus pool, MQTT, OTA) — decidir por spike | `[H]` | `02` §3.1/§5 |
| FW · MCU | **Zephyr** (ou bare-metal) | RTOS do MCU de safety | `[H]` | `02` §3.1 |
| FW · build | **Yocto / Buildroot** | Distro Linux embarcado | `[H]` | `02` §3.1 |
| FW · fila | **SQLite** (vs append-only) | Store-and-forward offline | `[E]` v1 | `02` §5 |
| Protocolo device | **Modbus-RTU (RS485) + Modbus-TCP** | Aquisição inversor/medidor/plug | `[F]` paridade | `00` §3, `02` §3.2 |
| Protocolo tel. | **MQTT sobre TLS 1.3 + mTLS X.509** | Telemetria borda↔nuvem | `[F-decisão]` | `00` §3, `03` §3.1 |
| Broker MQTT | **AWS IoT Core** (v1) vs **EMQX** self-hosted | Ingestão de frota | decisão `[H]`/gate | `03` §5 |
| Provisioning | **AWS IoT Fleet Provisioning by claim** | Identidade por device | `[F-decisão]` | `00` §4, `03` §3.2 |
| Cloud · TSDB | **TimescaleDB** (vs AWS Timestream) | Telemetria séries temporais | `[H]` | `03` §3.4/§5 |
| Cloud · relacional | **PostgreSQL** + **Row-Level Security** | Metadados, tenants, RBAC, isolamento | `[F-decisão]` | `03` §3.4/§3.5 |
| Cloud · otimização | regras → **MILP/heurística** → ML | Otimizador de autoconsumo/tarifa | `[E]` faseado | `03` §5 |
| Cloud · API | **REST + WebSocket**; **Open-API + OAuth2** | App/Web e terceiros | `[F]` | `00` §3, `03` §4 |
| SW · mobile | **React Native** ou **Flutter** | App iOS+Android (decidir por BLE) | `[H]` | `04` §3.1/§5 |
| SW · web | **React + Tailwind** (design system v2) | Console/portal | `[H]` | `04` §3.1 |
| Segurança | Secure boot, imagem OTA assinada, PoP (proof-of-possession) | Hardening borda | `[F-decisão]` | `00` §4, `02` §3.4 |
| Tempo | NTP + RTC com bateria | Deriva de relógio p/ schedule | `[H]` | `02` §6 |

> Nota de reconciliação: o DRAFT **não menciona** OpenEMS, ThingsBoard, EMHASS nem PyPSA — que são as decisões de build **confirmadas** pós-recalibração. O stack acima é o desenho *from scratch* que deve ser confrontado com essas escolhas OSS (ver §5).

## 4 · Candidatos a ADR

Ordem = maior alavancagem no v1 primeiro.

1. **ADR-001 · Camada de abstração de device (S2.3 / driver-model)** — mapa de registradores por modelo, carregável/versionado, empurrado pela nuvem (ENG-17/18). É a **disciplina inegociável do v1**; decidir formato (YAML vs schema ThingsBoard), catálogo versionado e política de compatibilidade por firmware do device.
2. **ADR-002 · Fork OpenEMS (EMS/edge-logic)** — decisão confirmada, ausente do DRAFT; registrar o que se herda do OpenEMS vs o que o DRAFT propunha construir (agente de borda Go/Rust, scheduler local).
3. **ADR-003 · Build-on ThingsBoard (multi-tenant / IoT / ingestão)** — confirmado; reconcilia ENG-11/12/13 (ingestão MQTT, TSDB, multi-tenant/RBAC/RLS): o que ThingsBoard já entrega vs o que o DRAFT reprojetava do zero.
4. **ADR-004 · Ingestão & time-series (broker + TSDB)** — IoT Core vs EMQX vs broker do ThingsBoard; Timescale vs Timestream vs store nativo (ENG-04/11/12/25). Fecha o gate `00` §6.4 com custo/device em escala.
5. **ADR-005 · Modelo multi-tenant & isolamento (RLS vs nativo)** — hierarquia de papéis + isolamento por-linha vs o multi-tenant do ThingsBoard (ENG-13). Confirmado como obrigatório na recalibração.
6. **ADR-006 · Identidade & provisioning por device (X.509 + Fleet Provisioning)** — princípio confirmado no smartmeter; formalizar contra anti-padrão do cert de frota compartilhado (ENG-06/08).
7. **ADR-007 · Edge vs Cloud (fronteira de safety/otimização)** — otimização/forecast cloud-side; safety autônomo na borda (ENG-05/07/14). Relevante quando o **ODM próprio** entrar (fase-2); registrar já a fronteira.
8. **ADR-008 · Arquitetura de HW do gateway ODM (Linux AP + MCU safety)** — FASE-2+; decisão de dois-processadores + BOM/NRE + certificação ANATEL/INMETRO (ENG-10, gates `00` §6).
9. **ADR-009 · Framework do cliente (RN vs Flutter; web SPA)** — decidir por caminho crítico (BLE quando houver device); web SPA para o portal do integrador no v1 (ENG-21/22).

## 5 · Conflitos com a recalibração / escopo v1

| # | O que o DRAFT afirma | O que foi confirmado depois | Resolução sugerida |
|---|---|---|---|
| C1 | **Clonar o EzManager3000** — HW+FW+cloud+app próprios desde já (ENG-01) | v1 = **integrador sobre smart-meter EXISTENTE**; ODM próprio é fase posterior/moat | Rebaixar clone total para FASE-2+; v1 entrega ingestão + abstração + portal sobre device de terceiro |
| C2 | **Cloud/EMS reimplementados do zero** (agente Go/Rust, ingestão própria, otimizador próprio) | **Fork OpenEMS + build-on ThingsBoard**; EMHASS/PyPSA na fase-2 | Não reconstruir; mapear cada componente do DRAFT para o que o OSS já entrega (ADR-002/003) |
| C3 | **Marca "CORRENTE"** em todos os 5 docs + designações "Gateway de Borda" | Marca **EOS-DENO** (naming resolvido; gate de marca fechado no STATE) | Renomear em massa CORRENTE→EOS-DENO ao promover a spec |
| C4 | **Borda própria + FW/MCU + BLE/OTA/safety autônomo** como núcleo (ENG-05/07/09/10/23/26) | v1 **sem borda própria** — smart-meter de terceiro; foco monitoramento/frota/comissionamento/**diagnóstico remoto** | Tratar todo o edge-safety/FW como FASE-2+ (device ODM); manter só o que é cloud-side/leitura no v1 |
| C5 | **Otimização, motor de tarifa, Open-API, VPP/agregador** presentes na arquitetura (ENG-14/15/16, `04` §3.2 VPP) | **Fora do v1 deliberado**: VPP, CCEE, agent-fabric, otimização, mercado livre, 18 cenários | Marcar explicitamente FASE-2+; não construir P&L nem UI sobre isso no v1 |
| C6 | **Ausência total de agent-fabric / AI-native (LLM)** — DRAFT trata "AI" só como forecast/scheduling estatístico herdado da GoodWe | Um dos **2 tetos vazios** = agent-fabric AI-native (LLM), onde o EOS-DENO nasce à frente | DRAFT subespecifica o diferencial estratégico; a arquitetura AI-native precisa ser desenhada nova (fora do DRAFT), fase-2 |
| C7 | **CCEE/mercado livre ausente**; foco em SCEE/compensação + tarifa dinâmica (opcionalidade) | Outro teto vazio = **CCEE/BR**; empresa-âncora adquire comercializadora | SCEE no v1 está correto; CCEE/ACL é moat de fase-2, não no DRAFT |
| C8 | Multi-tenant tratado como **feature de cloud** (RLS no Postgres) (ENG-13) | Multi-tenant é **obrigatório/estrutural** na recalibração | Elevar a decisão estrutural; reconciliar com multi-tenant nativo do ThingsBoard (ADR-005) |

**Pontos do DRAFT já alinhados (preservar):** bear-case do clone (ENG-02), device-abstraction/driver-model (ENG-17) que antecipa a S2.3, identidade X.509 por device (ENG-06), correção dos anti-padrões de segurança (cert de frota / blind relay / senha `1234`), envelope canônico versionado (ENG-04), foco BR (split-phase/zero-export/SCEE, pt-BR) e ingestão→time-series→modelo de ativo (ENG-11) — que é literalmente o fluxo do v1.

**Arquivos-fonte (todos absolutos):**
- `/home/marcus/lab/sandbox/repo-teste/docs/smart/referencias/produto/eos-deno-requisitos-produto-2026-06-30-CONF/05-engenharia-ref-DRAFT/00-ARQUITETURA-HEMS-CORRENTE.md`
- `/home/marcus/lab/sandbox/repo-teste/docs/smart/referencias/produto/eos-deno-requisitos-produto-2026-06-30-CONF/05-engenharia-ref-DRAFT/01-ENG-HARDWARE.md`
- `/home/marcus/lab/sandbox/repo-teste/docs/smart/referencias/produto/eos-deno-requisitos-produto-2026-06-30-CONF/05-engenharia-ref-DRAFT/02-ENG-FIRMWARE.md`
- `/home/marcus/lab/sandbox/repo-teste/docs/smart/referencias/produto/eos-deno-requisitos-produto-2026-06-30-CONF/05-engenharia-ref-DRAFT/03-ENG-CLOUD.md`
- `/home/marcus/lab/sandbox/repo-teste/docs/smart/referencias/produto/eos-deno-requisitos-produto-2026-06-30-CONF/05-engenharia-ref-DRAFT/04-ENG-SOFTWARE.md`
- Framing: `_LEIA.md`, `README-CLAUDE-CODE.md`, `00-fundacao/04-MEMORIA-E-APRENDIZADO.md` (STATE) na mesma árvore `...-CONF/`.
