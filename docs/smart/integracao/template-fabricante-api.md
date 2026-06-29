# Template — Mapa de API Cloud por Fabricante

> Copie para `fabricantes/api/<marca>.md` e preencha a partir da **documentação oficial da API** do fabricante. Ligue cada endpoint/campo a uma **capacidade canônica** do [mapa canônico](mapa-canonico-capacidades.md). Conector cloud-to-cloud da [camada de integração](../05-integracao-e-conectividade.md).

---

## Identificação

| Campo | Valor |
|---|---|
| Marca | `<ex.: Sungrow>` |
| Nome da API | `<ex.: iSolarCloud OpenAPI>` |
| Base URL / região | `<>` `[VERIFICAR]` |
| Autenticação | OAuth2 / API key / appkey+secret `[VERIFICAR]` |
| Acesso | parceria necessária? sim/não |
| Rate limits | `<req/min>` `[VERIFICAR]` |
| Granularidade/latência de dados | `<ex.: 5 min>` |
| Suporta **controle (escrita)**? | sim/limitado/não |
| Fonte (doc oficial) | `<link/arquivo + data>` |

## Capacidades de LEITURA (telemetria)

| Capacidade canônica (id) | Endpoint | Campo na resposta | Unidade | Observações |
|---|---|---|---|---|
| `inv.ac.power` | `GET <...>` | `<json.path>` | W | |
| `inv.energy.today` | `GET <...>` | `<json.path>` | Wh | |
| `bat.soc` | `GET <...>` | `<json.path>` | % | |
| `meter.power.active` | `GET <...>` | `<json.path>` | W | |
| `...` | | | | |

## Capacidades de CONTROLE (escrita)

| Capacidade canônica (id) | Endpoint | Corpo/parâmetro | Limites | Observações |
|---|---|---|---|---|
| `inv.limit.active` | `POST <...>` | `<>` | | `[VERIFICAR se permitido]` |
| `bat.mode` | `POST <...>` | `<>` | | |
| `bat.backup.reserve.soc` | `POST <...>` | `<>` | | |
| `...` | | | | |

## Mapa de enums / estados

| Capacidade | Valor nativo | Valor canônico |
|---|---|---|
| `inv.status` | `<>` | `<>` |

## Lacunas e riscos

- `[VERIFICAR]` o que a API **não** permite controlar (muitas só leem).
- Dependência de **parceria/credenciais**; quotas; disponibilidade regional.
- Preferir caminho **local** para controle crítico quando a API for só leitura.
