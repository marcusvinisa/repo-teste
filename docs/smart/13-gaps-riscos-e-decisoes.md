# 13 — Gaps, Riscos e Decisões

> Registro honesto do que foi **assumido**, do que **diverge**, do que **falta** e do que pode **dar errado**. É o documento para você revisar e corrigir antes de avançar.

---

## 1. Decisões assumidas como *default* (a confirmar)

A ferramenta de perguntas interativas ficou indisponível na sessão; estas quatro decisões foram tomadas como *default* (todas alinhadas ao seu briefing). **Confirme ou ajuste cada uma:**

| # | Decisão | Default adotado | Alternativas |
|---|---|---|---|
| D1 | **Escopo da documentação** | Suite completa (14 docs) | Núcleo técnico (~6) · Conceito executivo (1–2) |
| D2 | **Estratégia de hardware** | Família OEM/ODM: **Gateway + Controller**, spec + diagrama de blocos + BOM-classe ([06](06-especificacao-hardware.md)) | Design clean-sheet completo · SKU único |
| D3 | **Integração** | **Híbrida** local + cloud-to-cloud ([05](05-integracao-e-conectividade.md)) | Edge-first · API-first |
| D4 | **Personas** | 4 (morador + instalador primárias; agregador + gestor GD avançadas) ([01](01-visao-e-prd.md)) | Subconjunto |

Outros *defaults* menores: **idioma PT-BR**; saída em **.md** no diretório `docs/smart/`; **commit/push** na branch de trabalho.

---

## 2. Divergência de contagem de cenários (15 vs 18)

- A grade completa é **3 arranjos × 6 níveis = 18**; você indicou **15**.
- **Reconciliação proposta:** os 15 núcleo são **N1–N5 × {Cativo, GD compartilhada, Mercado livre}** (5 × 3 = 15); as **3 células N0** ("só consumo", sem ativo a controlar) são baseline de visibilidade/billing, fora dos 15.
- **Ação:** confirme se é essa a intenção (ver [11](11-matriz-de-cenarios.md) §2). Se quiser os N0 como cenários plenos, adotamos 18.

---

## 3. Gaps de contexto (podem limitar/impedir partes)

| Gap | Impacto | Encaminhamento |
|---|---|---|
| **Specs reais das APIs de fabricantes** (campos, limites de controle, contratos de parceria — GoodWe Open-API e outros) | Define o que dá para **controlar** via nuvem ([05](05-integracao-e-conectividade.md)) | Obter docs oficiais + parcerias; marcado `[VERIFICAR]` |
| **Status real de grid services/DR remunerado em BT no Brasil** | Define monetização do **N5** ([02](02-contexto-regulatorio-mercado-br.md)) | Confirmar com ANEEL/ONS/CCEE; construir capacidade, ativar receita depois |
| **Cronograma da abertura do mercado livre BT** | Habilita o **arranjo C** pleno | Acompanhar MME/CCEE; desacoplar no roadmap ([12](12-roadmap-e-faseamento.md)) |
| **Regras/custos de certificação INMETRO/ANATEL/ABNT** | Caminho crítico do hardware ([06](06-especificacao-hardware.md)) | Engenharia de certificação; módulos pré-certificados |
| **Viabilidade regulatória/comercial de V2G no BR** | Modo #9 ([10](10-modos-de-operacao-e-features.md)) | Tratar como futuro `[VERIFICAR]` |
| **Regulação de armazenamento (ESS) no BR** | Modos com bateria/peak shaving | Acompanhar REN/consultas ANEEL |
| **Modelo de negócio e precificação** | Empacotamento/tiers ([01](01-visao-e-prd.md)) | Decisão de negócio do usuário |
| **Identidade de marca "Smart"** (logo, nome final, conflitos de marca) | Branding/white-label | Decisão do usuário / verificação de marca |
| **Requisitos específicos por distribuidora** (parecer de acesso, proteções) | Comissionamento/conexão ([02](02-contexto-regulatorio-mercado-br.md)) | Base de regras por concessionária |
| **Requisitos LGPD** (consentimento, retenção, titularidade dos dados) | Plataforma/dados ([08](08-plataforma-cloud-e-apis.md)) | Avaliação jurídica |

> **Nenhum gap impede começar** (Fase 0/MVP é viável já). Eles condicionam principalmente **N5, mercado livre e controle via nuvem de certos fabricantes**.

---

## 4. Riscos e mitigação

| Categoria | Risco | Mitigação |
|---|---|---|
| **Regulatório** | Mercado de flexibilidade/DR não se materializar em BT | N5 como capacidade técnica; receita opcional; foco em valor cativo/GD |
| **Regulatório** | Mudança nas regras de GD/Fio B | Modelo de tarifa/crédito parametrizável ([04](04-modelo-de-dominio-e-dados.md)) |
| **Técnico** | Fabricante sem controle local nem via API | Preferir local; sinalizar incompatibilidade; ampliar matriz ([05](05-integracao-e-conectividade.md)) |
| **Técnico** | Segurança (comando indevido) | Validação local de limites + mTLS + assinatura ([03](03-arquitetura-de-sistema.md)/[07](07-especificacao-firmware-edge.md)) |
| **Técnico** | Confiabilidade offline | Edge-first com fail-safe ([07](07-especificacao-firmware-edge.md)) |
| **Comercial** | Custo do hardware vs valor percebido | Tiers; modo só-nuvem em N0–N1 ([01](01-visao-e-prd.md)) |
| **Fornecimento** | Disponibilidade de SoC/rádios | Multi-fornecedor; módulos padrão ([06](06-especificacao-hardware.md)) |
| **Cronograma** | Homologações atrasarem | Iniciar cedo; pré-certificados ([12](12-roadmap-e-faseamento.md)) |

---

## 5. Premissas `[PREMISSA]` e itens `[VERIFICAR]` consolidados

- **[PREMISSA]** NFRs (latências, escala, retenção), escolhas de SoC/BOM, datas do roadmap, modelo de receita.
- **[VERIFICAR]** percentuais/datas do Fio B; versões vigentes de REN; cronograma de abertura BT; portarias INMETRO; requisitos ANATEL; status de DR/grid services remunerado; viabilidade de V2G; classe de exatidão de medição exigida; requisitos LGPD.

---

## 6. Perguntas abertas ao usuário

1. Confirma os *defaults* **D1–D4** (§1)?
2. Confirma a reconciliação **15 = N1–N5 × 3 arranjos** (§2)?
3. Idioma final só **PT-BR** ou também **EN** (para fabricantes/investidores)?
4. Profundidade do hardware: mantém **nível OEM/ODM** ou quer **clean-sheet** (esquemático/BOM detalhada)?
5. Prioridade de **fabricantes/ecossistemas** para os primeiros conectores (além de GoodWe)?
6. Há **marca/identidade** definida para "Smart" (ou é nome de trabalho)?
7. Quer que eu gere artefatos extra: **OpenAPI** da API pública, **mapa Modbus/SunSpec** de referência, **checklist de certificação**, ou **modelo de dados** em JSON Schema?

> Responda aqui e eu atualizo a suite e faço novo commit.
