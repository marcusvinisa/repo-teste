# EOS-DENO · Base de Requisitos de Produto (para Claude Code)
> Snapshot **2026-06-30** · versões confirmadas e consolidadas. A estratégia foi feita no projeto claude.ai; o **build acontece no Claude Code (spec-driven)**. Este pacote é a fundação de requisitos.

## O que é
**EOS-DENO** — plataforma de energia AI-native/operada por agentes (BR), spinoff da empresa-âncora. Beachhead = **integrador/EPC**.

## ⚠ ESCOPO DO v1 — LER PRIMEIRO
**Construir:** o produto do **integrador/EPC (P1)** sobre o **hardware smart-meter existente** (ainda NÃO o ODM próprio).
**Fluxo:** smart-meter → ingestão → time-series → modelo de ativo → **portal do integrador** (monitoramento + frota + comissionamento + diagnóstico remoto).
**Disciplina inegociável:** **camada de abstração de device (S2.3) desde a 1ª linha** — trocar p/ o medidor ODM depois = configuração, não reescrita.
**Fora do v1 (deliberado):** VPP, CCEE, agent-fabric, otimização, mercado livre, os 18 cenários — fase posterior.
**Decisões de build já tomadas:** fork **OpenEMS** (EMS) · build-on **ThingsBoard** (multi-tenant/IoT) · EMHASS/PyPSA (otimização, fase 2). Detalhe por domínio na spec de software.

## Como usar cada bloco
- **00-fundacao/** — contexto e guardrails. `04-MEMORIA` tem o **STATE com o escopo do v1**; `INSTRUCOES` tem o contrato de comportamento (taxonomia, red-team, gates).
- **01-mercado/** — dossiê quantitativo GD compartilhada + ACL (contexto de mercado/regulação).
- **02-hardware/** — requisitos do device: matriz (catálogo O QUE/COMO, 118 sub-itens) · scoring (11 players) · spec (Herdar/Alcançar/Ocupar).
- **03-software/** — requisitos da plataforma: personas + 18 cenários · matriz (~70 microsserviços) · scoring (16 players, dupla-lente) · spec (build/fork/buy por domínio).
- **04-produtos/** — escopo de produto/negócio: 14 produtos em 3 tiers de PMF · unit economics do top-5.
- **05-engenharia-ref-DRAFT/** — arquitetura HEMS + eng HW/FW/cloud/SW. **DRAFT v0.1, marca CORRENTE, pré-recalibração** — ver `_LEIA.md` na pasta.

## Convenção epistêmica (em todos os docs)
**[F]** fato c/ fonte · **[E]** estimativa · **[H]** hipótese · **[INPUT]** placeholder a validar. Benchmarks banana-com-banana (paralelo nomeado + tradução BR). Grande parte do unit economics é [INPUT]/[E] — **validar com descoberta de 2–3 integradores** antes de tratar como verdade.

## Status por bloco
- **Confirmado/consolidado:** 00-fundacao, 01-mercado, 02-hardware, 03-software, 04-produtos.
- **DRAFT (referência, atualizar):** 05-engenharia-ref-DRAFT.
- **Marca pendente:** `02-hardware/scoring-11-players.md` ainda tem "CORRENTE" no rodapé.

## Achados-âncora
- 2 tetos de mercado vazios: **CCEE/BR** e **agent-fabric AI-native (LLM)** — onde o EOS-DENO nasce à frente.
- **P5 Meter MaaS não fecha como SaaS** (LTV:CAC ~1,4x, payback ~69m) — economia de infra, exige financiamento.
- Beachhead integrador = única persona que fecha unit economics sem gatilho regulatório.
