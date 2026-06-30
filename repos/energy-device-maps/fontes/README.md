# fontes/ — documentos oficiais de protocolo (Modbus)

> Onde entram os **documentos oficiais de protocolo Modbus** dos fabricantes, **antes** de virarem perfis em `profiles/`.

## Como adicionar (PDF pesado → Markdown)
1. **Não cole o PDF no chat** (pesa demais e estoura o contexto). Em vez disso:
2. Converta o PDF para Markdown com **[markitdown](https://github.com/microsoft/markitdown)**:
   `markitdown goodwe-modbus-hybrid-g2.pdf > fontes/goodwe-modbus-hybrid-g2.md`
3. Commite o **`.md`** aqui (leve, versionável, diff-friendly). O PDF original pode ficar fora do git (ou em git-lfs se quiser versioná-lo).
4. Rode `edmaps ingest fontes/<arquivo>.md --vendor goodwe --model <serie>` para gerar o perfil-rascunho em `profiles/goodwe/`, e revise.

## GoodWe (1º fabricante) — esperado
O mapa Modbus da GoodWe cobre **duas linhas × duas gerações**:

| Linha | Geração | Perfil destino (sugerido) |
|---|---|---|
| Híbrido | G1 | `profiles/goodwe/hybrid-g1.yaml` |
| Híbrido | G2 | `profiles/goodwe/hybrid-g2.yaml` |
| Grid-tie | G1 | `profiles/goodwe/grid-tie-g1.yaml` |
| Grid-tie | G2 | `profiles/goodwe/grid-tie-g2.yaml` |

> Cada perfil cita `source` (arquivo em `fontes/` + versão + data). Registradores não documentados → `gaps` com `[VERIFICAR]`. Não comitar PDF proprietário sem licença/permissão.
