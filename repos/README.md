# Repos externos do Smart — Conectores & Mapas de Dispositivos

> Dois serviços **standalone e reutilizáveis** que materializam o [projeto de integração](../docs/smart/integracao/00-modelo-de-abstracao.md) (decisão **D9**). São **sementes de repositórios separados** — pensados para serem usados pela plataforma Smart **e** em outros projetos. Construídos sob a metodologia **spec-driven** (spec → plano → tarefas → implementação), **contrato-primeiro** e **fatias verticais**.

| Repo | O que é | Camada | Linguagem sugerida |
|---|---|---|---|
| [`energy-connectors`](energy-connectors/) | Serviço que conecta às **nuvens de fabricantes** (GoodWe, Deye/Solarman, Sungrow, Growatt, Huawei, Solis…) e expõe **uma API normalizada** mapeada ao modelo canônico | cloud-to-cloud `[SW]` | TypeScript/Node `[a confirmar]` |
| [`energy-device-maps`](energy-device-maps/) | Registro de **perfis Modbus/SunSpec** por fabricante/modelo (registrador → capacidade canônica) + lib de leitura/validação + CLI de ingestão (markitdown) | local/edge `[HW]` | Python `[a confirmar]` |

## Contrato compartilhado: o modelo canônico

Ambos os repos dependem do **mesmo contrato canônico** — o vocabulário agnóstico de capacidades. Ele é **vendado** em cada repo em `canonical/`:
- `canonical/modelo-canonico.schema.json` — JSON Schema (telemetria/dispositivos/comandos).
- `canonical/mapa-canonico-capacidades.md` — referência humana (superset de capacidades).

> **Regra de sincronização:** o canônico é a **fonte de verdade** mantida na plataforma Smart ([docs/smart/integracao](../docs/smart/integracao/mapa-canonico-capacidades.md)). Cada repo carrega uma cópia versionada; mudanças no canônico propagam-se aos repos por atualização explícita (não divergir silenciosamente). Novos `ids` propostos pelos repos voltam como sugestão ao canônico.

## Como se encaixam na plataforma Smart

```mermaid
flowchart LR
  subgraph EDGE[Edge / Gateway]
    dm[energy-device-maps\n(perfis + driver local)]
  end
  subgraph CLOUD[Smart Cloud]
    ec[energy-connectors\n(API normalizada multimarca)]
  end
  canon[(Contrato canônico\nmodelo-canonico.schema.json)]
  dm --> canon
  ec --> canon
  dm -->|Modbus/SunSpec| ativos[Ativos locais]
  ec -->|APIs| nuvens[Nuvens de fabricantes]
  canon --> plat[Plataforma Smart / DAL]
```

- `energy-device-maps` é consumido pelo **firmware/edge** ([07](../docs/smart/07-especificacao-firmware-edge.md)) para falar Modbus/SunSpec local.
- `energy-connectors` é consumido pela **nuvem** ([08](../docs/smart/08-plataforma-cloud-e-apis.md)) para falar com as nuvens dos fabricantes.
- Os dois entregam dados/controle no **modelo canônico** ([05](../docs/smart/05-integracao-e-conectividade.md)).

## Como usar os bootstrap prompts

Cada repo tem um **`BOOTSTRAP-PROMPT.md`** — um prompt completo para colar numa **nova sessão do Claude Code** (em um repositório vazio) e construir o serviço do zero pelo fluxo spec-driven. O prompt é **self-contained**: referencia o contrato canônico e a spec do próprio repo. Reutilizável em outros projetos — basta copiar a pasta `canonical/` e o `SPEC.md`.

> Estes são **seeds**: a `SPEC.md` e o `BOOTSTRAP-PROMPT.md` definem o produto; a implementação (código, testes) é feita na sessão dedicada de cada repo.
