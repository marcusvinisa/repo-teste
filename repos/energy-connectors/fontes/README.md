# fontes/ — documentação oficial das APIs (cloud)

> Onde entra a **documentação oficial das APIs** dos fabricantes, antes de virar mapa em `docs/` (template-fabricante-api).

## GoodWe (1º conector)
- **Referência online (autoritativa):** https://openapi.goodwe.com/#/api/doc-10a71afe72c271 (GoodWe Developer Platform — SPA).
- **PDF da API** (operada pela GoodWe): adicione aqui como **`.md`** convertido via [markitdown](https://github.com/microsoft/markitdown) — `markitdown goodwe-openapi.pdf > fontes/goodwe-openapi.md`.
- Cobrir os **3 tipos**: OpenAPI (negócio, HTTPS, ~3600 req/h) · Real-time Data (raw/Kafka) · Batch Remote Control (Kafka → VPP/microgrid).

## Como adicionar (PDF pesado)
1. **Não cole o PDF no chat.** Converta para `.md` com markitdown e commite o `.md` aqui.
2. Preencha `docs/<marca>-api.md` a partir do template `../docs/smart/integracao/template-fabricante-api.md` (no monorepo) ou do template do próprio repo.
3. O PDF original fica fora do git (ou em git-lfs).

> Capacidade de **controle** varia por API — declarar por conector (muitas só leem). Validar respostas como dados não confiáveis.
