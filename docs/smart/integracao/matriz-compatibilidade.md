# Integração — Matriz de Compatibilidade

> Banco de **compatibilidade** marca × modelo × tipo × capacidade × caminho, **curado por tipo de ativo**. É o índice consultável que diz o que o Smart consegue **ler/controlar** de cada equipamento e por onde. Alimentado pelos [mapas por fabricante](00-modelo-de-abstracao.md); itens não levantados ficam `[VERIFICAR]`.

**Legenda:** ✅ suportado · ⚠️ parcial · ❌ não · `?` a levantar. **Caminho:** `L` local (Modbus/SunSpec/OCPP/...) · `C` cloud (API). **Status Smart:** `testado` / `beta` / `planejado`.

---

## 1. Inversores PV / Híbridos (`inverter`)

| Marca | Série/Modelo | Caminho | Telemetria | Limite ativa/export | Reativo/PF | Workmode | Controle bateria | SunSpec | Status |
|---|---|---|---|---|---|---|---|---|---|
| GoodWe | ET / EH `[VERIFICAR]` | L+C | ? | ? | ? | ? | ? | ? | planejado |
| Deye | SUN-…SG `[VERIFICAR]` | L+C | ? | ? | ? | ? | ? | ? | planejado |
| Sungrow | SH-RS / SH-RT `[VERIFICAR]` | L+C | ? | ? | ? | ? | ? | ? | planejado |
| Growatt | MIN / SPH `[VERIFICAR]` | L+C | ? | ? | ? | ? | ? | ? | planejado |
| Huawei | SUN2000 `[VERIFICAR]` | L+C | ? | ? | ? | ? | ? | ? | planejado |
| Solis | S6 `[VERIFICAR]` | L+C | ? | ? | ? | ? | ? | ? | planejado |

## 2. Baterias / ESS (`battery`)

| Marca | Modelo | Caminho | SoC/SoH | Setpoint potência | Janela SoC | Backup reserve | Status |
|---|---|---|---|---|---|---|---|
| `<marca>` | `<modelo>` | L/C | ? | ? | ? | ? | planejado |

## 3. Medidores (`meter`)

| Marca | Modelo | Caminho | P/Q/V/I | Energia bi | Classe exatidão | Status |
|---|---|---|---|---|---|---|
| `<commodity>` | `<modelo>` | L | ? | ? | < 1% `[VERIFICAR]` | planejado |

## 4. EV Chargers (`ev`) — futuro

| Marca | Modelo | Caminho | OCPP ver. | SmartCharging | V2X | Status |
|---|---|---|---|---|---|---|
| `<marca>` | `<modelo>` | L (OCPP) | 1.6/2.0.1 | ? | ? | planejado |

## 5. Bombas de calor (`heatpump`) — futuro

| Marca | Modelo | Caminho | SG-Ready | EEBus | Modulação | Status |
|---|---|---|---|---|---|---|
| `<marca>` | `<modelo>` | L | ? | ? | ? | planejado |

## 6. Cargas / smart plugs (`load`)

| Marca | Modelo | Caminho | Medição | Chaveamento | Status |
|---|---|---|---|---|---|
| Shelly (e compatíveis) | `<modelo>` | L (Wi-Fi/Matter) | ✅ | ✅ | beta `[VERIFICAR]` |

---

## 7. Curadoria por tipo (regras)

- **Chave primária:** `marca + modelo + firmware`.
- **Capacidades** referenciam ids do [mapa canônico](mapa-canonico-capacidades.md).
- **Caminho duplo (L+C):** registrar capacidades por caminho; controle crítico prioriza `L`.
- **Novos tipos** (ex.: outros EV chargers): adicionar seção mantendo o mesmo cabeçalho (marca/modelo/caminho/capacidades/status).
- **Auditoria:** cada linha cita a **fonte** e a **data** do levantamento.

> Preenchimento em escala: ver [PROMPT-projeto-externo.md](PROMPT-projeto-externo.md).
