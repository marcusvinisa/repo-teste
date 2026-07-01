# HEMS CORRENTE — Arquitetura de Referência (North Star)

> **Status:** Draft v0.1 · **Data:** 2026-06-26 · **Autor:** Marcus (CPTO) · **Escopo:** Projeto CORRENTE
> **Premissa-âncora de produto:** clonar/reimplementar do zero o equivalente funcional do **GoodWe EzManager3000** — hardware de borda + firmware + cloud + app — como produto próprio do CORRENTE, substituindo o gateway e a stack SEMS da GoodWe.
> **Designação de produto:** este documento usa designações **técnicas e provisórias** (ex.: *Gateway de Borda*). Naming comercial é **decision-gate** (marca/entidade) e não está cunhado aqui.

Documento de amarração. Define as quatro camadas, os **contratos de fronteira** entre elas e as decisões transversais. Os documentos `01`–`04` aprofundam cada camada e **devem** obedecer aos contratos abaixo.

---

## 1 · Premissa estratégica e leitura contrária (obrigatório — bear case)

Clonar hardware certificado é a aposta mais cara da plataforma. A leitura contrária precisa estar à vista antes de qualquer linha de código:

- **[F]** O EzManager3000 já é produto comercial **certificado** (CE-RED / EN18031, RCM) — *Fonte: datasheet GoodWe, seção Certification.* Recriar paridade exige nova certificação (no BR: **ANATEL** p/ rádio + **INMETRO** quando aplicável), com custo e prazo de meses.
- **[H]** Custo de prateleira de um gateway equivalente ≈ US$ 50–100/unid. — *validar com cotação real GoodWe/SOFAR/Deye antes de fechar BOM-alvo.*
- **Pre-mortem (2028, o clone morreu):** gastamos 12–18 meses e o NRE de HW+FW+certificação para chegar a **paridade** com um produto commodity, enquanto o moat real do CORRENTE — camada de dados/orquestração/AI e encaixe regulatório BR — ficou subinvestido. O hardware virou âncora de custo, não de diferenciação.

**O outro lado (por que clonar pode ser racional):** controle total da stack (sem refém de roadmap/cloud de fabricante), **dado proprietário** como moat, hardware desenhado para o BR (split-phase 127/254 V, ANEEL, sem o RCR alemão que é morto aqui), e unit economics de hardware próprio em escala — fila que você já modelou de **200 → 20.000 unid./mês [F, memória do projeto]**. O gateway deixa de ser custo e vira **canal de aquisição de dados** que alimenta a plataforma. A decisão de clonar é uma aposta de **verticalização**, não um erro de categoria — desde que o cronograma de certificação e o NRE entrem no caso-base, não no otimista.

---

## 2 · Visão de sistema (diagrama de componentes)

```
        CAMPO (residência / C&I)                      NUVEM (multi-tenant)                 USUÁRIOS
 ┌─────────────────────────────────┐        ┌──────────────────────────────────┐   ┌──────────────────┐
 │  Inversores (GoodWe/SOFAR/Deye) │        │  Ingestão  MQTT/TLS (mTLS X.509)  │   │  App mobile      │
 │  Medidor + CT  ── RS485 ───────►│        │     │                            │   │  (iOS/Android)   │
 │  EV charger / Bomba de calor    │        │     ▼                            │   │  Web (operador / │
 │  Plugs inteligentes (WiFi/LAN)  │        │  TSDB telemetria + Postgres meta │◄─►│   instalador /   │
 │            │                    │        │     │                            │   │   aggregator)    │
 │   ┌────────▼─────────┐          │  MQTT  │     ▼                            │   └────────┬─────────┘
 │   │ GATEWAY DE BORDA │──────────┼───────►│  Otimização + Forecast (AI)      │            │ REST/WS
 │   │  (HW+FW próprio) │  TLS     │  cmds  │  Motor de tarifa  ·  Open-API    │◄───────────┘
 │   └────────┬─────────┘◄─────────┼────────│  RBAC multi-tenant  ·  OTA mgr   │
 │     safety │ DO/relé, DI, AI    │        └──────────────────────────────────┘
 │     loop autônomo (zero-export, │              ▲ Fleet provisioning by claim
 │     one-touch shutdown)         │              │ (X.509 por device)
 │            │ BLE (comissionamento local) ◄─────┼──────────────  App (provisioning)
 └─────────────────────────────────┘
```

**Princípio de autonomia de borda:** se a nuvem cair, o Gateway de Borda mantém **modo seguro autônomo** (autoconsumo + zero-export) sem supervisão. Nuvem otimiza; **a borda nunca depende da nuvem para ser segura.**

---

## 3 · Contratos de fronteira (a cola entre os 4 documentos)

| Fronteira | Protocolo / contrato | Dono do contrato | Detalhado em |
|---|---|---|---|
| **Borda ↔ Dispositivos** | Modbus-RTU (RS485, 4 barramentos) + Modbus-TCP (LAN/WiFi). Driver model: 1 mapa de registradores por modelo de inversor/medidor. | FW (`02`) | `02`, `01` |
| **Borda ↔ Nuvem (telemetria)** | **MQTT sobre TLS 1.3, mTLS X.509 por device.** Envelope versionado (`schema_version`, `device_id`, `ts`, `payload`). Store-and-forward offline com fila persistente. | Nuvem (`03`) define schema; FW (`02`) implementa | `02`, `03` |
| **Borda ↔ Nuvem (comando)** | Comando **assinado** pela nuvem; envelope validado na borda contra *safety envelope* antes de virar Modbus write. Comando inválido = rejeitado + logado (mitiga *blind relay attack*). | Nuvem assina; FW valida | `02`, `03` |
| **Nuvem ↔ App/Web** | REST (CRUD/config) + WebSocket (tempo real). | Nuvem (`03`) | `03`, `04` |
| **Nuvem ↔ Terceiros** | **Open-API**: raw data · processed data · batch control (paridade com a Open-API GoodWe do white paper). | Nuvem (`03`) | `03` |
| **App ↔ Borda (local)** | **BLE GATT** para comissionamento/provisioning seguro + fallback WiFi-AP local. **Sem senha default fixa** (vide §4). | FW (`02`) + App (`04`) | `02`, `04` |

**Envelope canônico (telemetria) — referência para `02` e `03`:**
```json
{ "schema_version": "1.0", "device_id": "...", "ts": "RFC3339",
  "kind": "telemetry|event|cmd_ack", "seq": 0,
  "payload": { "...": "..." }, "sig": "opcional p/ cmd" }
```

---

## 4 · Decisões transversais (valem para as 4 camadas)

- **Identidade por device [F-decisão]:** **X.509 único por unidade** + **AWS IoT Fleet Provisioning by claim** (ou equivalente). Proíbe certificado de frota compartilhado — corrige o achado de *shared fleet cert* já mapeado no smartmeter.
- **Validação de comando [F-decisão]:** todo write Modbus originado na nuvem é validado na borda (faixa, dispositivo-alvo, assinatura). Corrige *uninvalidated Modbus write = blind relay path*.
- **Provisioning [F-decisão]:** **nada de senha default global** tipo `1234` (anti-padrão do SEMS+/EzManager). Credencial por device + bootstrap via BLE com PoP (proof-of-possession).
- **OTA [F-decisão]:** A/B com rollback automático + assinatura de imagem. USB (pendrive, FAT32) como canal de recuperação offline — paridade com o EzManager.
- **Modo seguro de borda:** autoconsumo + zero-export sustentados localmente sem nuvem.
- **Observabilidade:** todo device reporta heartbeat + estado de saúde; toda integração tem monitor.

---

## 5 · Mapa de paridade vs EzManager3000 + deltas Brasil

| Capacidade EzManager3000 | Manter no clone? | Delta BR |
|---|---|---|
| 4× RS485 / Modbus-RTU, 1× LAN / Modbus-TCP, WiFi, BLE 5.2 | **Sim** | — |
| Gestão: 1 híbrido, 1 grid-tied, 2 EV, 1 bomba SG-Ready, 12 plugs *(Fonte: datasheet)* | **Sim** (rever limites por demanda) | — |
| Controle SG-Ready (DO+12 V), one-touch shutdown (AI+12 V) | **Sim** | — |
| **RCR / Ripple Control Receiver (§14a EnWG, Alemanha)** | **Não** no caso-base | Substituir por **zero-export ANEEL RN 1000/2021** + telecomando do controle de injeção |
| Tarifa dinâmica / negativa, trading auto, AI scheduling/forecast | **Sim, na nuvem** | Ajustar ao **SCEE** (compensação) — não há spot residencial BR como na UE; tarifa dinâmica é **opcionalidade**, não caso-base |
| Cloud SEMS + SEMS+ App | **Reimplementar** (cloud CORRENTE + app próprio) | Multi-tenant p/ gerador/distribuidor/agregador/instalador/consumidor |
| Certificação CE-RED / EN18031, RCM | **Reequivaler** | **ANATEL** (rádio) + **INMETRO** (quando aplicável) |
| Split-phase / grid code | implícito EU | **127/254 V split-phase** (São Paulo/Enel) como cidadão de 1ª classe |

---

## 6 · Decision-gates ainda abertos (não cruzar sem brief)

1. **SoC do Gateway** — Linux SoC único vs. dois processadores (Linux + MCU safety) vs. ESP32 (protótipo). Recomendação em `01` §5. → **gate técnico-financeiro (BOM/NRE).**
2. **Naming comercial** do produto/linha. → **gate de marca.**
3. **Estratégia de certificação** (próprio vs. casa de teste) e cronograma. → **gate de capital/prazo.**
4. **Build vs. compra do broker MQTT** (AWS IoT Core vs. EMQX self-hosted). → `03` §5.

---

## Apêndice · Premissas

| # | Afirmação | Rótulo | Fonte / método |
|---|---|---|---|
| A1 | EzManager: 4×RS485, 1×LAN, WiFi b/g/n, BT5.2, 4×DI/2×DO/1×AI/1×CAN, USB2.0, ≤7 W, IP20, -30~+60 °C | **[F]** | Datasheet + Manual GoodWe (seções Comunicação/Técnico) |
| A2 | EzManager gerencia até 1 híbrido + 1 grid-tied + 2 EV + 1 bomba SG-Ready + 12 plugs | **[F]** | Datasheet, Device Management |
| A3 | Otimização AI/forecast roda na **nuvem**, não no edge (edge executa schedule) | **[E]** | Manual: "AI mode takes effect 24h after enabling", "data transmission time lag" ⇒ inferência cloud-side |
| A4 | Custo de prateleira de gateway equivalente US$ 50–100 | **[H]** | Validar com cotação GoodWe/SOFAR/Deye |
| A5 | RCR alemão é dispensável no BR; substituído por zero-export ANEEL | **[E]** | RN 1000/2021 + ausência de equivalente §14a no BR |
| A6 | Demanda-alvo de fleet 200 → 20.000 unid./mês | **[F]** | Modelagem prévia do projeto (memória) |
