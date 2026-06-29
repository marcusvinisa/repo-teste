# Template — Mapa Modbus/SunSpec por Fabricante

> Copie este arquivo para `fabricantes/modbus/<marca>-<serie>.md` e preencha a partir do **documento oficial "Modbus protocol"** do fabricante (convertido via [markitdown](https://github.com/microsoft/markitdown) em `fontes/`). Ligue cada registrador a uma **capacidade canônica** do [mapa canônico](mapa-canonico-capacidades.md).

---

## Identificação

| Campo | Valor |
|---|---|
| Marca | `<ex.: GoodWe>` |
| Série / modelos cobertos | `<ex.: ET 6.0-15.0kW>` |
| Tipo(s) de ativo | `inverter` / `battery` / `meter` |
| Firmware mínimo | `[VERIFICAR]` |
| Protocolo | Modbus-RTU (RS485) / Modbus-TCP / SunSpec |
| Endereço/Unit ID padrão | `<ex.: 247>` |
| Baud / paridade (RTU) | `<ex.: 9600 8N1>` |
| Fonte (doc oficial) | `<arquivo em fontes/ + versão + data>` |
| Compatível com SunSpec? | sim/parcial/não (se sim, citar models) |

## Convenções do fabricante

- Endianness: `<big/little, word swap?>` `[VERIFICAR]`
- Tipo de dado: `<U16/S16/U32/S32/float32...>`
- Escala/ganho: `<fator>` · Offset: `<>`
- Função Modbus de leitura/escrita: `<03/04/06/16>`

## Mapeamento registrador → capacidade canônica

| Capacidade canônica (id) | Registrador | Tipo dado | Escala | Unidade | Acesso | Observações |
|---|---|---|---|---|---|---|
| `inv.ac.power` | `<addr>` | S32 | x1 | W | R | |
| `inv.energy.today` | `<addr>` | U32 | x0.1 | kWh→Wh | R | |
| `inv.mppt[1].voltage` | `<addr>` | U16 | x0.1 | V | R | |
| `bat.soc` | `<addr>` | U16 | x1 | % | R | |
| `bat.power.setpoint` | `<addr>` | S16 | x1 | W | W | sinal +carrega/−descarrega |
| `inv.limit.export` | `<addr>` | U16 | x1 | % | RW | zero-export |
| `inv.workmode` | `<addr>` | enum | — | enum | RW | mapear valores → canônico |
| `...` | | | | | | |

> Liste **todos** os registradores relevantes do doc oficial. Capacidades canônicas sem registrador correspondente = **não suportadas** por este modelo (deixar fora ou marcar `[VERIFICAR]`).

## Mapa de enums

| Capacidade | Valor nativo | Valor canônico |
|---|---|---|
| `inv.workmode` | `0` | self-use |
| `inv.workmode` | `1` | feed-in-priority |
| `inv.status` | `<n>` | `<estado canônico>` |

## Lacunas e riscos

- `[VERIFICAR]` registradores não documentados / divergências por firmware.
- Limitações de escrita (alguns setpoints só via app do fabricante).
