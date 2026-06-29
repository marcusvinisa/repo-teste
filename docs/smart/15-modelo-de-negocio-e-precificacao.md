# 15 — Modelo de Negócio e Precificação (Proposta)

> **`[PROPOSTA — decisão de negócio do usuário]`** Modelo de receita, precificação por tier/persona e *go-to-market* para o Smart. Não é decisão fechada: é um ponto de partida com opções e recomendação. Liga-se a [01 — Visão/PRD](01-visao-e-prd.md) (tiers), [11 — Cenários](11-matriz-de-cenarios.md) e [12 — Roadmap](12-roadmap-e-faseamento.md).

---

## 1. Fontes de receita

| # | Fonte | Descrição | Quem paga |
|---|---|---|---|
| R1 | **Hardware** | Venda ou locação do **Smart Gateway** / **Smart Meter** ([06](06-especificacao-hardware.md)) | Proprietário ou instalador |
| R2 | **Assinatura de software (SaaS)** | Por **UC**, escalonada por tier/nível de ativo ([01](01-visao-e-prd.md)) | Proprietário / instalador |
| R3 | **Fee de serviços de mercado** | % sobre receita de **VPP/grid services** e arbitragem (quando houver) | Agregador / proprietário |
| R4 | **Fee de GD compartilhada** | Por UC participante ou % sobre créditos rateados | Gestor de GD |
| R5 | **Licença white-label / API** | Plataforma sob marca de canal (instalador/comercializadora) | Canal/parceiro |
| R6 | **Serviços profissionais** | Comissionamento, integração, suporte premium | Instalador / cliente final |

---

## 2. Precificação por tier (proposta indicativa) `[PREMISSA]`

> Valores são **placeholders** para discussão — não são preços validados de mercado.

| Tier ([01](01-visao-e-prd.md)) | Hardware | Assinatura | Observação |
|---|---|---|---|
| **Smart Lite** `[SW]` | — | gratuito ou baixo/UC/mês | monitoramento via API; porta de entrada |
| **Smart Home** `[SW+HW]` | Gateway (venda/locação) | mensal/UC | autoconsumo, backup, EV, automações |
| **Smart Home+** `[SW+HW]` | Gateway + Smart Meter | mensal/UC (maior) | otimização por preço + load shifting |
| **Smart Grid** `[SW+HW]` | Gateway + Smart Meter | mensal/UC + **R3** | grid services/VPP + revenue share |
| **Smart Pro/Fleet** `[SW]` | — | por seat/UC sob gestão | instalador/agregador; volume |
| **Smart DG** `[SW]` | — | por UC participante (**R4**) | gestor de GD |

---

## 3. Opções de modelo (escolher 1 como principal)

| Opção | Lógica | Prós | Contras |
|---|---|---|---|
| **A — Hardware + SaaS** (recomendada) | vende/loca HW + assinatura recorrente por UC | receita recorrente, alinha valor; clássico HEMS | exige base instalada p/ escalar |
| **B — HaaS (tudo como serviço)** | hardware embutido numa mensalidade única | baixa barreira de entrada p/ o cliente | capital intensivo; risco de churn |
| **C — Plataforma/atacado (B2B2C)** | vende para instaladores/comercializadoras que revendem | escala via canal, white-label (R5) | margem menor por UC; depende do canal |
| **D — Energia-as-a-service / share de economia** | cobra % da economia/receita gerada | alинhamento total com resultado | medição/atribuição complexa; fluxo de caixa |

> **Recomendação:** **A** como base (HW + SaaS por UC), com **C** (canal/white-label) para escala e **R3/R4** ativando-se nos níveis N5 e arranjo B. **D** como oferta opcional para grandes contas/agregadores.

---

## 4. Considerações de unit economics `[PREMISSA]`

- **Margem de hardware:** OEM/ODM com rádios pré-certificados reduz COGS ([06](06-especificacao-hardware.md)/[12](12-roadmap-e-faseamento.md)).
- **LTV/CAC:** assinatura recorrente (R2) sustenta CAC do canal; locação (R1) suaviza barreira.
- **Churn:** menor nos tiers com hardware instalado e automações ativas (lock-in funcional saudável).
- **Receita de mercado (R3):** **opcional e gradual** — depende da regulação de flexibilidade em BT ([02](02-contexto-regulatorio-mercado-br.md)); não deve ser base do plano de negócio no curto prazo.
- **GD (R4):** receita previsível por UC participante; cresce com o tamanho do programa.

---

## 5. Go-to-market

- **Canais primários:** integradores/EPCs solares (instalam HW e revendem SaaS) e **comercializadoras varejistas** (quando o mercado livre BT abrir — [02](02-contexto-regulatorio-mercado-br.md)).
- **White-label (R5):** permite que o canal use a própria marca sobre o app/portal ([09](09-apps-web-mobile-e-ux.md)).
- **Entrada:** **Smart Lite** (monitoramento) como porta de entrada de baixo atrito → *upsell* para tiers com hardware.
- **GD compartilhada:** parceria com **administradoras de geração compartilhada/cooperativas** (R4).

---

## 6. Decisões em aberto (para o usuário)

1. **Hardware: venda vs locação vs HaaS** (define caixa e barreira de entrada).
2. **Faixa de preço** da assinatura por tier (precisa de pesquisa de disposição a pagar no BR).
3. **Revenue share (R3)** — percentual e gatilho regulatório para ativar.
4. **Fee de GD (R4)** — por UC fixo ou % sobre créditos.
5. **Estratégia de canal** — direto ao consumidor vs B2B2C via instaladores/comercializadoras.

> Quando você definir 1–5, transformo esta proposta em **modelo fechado** com tabela de preços e projeção simples.
