# energy-connectors

> Serviço **vendor-agnóstico** que conecta às **nuvens de fabricantes de energia** (GoodWe, Deye/Solarman, Sungrow, Growatt, Huawei, Solis…) e expõe **uma única API normalizada** mapeada ao [modelo canônico](canonical/mapa-canonico-capacidades.md). Lê telemetria e executa controle **onde o fabricante permite**. Reutilizável em qualquer projeto de EMS/HEMS/VPP.

- **Spec:** [`SPEC.md`](SPEC.md) — leia primeiro.
- **Bootstrap (outra sessão):** [`BOOTSTRAP-PROMPT.md`](BOOTSTRAP-PROMPT.md).
- **Contrato canônico:** [`canonical/`](canonical/).

## Em uma linha
"Um conector universal para nuvens de inversores/baterias — fala N APIs proprietárias, devolve um modelo único."

## Onde se encaixa
É a variante **cloud-to-cloud** da camada de ingestão. No catálogo EOS-DENO equivale a **S0.1 (Device Gateway/Connector)** + **S0.2 (Protocol Adapter Registry)** no plano da nuvem; o par local é o [`energy-device-maps`](../energy-device-maps/). Consumido pela [plataforma Smart cloud](../../docs/smart/08-plataforma-cloud-e-apis.md) e pela [camada de integração](../../docs/smart/05-integracao-e-conectividade.md).

## Fundações OSS candidatas (build-on, não reescrever)
- **ThingsBoard / OpenRemote** — gestão de dispositivos/tenant, ingestão (referência de S0).
- **OpenEMS** — modelo de connectors/edge (referência de driver agnóstico).
- Não há OSS pronto para "multi-vendor cloud connector BR" → o núcleo de adaptadores é **build**.

## Status
Seed (spec pronta; implementação na sessão dedicada — ver bootstrap).
