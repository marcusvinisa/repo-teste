# 13 — Gaps, Riscos e Decisões

> Registro das **decisões confirmadas**, do que ainda **falta** e do que pode **dar errado**. Atualizado após a rodada de confirmações com o usuário e a pesquisa regulatória.

---

## 1. Decisões confirmadas

| # | Tema | Decisão final |
|---|---|---|
| D1 | **Escopo da documentação** | ✅ **Suite completa** + artefatos técnicos (OpenAPI, JSON Schema, mapa canônico, checklist de certificação, diagrama de cenários) |
| D2 | **Hardware** | ✅ **Smart Gateway** (cérebro + controle por **sinal**; aciona contator/disjuntor/ATS **externos**, não chaveia potência) + **Smart Meter** (*commodity*, exatidão **< 1%**, no quadro/QGBT). Topologias: **T1 separada** ou **T2 integrada**. **Sem** SKU "Controller". Nível OEM/ODM. Ver [06](06-especificacao-hardware.md) |
| D3 | **Integração** | ✅ **Híbrida** local + cloud-to-cloud ([05](05-integracao-e-conectividade.md)) |
| D4 | **Personas** | ✅ **4 personas** com roles/atribuições: morador + instalador (primárias), agregador + gestor GD (avançadas). RBAC em [08](08-plataforma-cloud-e-apis.md) |
| D5 | **Cenários** | ✅ **Grade completa de 18** (3 arranjos × 6 níveis), N0 incluídos como cenários plenos ([11](11-matriz-de-cenarios.md)) |
| D6 | **Idioma** | ✅ **PT-BR + EN** (espelho em `docs/smart/en/`) |
| D7 | **Conectores prioritários** | ✅ **GoodWe, Deye, Sungrow, Growatt, Huawei, Solis** ([05](05-integracao-e-conectividade.md)) |
| D8 | **Marca** | ✅ **"Smart"** é nome definitivo |
| D9 | **Mapa de integração** | ✅ Mapa **canônico** (superset de capacidades) + **modelo de abstração** + **templates por fabricante** + **matriz de compatibilidade** + **prompt de projeto externo** (ingestão via *markitdown*). Ver `docs/smart/integracao/` |

---

## 2. Itens regulatórios validados na pesquisa (jun/2026)

Itens antes marcados `[VERIFICAR]` agora **confirmados** com fontes públicas (ver [02](02-contexto-regulatorio-mercado-br.md)):

| Tema | Situação confirmada |
|---|---|
| **Fio B (Lei 14.300)** | Rampa **15/30/45/60/75/90%** (2023→2028); **2029** = ANEEL revisa metodologia (CNPE). GD I (≤6/jan/2023) isenta até **2045**. Autoconsumo instantâneo isento |
| **Mercado livre BT** | **Lei nº 15.269/2025**: BT comercial/industrial até **nov/2027**, residencial até **nov/2028**; cria **Supridor de Última Instância (SUI)** |
| **INMETRO inversores** | **Portaria 140/2022** + **515/2023** (desconexão de emergência); escopo ≤ 75 kW; aplica-se ao inversor, não ao Gateway/Meter |
| **Grid services / RED** | ANEEL: **sandbox** de serviços ancilares; ONS autorizado a contratar **controle de tensão** (2025); agenda de **observabilidade/operabilidade/controlabilidade de RED**; **CP 001/2026** sobre medidores inteligentes em BT |

---

## 3. Gaps remanescentes

| Gap | Impacto | Encaminhamento |
|---|---|---|
| **Specs reais das APIs de fabricantes** (campos, limites de controle, contratos) — GoodWe, Deye/Solarman, Sungrow, Growatt, Huawei, Solis | Define o que dá para **controlar** via nuvem ([05](05-integracao-e-conectividade.md)) | **Projeto externo** (D9): ingerir docs oficiais via *markitdown* e popular a matriz; marcado `[VERIFICAR]` |
| **Mapas Modbus/SunSpec proprietários por modelo** | Drivers locais | Idem D9 — usuário recebe os mapas oficiais por e-mail e popula os templates |
| **Regulamentação infralegal do mercado livre BT** | Detalhes de medição/contratação do arranjo C | Acompanhar ANEEL (horizonte 2027) |
| **Regras finais de remuneração de flexibilidade/DR em BT** | Monetização do N5 | Construir capacidade; ativar receita conforme sandbox/regras evoluem |
| **Classe metrológica do Smart Meter** | Certificação do medidor ([06](06-especificacao-hardware.md)) | **Proposto:** EMS = classe 1 / 0,5S (≤1%); faturamento = INMETRO RTM 587 + PRODIST M5 + SMF. `[VERIFICAR por uso]` |
| **Custos/prazos de ANATEL e ensaios EMC** | Caminho crítico do hardware | Engenharia de certificação; módulos pré-certificados |
| **Viabilidade regulatória/comercial de V2G no BR** | Modo #9 ([10](10-modos-de-operacao-e-features.md)) | Tratar como futuro `[VERIFICAR]` |
| **Regulação de armazenamento (ESS) no BR** | Modos com bateria | Acompanhar REN/consultas ANEEL |
| **Modelo de negócio e precificação** | Empacotamento/tiers ([01](01-visao-e-prd.md)) | **Proposta** em [15](15-modelo-de-negocio-e-precificacao.md); aguarda decisão do usuário |
| **Requisitos LGPD** (consentimento, retenção, titularidade) | Plataforma/dados ([08](08-plataforma-cloud-e-apis.md)) | Avaliação jurídica |
| **Requisitos específicos por distribuidora** (parecer de acesso) | Comissionamento/conexão | Base de regras por concessionária |

> **Nenhum gap impede começar** — a Fase 0/MVP é viável já. Eles condicionam principalmente **N5, mercado livre pleno e controle via nuvem de certos fabricantes**.

---

## 4. Riscos e mitigação

| Categoria | Risco | Mitigação |
|---|---|---|
| **Regulatório** | Remuneração de flexibilidade/DR em BT demorar | N5 como capacidade técnica; foco em valor cativo/GD/controle de tensão |
| **Regulatório** | Mudanças em GD/Fio B | Modelo de tarifa/crédito parametrizável ([04](04-modelo-de-dominio-e-dados.md)) |
| **Técnico** | Fabricante sem controle local nem via API | Preferir local; sinalizar incompatibilidade; ampliar matriz ([05](05-integracao-e-conectividade.md)) |
| **Técnico** | Segurança (comando indevido) | Validação local de limites + mTLS + assinatura ([03](03-arquitetura-de-sistema.md)/[07](07-especificacao-firmware-edge.md)) |
| **Técnico** | Confiabilidade offline | Edge-first com fail-safe ([07](07-especificacao-firmware-edge.md)) |
| **Comercial** | Custo do hardware vs valor | Tiers; modo só-nuvem em N0–N1 ([01](01-visao-e-prd.md)) |
| **Fornecimento** | Disponibilidade de SoC/rádios | Multi-fornecedor; módulos padrão ([06](06-especificacao-hardware.md)) |
| **Cronograma** | Homologações atrasarem | Iniciar cedo; pré-certificados ([12](12-roadmap-e-faseamento.md)) |

---

## 5. Premissas `[PREMISSA]` e itens `[VERIFICAR]` consolidados

- **[PREMISSA]** NFRs (latências, escala, retenção), escolhas de SoC/BOM, datas do roadmap, modelo de receita.
- **[VERIFICAR]** regulamentação infralegal do mercado livre BT; regras finais de DR/flexibilidade; classe metrológica do Smart Meter; requisitos ANATEL/EMC; viabilidade de V2G; regulação de ESS; LGPD; mapas Modbus/API por fabricante (projeto externo D9).

---

## 6. Perguntas abertas restantes

1. **Modelo de negócio/precificação** — proposta em [15](15-modelo-de-negocio-e-precificacao.md); falta decidir HW (venda/locação/HaaS), faixas de preço, R3/R4 e canal.
2. **Classe metrológica** — proposta: EMS = classe 1 / 0,5S (≤ 1%); faturamento = INMETRO RTM 587 + PRODIST M5 + SMF. Confirma?
3. **Prioridade dos artefatos extra** já gerados — quer aprofundar algum (ex.: OpenAPI completo, JSON Schema por tipo de ativo)?
4. **Projeto externo de integração** — quando tiver os mapas oficiais, rodamos o prompt de `docs/smart/integracao/PROMPT-projeto-externo.md` em outra sessão e fazemos o merge.

> Responda e eu atualizo a suite + novo commit.
