# Smart — Plataforma Unificada EMS/HEMS · Documentação de Produto

> **Smart** é um produto único de gestão de energia (EMS/HEMS) composto por **aplicação web + mobile + hardware proprietário**, **agnóstico de marca**, que monitora, controla, configura, comissiona e opera inversores e os demais ativos de energia de uma unidade consumidora (UC) de **baixa tensão no Brasil**. Ele unifica e supera dois produtos hoje isolados (um app/portal de nuvem e um gateway de hardware), conectando-se aos ativos por **APIs de fabricantes** (incluindo a própria GoodWe) **e** por **protocolos locais** no hardware — uma topologia mista onde cada função roda na camada certa (só software, software+hardware ou só hardware).

**Versão:** 0.1 (rascunho) · **Data:** 2026-06-27 · **Escopo:** UCs de BT no Brasil (cativo, GD compartilhada, mercado livre).

---

## O que é esta suite

Documentação completa de produto e engenharia para construir o Smart: visão e PRD, contexto regulatório brasileiro, arquitetura de sistema, modelo de dados, integração multimarca, hardware, firmware/edge, plataforma de nuvem, apps/UX, catálogo de modos de operação, matriz de cenários, roadmap, e o registro de gaps/decisões.

> ✅ **Decisões confirmadas.** Escopo: suite completa. Hardware: **Smart Gateway** (controle por **sinal**) + **Smart Meter** (*commodity* < 1%), topologia separada ou integrada. Integração: **híbrida** local + cloud. **4 personas** com roles e atribuições. Cenários: **grade completa de 18**. Idioma: **PT-BR + EN** (espelho em `en/`). Conectores prioritários: **GoodWe, Deye, Sungrow, Growatt, Huawei, Solis**. Pendências e itens `[VERIFICAR]` em **[13 — Gaps, Riscos e Decisões](13-gaps-riscos-e-decisoes.md)**.

---

## Documentos

| # | Documento | Conteúdo |
|---|-----------|----------|
| 01 | [Visão de Produto e PRD](01-visao-e-prd.md) | Problema, proposta de valor, posicionamento, personas, empacotamento, KPIs |
| 02 | [Contexto Regulatório e de Mercado (BR)](02-contexto-regulatorio-mercado-br.md) | ANEEL, GD/Lei 14.300, mercado livre/ACL, tarifas, grid services, normas técnicas |
| 03 | [Arquitetura de Sistema](03-arquitetura-de-sistema.md) | Camadas edge/cloud/apps, topologias mistas, fluxos, NFRs, segurança |
| 04 | [Modelo de Domínio e Dados](04-modelo-de-dominio-e-dados.md) | Entidades, modelo canônico de telemetria, modelo de tarifa |
| 05 | [Integração e Conectividade](05-integracao-e-conectividade.md) | DAL, drivers locais, conectores cloud-to-cloud, matriz de vendors |
| 06 | [Especificação de Hardware](06-especificacao-hardware.md) | Família Smart Gateway + Smart Meter, blocos, I/O, certificações BR |
| 07 | [Especificação de Firmware / Edge](07-especificacao-firmware-edge.md) | Stack, módulos, modos no edge, fail-safe/offline, OTA, segurança |
| 08 | [Plataforma Cloud e APIs](08-plataforma-cloud-e-apis.md) | Microsserviços, time-series, otimização/forecast, VPP, billing, API pública |
| 09 | [Apps Web/Mobile e UX](09-apps-web-mobile-e-ux.md) | Mapa de apps por persona, fluxos, telas, white-label |
| 10 | [Modos de Operação e Features](10-modos-de-operacao-e-features.md) | Catálogo completo com classificação por camada |
| 11 | [Matriz de Cenários (BT Brasil)](11-matriz-de-cenarios.md) | Grade 3 arranjos × 6 níveis, 15 núcleo, fichas por cenário |
| 12 | [Roadmap e Faseamento](12-roadmap-e-faseamento.md) | Fases MVP → tarifa dinâmica/EV → grid services/VPP, make-vs-buy |
| 13 | [Gaps, Riscos e Decisões](13-gaps-riscos-e-decisoes.md) | Decisões assumidas, divergências, gaps, riscos, perguntas abertas |
| 14 | [Glossário](14-glossario.md) | Termos PT-BR/EN |
| 15 | [Modelo de Negócio e Precificação](15-modelo-de-negocio-e-precificacao.md) | Proposta de receita, tiers e go-to-market |

---

## Projeto de Integração (multimarca)

Base viva para mapear ativos de qualquer fabricante (Modbus/SunSpec e APIs), em `docs/smart/integracao/`:

| Arquivo | Conteúdo |
|---|---|
| [Modelo de Abstração](integracao/00-modelo-de-abstracao.md) | Como representar dispositivos e adicionar mapas por fabricante |
| [Mapa Canônico de Capacidades](integracao/mapa-canonico-capacidades.md) | Superset de capacidades (geração, armazenamento e demais ativos) |
| [Template — Modbus/SunSpec](integracao/template-fabricante-modbus.md) | Modelo `.md` para mapa local por fabricante |
| [Template — API](integracao/template-fabricante-api.md) | Modelo `.md` para mapa de API cloud por fabricante |
| [Matriz de Compatibilidade](integracao/matriz-compatibilidade.md) | Banco marca × modelo × tipo × capacidade |
| [Prompt — Projeto Externo](integracao/PROMPT-projeto-externo.md) | Prompt para ingestão dos mapas oficiais (via markitdown) em outra sessão |

## Artefatos técnicos

Em `docs/smart/artefatos/`:

| Arquivo | Conteúdo |
|---|---|
| [openapi.yaml](artefatos/openapi.yaml) | Contrato REST (rascunho) da API pública |
| [modelo-canonico.schema.json](artefatos/modelo-canonico.schema.json) | JSON Schema do modelo canônico (telemetria/dispositivos/comandos) |
| [checklist-certificacao-br.md](artefatos/checklist-certificacao-br.md) | Checklist de certificação/conformidade no Brasil |
| [diagrama-tarifas-cenarios.md](artefatos/diagrama-tarifas-cenarios.md) | Diagramas de tarifas, sinais de preço e alavancas de valor |

---

## Ordem de leitura recomendada

- **Executivo / negócio:** 01 → 11 → 12 → 13
- **Engenharia de produto / arquitetura:** 03 → 04 → 05 → 10 → 08
- **Hardware / firmware:** 06 → 07 → 05 → 03
- **Regulatório / mercado:** 02 → 11 → 13
- **Sempre à mão:** [14 — Glossário](14-glossario.md)

---

## Convenções

Toda feature/modo de operação é classificada pela **camada que a executa**:

| Etiqueta | Significado |
|----------|-------------|
| `[SW]` | Só software (nuvem ou app) |
| `[SW+HW]` | Requer software **e** hardware proprietário |
| `[HW]` | Só hardware/edge — determinístico, funciona offline |
| `[AMBOS]` | Pode ser feito pelo app **ou** pelo hardware |

Marcações `[PREMISSA]` (suposição de projeto) e `[VERIFICAR]` (item a confirmar com fonte externa) aparecem ao longo da suite.
