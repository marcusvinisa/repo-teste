# Integração — Mapa Canônico de Capacidades

> **Superset** de todas as capacidades conhecidas (até jun/2026) de **sistemas de geração e armazenamento** — e dos demais ativos da casa — expressas de forma **agnóstica de marca**. É a lista-mestre de `ids` que os [mapas por fabricante](00-modelo-de-abstracao.md) referenciam, **estejam ou não preenchidos** para cada marca. Complementa o modelo de dados de [04](../04-modelo-de-dominio-e-dados.md) com o detalhe de **controle/config**, não só telemetria.

**Convenções:** unidades SI; sinal **+ importa/consome/carrega**, **− exporta/gera/descarrega** (visão da UC); acesso `R`/`W`/`RW`; tipo `T`=telemetria, `S`=setpoint, `M`=modo, `C`=config/comissionamento. `[VERIFICAR]` = suporte varia por modelo/fabricante.

---

## 1. Inversor PV / Híbrido (`asset = inverter`)

### 1.1 Telemetria (T, R)
| id | capacidade | unidade |
|---|---|---|
| `inv.ac.power` | potência ativa AC | W |
| `inv.ac.power.l1/l2/l3` | potência por fase | W |
| `inv.ac.reactive` | potência reativa | var |
| `inv.ac.apparent` | potência aparente | VA |
| `inv.ac.voltage.l1/l2/l3` | tensão por fase | V |
| `inv.ac.current.l1/l2/l3` | corrente por fase | A |
| `inv.ac.frequency` | frequência | Hz |
| `inv.ac.pf` | fator de potência | — |
| `inv.energy.today` / `inv.energy.total` | geração | Wh |
| `inv.dc.bus.voltage` | tensão do barramento DC | V |
| `inv.mppt[n].voltage/current/power` | por MPPT | V/A/W |
| `inv.string[n].current` | corrente por string | A |
| `inv.temp.internal` / `inv.temp.heatsink` | temperatura | °C |
| `inv.status` | estado operacional | enum |
| `inv.fault.code` / `inv.fault.list` | falhas | enum/lista |
| `inv.derate.reason` | motivo de derating | enum |
| `inv.meta.firmware` / `inv.meta.model` / `inv.meta.serial` | identificação | string |

### 1.2 Setpoints / controle (S, W)
| id | capacidade | unidade |
|---|---|---|
| `inv.limit.active` | limite de potência ativa | % ou W |
| `inv.limit.export` | limite de injeção / **zero-export** | % ou W |
| `inv.reactive.setpoint` | reativo alvo | var |
| `inv.pf.setpoint` | fator de potência alvo | — |
| `inv.voltvar.curve` | curva Volt-Var | tabela |
| `inv.voltwatt.curve` | curva Volt-Watt | tabela |
| `inv.freqwatt.curve` | resposta freq-watt | tabela |
| `inv.ramp.rate` | taxa de rampa | %/s |
| `inv.connect` | conectar/desconectar da rede | bool |
| `inv.power.onoff` | ligar/desligar | bool |

### 1.3 Modos (M, RW)
| id | capacidade | valores |
|---|---|---|
| `inv.workmode` | modo de operação | self-use · feed-in-priority · backup · economic · time-of-use · off-grid |
| `inv.reactive.mode` | modo de reativo | fixo-PF · fixo-Q · Volt-Var |

### 1.4 Config / comissionamento (C, RW)
| id | capacidade | unidade |
|---|---|---|
| `inv.grid.standard` | norma/país de rede (grid code) | enum |
| `inv.protect.voltage.hi/lo` | limites de tensão de proteção | V |
| `inv.protect.freq.hi/lo` | limites de frequência | Hz |
| `inv.reconnect.time` | tempo de reconexão | s |
| `inv.antiislanding` | parâmetros anti-ilhamento | enum (R; **não desabilitar** — ver [02](../02-contexto-regulatorio-mercado-br.md)) |
| `inv.drm` | DRM / controle por ripple | enum `[VERIFICAR]` |
| `inv.meter.config` | configuração de CT/medidor | enum |
| `inv.time.sync` | sincronismo de relógio | datetime |

---

## 2. Bateria / ESS — BMS + PCS (`asset = battery`)

### 2.1 Telemetria (T, R)
| id | capacidade | unidade |
|---|---|---|
| `bat.soc` / `bat.soh` | estado de carga / saúde | % |
| `bat.power` | potência (+carrega/−descarrega) | W |
| `bat.voltage` / `bat.current` | tensão / corrente do pack | V / A |
| `bat.energy.charged` / `bat.energy.discharged` | acumulados | Wh |
| `bat.capacity.remaining` / `bat.capacity.rated` | capacidade | Wh |
| `bat.cell.vmin` / `bat.cell.vmax` | tensão de célula | V |
| `bat.temp.min` / `bat.temp.max` | temperatura | °C |
| `bat.cycles` | ciclos | n |
| `bat.power.charge.max` / `bat.power.discharge.max` | limites disponíveis | W |
| `bat.bms.status` / `bat.bms.alarm` | estado/alarmes do BMS | enum |

### 2.2 Setpoints / controle (S, W)
| id | capacidade | unidade |
|---|---|---|
| `bat.power.setpoint` | potência alvo (+carrega/−descarrega) | W |
| `bat.current.limit.charge/discharge` | limites de corrente | A |
| `bat.soc.min` / `bat.soc.max` | janela de SoC | % |
| `bat.backup.reserve.soc` | SoC reservado p/ backup | % |
| `bat.force.charge` / `bat.force.discharge` | forçar (ex.: da rede) | bool/agenda |

### 2.3 Modos (M, RW)
| id | capacidade | valores |
|---|---|---|
| `bat.mode` | modo da bateria | idle · charge · discharge · standby · self-use · tou · backup |

### 2.4 Config (C, RW)
| id | capacidade |
|---|---|
| `bat.chemistry` / `bat.protect.limits` | química e limites de proteção |
| `bat.eps.enable` | habilitar saída de backup (EPS) |

---

## 3. Medidor (`asset = meter`)

| id | capacidade | unidade | tipo |
|---|---|---|---|
| `meter.power.active` (+ `.l1/l2/l3`) | potência ativa (+importa/−exporta) | W | T |
| `meter.power.reactive` / `meter.power.apparent` | reativa / aparente | var / VA | T |
| `meter.voltage.l1/l2/l3` / `meter.current.l1/l2/l3` | tensão / corrente | V / A | T |
| `meter.frequency` / `meter.pf` | frequência / FP | Hz / — | T |
| `meter.energy.import` / `meter.energy.export` | energia bidirecional | Wh | T |
| `meter.demand` | demanda | W | T |
| `meter.thd.v` / `meter.thd.i` | distorção harmônica | % | T `[VERIFICAR]` |
| `meter.ct.ratio` / `meter.wiring` / `meter.sign` | configuração | — | C |

---

## 4. EV Charger (`asset = ev`, base OCPP)

| id | capacidade | unidade | tipo |
|---|---|---|---|
| `ev.state` | estado | enum (Available/Preparing/Charging/Suspended/Finishing/Faulted) | T |
| `ev.power` / `ev.current.l1/l2/l3` / `ev.voltage` | sessão | W / A / V | T |
| `ev.energy.session` / `ev.energy.total` | energia | Wh | T |
| `ev.connector.status` | conector | enum | T |
| `ev.vehicle.soc` | SoC do veículo (ISO 15118) | % | T `[VERIFICAR]` |
| `ev.current.offered` | corrente máx. ofertada (V1G) | A | S/W |
| `ev.power.limit` | limite de potência | W | S/W |
| `ev.tx.start` / `ev.tx.stop` | iniciar/parar transação | — | S/W |
| `ev.pause` / `ev.resume` | pausar/retomar | bool | S/W |
| `ev.schedule` | perfil de carga (SmartCharging) | tabela | S/W |
| `ev.phase.switch` | comutação 1φ/3φ | enum | S/W `[VERIFICAR]` |
| `ev.v2x.discharge` | descarga V2H/V2G (ISO 15118-20) | W | S/W `[VERIFICAR]` |
| `ev.target.soc` | SoC alvo | % | S/W `[VERIFICAR]` |
| `ev.auth.mode` / `ev.ocpp.endpoint` | config | — | C |

---

## 5. Bomba de calor (`asset = heatpump`, SG-Ready / EEBus)

| id | capacidade | unidade | tipo |
|---|---|---|---|
| `hp.state` / `hp.power` | estado / potência | enum / W | T |
| `hp.cop` | COP | — | T `[VERIFICAR]` |
| `hp.temp.flow` / `hp.temp.dhw` / `hp.temp.ambient` | temperaturas | °C | T |
| `hp.sgready.mode` | estado SG-Ready (1 bloqueado · 2 normal · 3 recomendado · 4 forçado) | enum | S/W |
| `hp.temp.setpoint` | temperatura alvo | °C | S/W |
| `hp.power.modulation` | modulação (EEBus) | % | S/W `[VERIFICAR]` |
| `hp.mode` | modo (aquecimento/água/eco) | enum | M |
| `hp.sgready.wiring` / `hp.eebus.pair` | config | — | C |

---

## 6. Carga genérica (`asset = load`, smart plug/relé)

| id | capacidade | unidade | tipo |
|---|---|---|---|
| `load.power` / `load.energy` | potência / energia | W / Wh | T |
| `load.voltage` / `load.current` | tensão / corrente | V / A | T `[VERIFICAR]` |
| `load.switch` | liga/desliga | bool | S/W |
| `load.level` | nível/dimmer | % | S/W `[VERIFICAR]` |
| `load.priority` | prioridade de uso/corte | int | C |
| `load.type` / `load.power.max` | tipo / potência máx. | — | C |

---

## 7. Capacidades transversais (qualquer `asset`)

| id | capacidade | tipo |
|---|---|---|
| `meta.brand` / `meta.model` / `meta.serial` / `meta.firmware` | identificação | T/C |
| `health.status` / `health.alarms` | saúde / alarmes | T |
| `comm.health` / `comm.path` | qualidade e caminho (local/cloud) | T |
| `time.sync` | sincronismo de relógio | C |
| `ota.update` / `ota.version` | atualização de firmware | S/T |
| `commission.discover` | descoberta/one-click scan | C |

---

## 8. Como usar este mapa

- Os **ids** aqui são o **vocabulário fixo**. Os [mapas por fabricante](00-modelo-de-abstracao.md) preenchem **de onde** vem cada id (registrador Modbus/SunSpec ou campo de API).
- Capacidades não suportadas por um modelo ficam **vazias** na [matriz de compatibilidade](matriz-compatibilidade.md) — o superset não muda.
- Para um **novo tipo de ativo** (ex.: novo padrão de EV), adicione uma seção aqui e o tipo na matriz.
- O artefato [`modelo-canonico.schema.json`](../artefatos/modelo-canonico.schema.json) expressa parte deste mapa em JSON Schema (telemetria); este `.md` é a referência humana completa (telemetria + controle + config).
