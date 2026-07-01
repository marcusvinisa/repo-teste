# 01 · Engenharia de HARDWARE — Gateway de Borda HEMS CORRENTE

> **Status:** Draft v0.1 · **2026-06-26** · Camada: Edge/HW · Obedece aos contratos de `00-ARQUITETURA`.
> **Objeto:** placa + gabinete que substitui fisicamente o GoodWe EzManager3000. Alvo: trilho DIN / parede / mesa, IP20, indoor.

## 1 · Objetivo e escopo

**Dentro:** placa controladora, subsistema de I/O (RS485/DI/DO/AI/CAN), alimentação, conectividade (Ethernet/WiFi/BLE), gabinete DIN, BOM-alvo, plano de bring-up.
**Fora:** medidor/CT externo (comprado), inversores, certificação (cronograma vive em `00` §6.3).

## 2 · Requisitos

### Funcionais (paridade EzManager3000 — todos [F], fonte datasheet/manual GoodWe)
- 4× **RS485** isolado (Modbus-RTU) p/ inversores, medidores; 1× **Ethernet 10/100** (Modbus-TCP + nuvem); **WiFi 802.11 b/g/n**; **BLE 5.2**.
- 4× **DI** (entrada 0–12 V, 8–12 V = nível alto; opto-isolada), 2× **DO** (relé dry contact, **30 V DC @ 1 A**), 1× **AI** (0–12 V), 1× **CAN** (reservado/popular sob demanda).
- **12 V OUT @ 100 mA** (driver de relé externo / one-touch shutdown); **USB 2.0 host** (OTA por pendrive FAT32); **4× LED** de status.

### Não-funcionais
| Parâmetro | Alvo | Origem |
|---|---|---|
| Alimentação | Adaptador 100–240 VAC → **12 V DC**; entrada 12 V DC na placa | [F] datasheet |
| Consumo | **≤ 7 W** | [F] datasheet |
| Temp. operação / armazen. | **-30 ~ +60 °C** / -40 ~ +70 °C | [F] datasheet |
| Umidade / altitude / IP | 0–95 % não-cond. / 3000 m / **IP20** | [F] datasheet |
| Dimensões-alvo | ~99 × 85,6 × 71 mm (4–5 módulos DIN) | [F] datasheet |
| EMC/rádio | **CE-RED equiv. → ANATEL** (BR); EMC classe residencial | [E] vide `00` §5 |
| MTBF-alvo | ≥ 100.000 h @ 40 °C | [H] validar em DVT |

## 3 · Especificação técnica

### 3.1 Topologia de processamento (decisão central — vide §5)
**Recomendado (v1): dois processadores.**
- **AP (Application Processor):** SoC **Linux** classe i.MX 6ULL / Allwinner T113-S3 / Rockchip RK3308 — conectividade, nuvem (mTLS), OTA A/B, orquestração, drivers Modbus, fila persistente.
- **MCU de safety:** Cortex-M (STM32G0/G4) ou **RP2040** — laço hard-real-time: **zero-export, one-touch shutdown, watchdog dos relés, debounce de DI**. Roda independente do AP. Link AP↔MCU por UART/SPI com heartbeat.

> Racional: misturar safety crítico com um Linux não-determinístico é risco. O MCU garante que DO/relé e corte de injeção têm comportamento determinístico mesmo com o AP travado/atualizando.

### 3.2 Mapa de I/O (espelha o conector do EzManager — base p/ `02`)
| Bloco | Sinais | Spec elétrica | Isolação |
|---|---|---|---|
| RS485 ×4 | A1/B1 … A4/B4 | half-duplex, terminação comutável, proteção TVS/surge | **galvânica** por barramento |
| CAN ×1 | CAN_H/CAN_L | reservado | galvânica |
| DO ×2 | NC/COM/NO | relé **30 V DC @ 1 A** dry contact | relé = isolação natural |
| AI ×1 | AI_IN+/AI_GND | 0–12 V, ADC | divisor + clamp |
| 12 V OUT | +/− | **9,5–13,2 V @ 100 mA** | fusível resetável |
| DI ×4 | DI_1…DI_4 (+RG/0, CL/0, GND) | 0–12 V, alto 8–12 V | opto |
| USB | host A | USB 2.0, FAT32 OTA | ESD |
| ETH | RJ45 | 10/100, magnetics isolados | — |

### 3.3 Alimentação
12 V DC in → buck multi-rail (3V3/1V8/core do SoC). Supervisor de brownout dispara modo seguro no MCU. Reservar headroom: pico de 4× RS485 + Ethernet + relés ainda **≤ 7 W**.

### 3.4 Delta Brasil (hardware)
- Front-end de medição preparado para **split-phase 127/254 V** (entrada de CT externa, como no diagrama GoodWe).
- Não popular RCR alemão; reaproveitar bloco DI para **telecomando ANEEL / corte de injeção**.

## 4 · Interfaces (contratos com outras camadas)
- **→ Dispositivos:** RS485/Modbus-RTU + Ethernet/Modbus-TCP (contrato em `00` §3; mapa por modelo em `02`).
- **→ FW (`02`):** o MCU expõe à AP um registro de I/O (estado DI, comando DO, leitura AI, status safety) via UART/SPI; pinout e protocolo interno definidos em `02`.
- **→ App (`04`):** rádio BLE 5.2 para comissionamento; antena externa opcional (paridade: EzManager tem porta ANT p/ ambiente metálico).

## 5 · Decisões e trade-offs (SoC)
| Opção | Prós | Contras | Veredicto |
|---|---|---|---|
| **ESP32-S3 único** | barato (~US$3 [H]), WiFi+BLE nativos, familiar | **sem EMAC** (Ethernet via SPI-PHY ruim), 4×RS485 forçam expansor, safety+conectividade no mesmo core | só **protótipo v0** |
| **ESP32 clássico** | tem **EMAC**, WiFi+BT | BLE 4.2, SoC antigo | protótipo v0 viável |
| **Linux SoC único** | Ethernet+UARTs+USB nativos, TLS/OTA/fila robustos, provável escolha do EzManager [E] | safety não-determinístico, BOM/consumo maiores | **base v1** |
| **Linux + MCU safety** *(recomendado)* | determinismo de safety + robustez de nuvem | mais NRE/BOM | **alvo v1** |

**[H] Recomendação:** protótipo de conceito no **ESP32 clássico** (valida Modbus×4 + nuvem rápido e barato) → **DVT em Linux+MCU**. Validar a hipótese com um spike de 1–2 semanas medindo throughput de 4 barramentos Modbus simultâneos + latência do laço de zero-export.

## 6 · Riscos técnicos
- **Isolação galvânica de 4 RS485** em IP20 compacto: risco de EMC e roteamento. Mitigação: DC-DC isolado por barramento, plano de terra particionado.
- **Dissipação ≤7 W** com SoC Linux + relés: validar térmico em -30~+60 °C (gabinete fechado). Mitigação: orçamento térmico no DVT.
- **Surge nas linhas RS485** de campo (raios, BR): TVS + clamp dimensionados; teste de surge na homologação.
- **Lead time de SoC** (alocação): segunda fonte desde o EVT.

## 7 · Definition of Done (HW — base no `engineering-process`, categoria HW/FW)
```
[ ] Esquemático + layout revisados por par (1 eng sênior HW)
[ ] BOM-alvo com 2ª fonte nos componentes críticos (SoC, RS485, relés)
[ ] Bring-up board: power rails, clocks, boot do AP, vida do MCU
[ ] 4× RS485 validados em bancada com inversor real (GoodWe/SOFAR/Deye)
[ ] DO/relé, DI, AI, 12V OUT validados contra spec (30V@1A, 8–12V, 9,5–13,2V)
[ ] Térmico medido nos extremos -30/+60 °C ⇒ ≤7 W confirmado
[ ] Pré-scan EMC (rádio + conduzido) antes de submeter ANATEL
[ ] Sem regressão de I/O documentada · revisão de DFM/DFT
```
