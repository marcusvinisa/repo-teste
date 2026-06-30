# energy-device-maps

> Registro **versionado** de **perfis de dispositivo** (mapas Modbus/SunSpec por fabricante/modelo) que ligam **registradores → capacidades canônicas** ([modelo canônico](canonical/mapa-canonico-capacidades.md)), + uma biblioteca para **carregar/validar/decodificar/codificar** e uma **CLI** que ingere os documentos oficiais de protocolo (via [markitdown](https://github.com/microsoft/markitdown)) e gera perfis-rascunho. Reutilizável por qualquer edge/gateway/EMS.

- **Spec:** [`SPEC.md`](SPEC.md) — leia primeiro.
- **Bootstrap (outra sessão):** [`BOOTSTRAP-PROMPT.md`](BOOTSTRAP-PROMPT.md).
- **Contrato canônico:** [`canonical/`](canonical/).

## Em uma linha
"Os mapas Modbus/SunSpec do mercado, padronizados num formato único — qualquer gateway lê o canônico, não o registrador cru."

## Onde se encaixa
É a peça **local/edge** da camada de integração. No catálogo EOS-DENO equivale a **S0.2 (Protocol Adapter Registry)**; o par cloud é o [`energy-connectors`](../energy-connectors/). Consumido pelo [firmware/edge Smart](../../docs/smart/07-especificacao-firmware-edge.md) e por terceiros.

## Fundações OSS candidatas (build-on)
- **SunSpec models** (open) — base padronizada (inversor 101/102/103, storage 124, meter 201–204, battery 802+).
- **pymodbus** (ou libmodbus) — transporte Modbus RTU/TCP.
- **pydantic / jsonschema** — validação dos perfis.
- **markitdown** — conversão dos PDFs oficiais → Markdown para extração.
- O **formato de perfil** e o decode/encode canônico são **build** (não há padrão único de "registry de perfis multimarca").

## Status
Seed (spec + schema de perfil definidos; perfis e lib na sessão dedicada — ver bootstrap).
