# Referências de Produto (fonte para PRD/ADR)

> Coloque aqui os **specs de produto** exportados do projeto no Claude.ai (visão de plataforma, features, funções futuras). Este material é a **fonte citável** do PRD consolidado e dos ADRs.

## O que colocar
- Documentos de visão/plataforma, listas de features, requisitos, roadmap, casos de uso, benchmarks, etc.
- Formatos aceitos: **Markdown/txt (ideal)**, **PDF**, **DOCX**, planilhas (CSV/XLSX). PDF/DOCX eu converto (docling/markitdown).

## Como nomear (ajuda a rastrear)
`AAAA-tema.md` — ex.: `2026-visao-plataforma.md`, `2026-features-hems.md`, `2026-funcoes-futuras.md`.

## Depois de subir
Avise no chat ("subi as referências"). Eu faço `git pull`, **leio e extraio todos os requisitos** (atual vs novo, gaps, conflitos) e sigo para o **PRD + ADRs** (gate de revisão).

> Esta pasta é destino de **fontes brutas**; a consolidação vai para `docs/smart/PRD.md` e `docs/smart/adr/`.
