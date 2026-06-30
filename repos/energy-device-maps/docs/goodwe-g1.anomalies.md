# Relatório de ingestão — goodwe / fontes/goodwe-modbus-g1.pdf

Extrator: **docling 2.107.0 (--no-ocr)** · tabelas no doc: **53** · registradores extraídos: **147**

- ⚠️ com flag `verify`: **7**
- sem `type` (Data Format): **15**
- sem `unit`: **37**
- endereços duplicados ignorados: **0**

## Registradores com anomalia (gate de verificação)

| Address | Name | type | unit | access | Flags |
|---|---|---|---|---|---|
| `0x0012` | Min ut/S econ d | u16 | — | RW | nome possivelmente com quebra de linha — conferir verbatim |
| `0x0102` | Range of reactive power adjust H | u16 | Var | RW | valor '66535' — provável typo do PDF para 65535 |
| `0x0103` | Range of reactive power adjust L | u16 | Var | RW | valor '66535' — provável typo do PDF para 65535 |
| `0x0104` | Max value of reactive power adjust H | u16 | Var | R | valor '66535' — provável typo do PDF para 65535 |
| `0x0105` | Max value of reactive power adjust L | u16 | Var | R | valor '66535' — provável typo do PDF para 65535 |
| `0x0106` | High byte: 0-100 , -100 , 0 , 128 ; Low byte: 0~256, ID command ; | f32 | % | W | múltiplos tokens de formato ['Real', 'Integer'] — conferir alinhamento |
| `0x0210` | Model Name of Inverter | string | — | R | range de endereço reconstruído (NNNN-NNNN quebrado pela extração) — conferir |

> Revisar cada linha acima contra a imagem da página antes de mapear `canonical`.
