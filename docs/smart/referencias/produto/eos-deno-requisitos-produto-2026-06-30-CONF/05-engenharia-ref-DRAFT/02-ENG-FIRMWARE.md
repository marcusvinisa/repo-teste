# 02 · Engenharia de FIRMWARE — Gateway de Borda HEMS CORRENTE

> **Status:** Draft v0.1 · **2026-06-26** · Camada: Edge/FW · Obedece aos contratos de `00-ARQUITETURA`.
> **Objeto:** firmware do gateway que substitui o EzManager3000 — aquisição, controle de cargas, safety, execução de setpoints da nuvem, conectividade.

## 1 · Objetivo e escopo

**Dentro:** stack do AP (Linux) + firmware do MCU de safety, drivers de dispositivo, agente de nuvem, OTA, provisioning, laço de safety.
**Fora:** otimização/forecast (vive na nuvem, `03`); hardware (`01`).

> **Divisão de responsabilidade [E]:** a inteligência (otimização de tarifa, forecast, scheduling) é **cloud-side** — o manual GoodWe indica latência de ativação de AI mode (24 h) compatível com inferência na nuvem. O FW é **gateway de protocolo + executor de schedule + controlador de safety**, não caixa de IA.

## 2 · Requisitos

### Funcionais (paridade EzManager — [F], fonte manual GoodWe)
- **Modbus-RTU master** nos 4 barramentos RS485 + **Modbus-TCP** (LAN/WiFi) p/ inversores/medidores/plugs.
- Controle **SG-Ready** via DO+12 V (modos: economia / reforço de reserva — manual §DO); **one-touch shutdown** via AI+12 V; **anti-backfeed / zero-export**.
- Modos de estação: **autoconsumo**, controle de potência injetada, **modo AI** (executa schedule recebido da nuvem).
- **OTA**: nuvem (A/B) + **USB pendrive FAT32** (pasta `collector`) como recuperação — paridade EzManager.
- **Provisioning** local por **BLE** (substitui SEMS+/Bluetooth) + WiFi-AP fallback.
- **Telemetria** store-and-forward (opera offline e sincroniza).

### Não-funcionais
| Parâmetro | Alvo | Origem |
|---|---|---|
| Latência laço de safety (zero-export, shutdown) | **≤ 200 ms** loop no MCU | [H] validar |
| Poll Modbus / device | 1–5 s configurável; 4 barramentos concorrentes | [E] |
| Buffer offline | ≥ 72 h de telemetria em fila persistente | [H] |
| Boot até modo seguro | ≤ 10 s (MCU assume antes do AP subir) | [H] |
| Atualização sem perder safety | OTA do AP **não** derruba o MCU | [F-decisão] `00` §4 |

## 3 · Especificação técnica

### 3.1 Arquitetura de software (AP — Linux)
```
┌───────────────────────────────────────────────┐
│  Agente CORRENTE (Go ou Rust)                   │
│  ├─ Modbus master pool (4×RTU + TCP)            │  → drivers por modelo
│  ├─ Device drivers (GoodWe/SOFAR/Deye/ Shelly) │
│  ├─ Telemetry pipeline → fila persistente      │  (SQLite/embedded queue)
│  ├─ MQTT client (TLS1.3, mTLS X.509)           │  ↔ nuvem (00 §3)
│  ├─ Command validator (safety envelope)        │  ↕ MCU
│  ├─ Local scheduler (executa plano da nuvem)   │
│  ├─ BLE/WiFi provisioning (PoP, sem 1234)      │
│  └─ OTA agent (A/B + assinatura + rollback)    │
└───────────────────────────────────────────────┘
            ▲ UART/SPI + heartbeat
┌───────────────────────────────────────────────┐
│  MCU de safety (Zephyr / bare-metal)            │
│  ├─ Zero-export control loop (autônomo)        │
│  ├─ One-touch shutdown (AI+12V)                │
│  ├─ DO/relé driver + interlock + watchdog      │
│  └─ DI debounce (telecomando/RCR-BR)           │
└───────────────────────────────────────────────┘
```
**Stacks [H]:** AP em **Go** (concorrência natural p/ N barramentos + MQTT) ou **Rust** (segurança de memória); distro via **Yocto/Buildroot**. MCU em **Zephyr** (alinha à sua skill `embedded-firmware`). Validar Go vs Rust por footprint/equipe num spike.

### 3.2 Driver model (contrato com `01` e dispositivos)
Um **mapa de registradores por modelo** (YAML/struct), carregável por OTA sem reflash:
```yaml
device: goodwe_et_g2          # ex.: ET15-30kW, ES G2, SOFAR HYD, Deye
transport: rtu                # rtu | tcp
unit_id: 247                  # ⚠ default 247 → resolver colisão de endereço
registers:
  pv_power:   { addr: 0x..., type: u32, scale: 1, unit: W }
  soc:        { addr: 0x..., type: u16, scale: 0.1, unit: % }
  export_w:   { addr: 0x..., type: s32, scale: 1, unit: W }
writes:
  export_limit: { addr: 0x..., type: u16, range: [0, 100], unit: % }
```
> Você já mapeou na prática os Modbus maps **GoodWe ES-LD / SDT-G3** e a **colisão de endereço default 247** — entra como caso de teste obrigatório do provisioning.

### 3.3 Laço de safety (MCU, autônomo)
- Lê potência injetada (medidor/CT) → se injeção > limite ANEEL configurado, atua **redução de injeção** no inversor (Modbus write via AP **ou** via interlock direto) dentro do envelope.
- **Fail-safe:** perda de heartbeat do AP por *N* ciclos ⇒ MCU mantém último estado seguro (autoconsumo + zero-export) e sinaliza LED.
- One-touch shutdown e DO/relé têm prioridade sobre comando de nuvem.

### 3.4 Segurança (corrige anti-padrões já identificados)
- **Identidade:** X.509 por device + Fleet Provisioning by claim (`00` §4) — **fim do cert de frota compartilhado.**
- **Comando:** todo write originado na nuvem passa pelo **command validator** (device-alvo correto, faixa do registrador, assinatura) antes de virar Modbus — **fecha o blind relay path.**
- **Provisioning:** **sem senha default global** (`1234` do SEMS+ é proibido); bootstrap BLE com proof-of-possession + rotação de credencial.
- **Secure boot** no AP + **imagem OTA assinada** + rollback automático em falha de health-check pós-update.

## 4 · Interfaces
- **↔ Dispositivos:** Modbus-RTU/TCP por driver model (§3.2).
- **↔ Nuvem (`03`):** MQTT/TLS, envelope canônico de `00` §3; comandos assinados; ACK de comando (`kind: cmd_ack`).
- **↔ MCU (`01`):** protocolo interno UART/SPI (registro de I/O + heartbeat).
- **↔ App (`04`):** GATT BLE de comissionamento (perfis: status, set credencial, set rede, set planta).

## 5 · Decisões e trade-offs
- **Go vs Rust no AP [H]:** Go entrega mais rápido com sua equipe; Rust reduz classe inteira de bugs de memória no agente que fala com a rede. → spike comparativo.
- **Safety no MCU vs no AP [F-decisão]:** no **MCU** — não negociável; Linux não dá garantia hard-real-time.
- **Fila offline: SQLite vs fila append-only [E]:** SQLite simplifica consulta/retenção; append-only é mais leve. → SQLite no v1.
- **Modbus map estático vs carregável [F-decisão]:** **carregável por OTA** — adicionar inversor sem reflash é requisito de plataforma.

## 6 · Riscos técnicos
- **Colisão de endereço Modbus 247** em multi-inversor: descoberta + reendereçamento no provisioning (caso de teste).
- **Surpresa de mapa por firmware do inversor** (GoodWe muda registrador entre versões): driver versionado + tabela de compatibilidade.
- **OTA derrubando o gateway** em campo: A/B + rollback + canal USB de recuperação obrigatórios antes do 1º piloto.
- **Deriva de relógio** afetando schedule de tarifa: NTP + RTC com bateria.

## 7 · Definition of Done (FW — `engineering-process`, HW/FW)
```
[ ] Spec de FW + protocolo interno AP↔MCU documentados
[ ] Revisão por par (1 eng sênior FW)
[ ] Modbus master testado com inversor real nos 4 barramentos (bancada)
[ ] Driver model validado p/ ≥2 famílias (GoodWe + SOFAR/Deye)
[ ] Laço de safety testado: perda de nuvem ⇒ modo seguro autônomo
[ ] OTA A/B + rollback testado (incl. recuperação por USB FAT32)
[ ] Provisioning BLE testado SEM senha default; cert por device emitido
[ ] Command validator rejeita write fora de faixa/assinatura (teste negativo)
[ ] Sem regressão documentada · merged com PR revisado
```
