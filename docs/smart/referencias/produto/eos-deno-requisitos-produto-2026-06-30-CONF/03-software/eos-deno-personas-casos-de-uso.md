# EOS-DENO · Personas & Casos de Uso (camada de software)

> **Para que serve:** definir *quem* usa a plataforma e *quais casos de uso* cada um tem — para que o software seja **modularizado em microsserviços** e **personalizável por persona** (cada persona/cenário consome um subconjunto de serviços = um bundle). Duas granularidades convivem: as **personas da cadeia** (atores que operam a plataforma) e a **matriz de cenários do consumidor** (como a necessidade do consumidor varia por ativo × arranjo comercial). Complementa o mapa de hardware — aqui o device é insumo.

---

## 1 · Personas da cadeia (atores da plataforma)

Sete personas, do consumidor à operação da plataforma. `código` usado no mapeamento de serviços (ver `eos-deno-matriz-software.md`). A lista é referência, **não teto** — novas personas (ex.: seguradora, banco, poder concedente) podem entrar.

| Cód | Persona | Quem é | Jobs principais | Casos de uso exclusivos (não-compartilhados) |
|---|---|---|---|---|
| **CON** | Consumidor / Prosumidor | Dono da UC (residencial/PME) — varia pelos 18 cenários | Pagar menos, ter backup, conveniência, transparência | Conta/tarifa, autoconsumo, backup, EV charging, conforto; visão de economia em R$/CO₂ |
| **INT** | Integrador / EPC | Instala, comissiona, faz O&M — **beachhead** | Vender, instalar rápido, dar suporte, escalar carteira | Comissionamento, onboarding de ativos, diagnóstico remoto, RMA, portal multi-cliente |
| **COM** | Comercializadora / Varejista | Vende energia ao consumidor (empresa-âncora adquirindo uma) | Adquirir/reter carteira, faturar, gerir contratos | Gestão de book, billing de energia, gestão de planos/contratos, app white-label, churn/retenção, liquidação CCEE da carteira |
| **AGG** | Agregador / VPP | Agrega DER para mercado/rede | Monetizar flexibilidade da frota | Agregação de portfólio, bidding em mercado, qualificação ancilar, despacho coordenado, medição de baseline, revenue-share |
| **GER** | Gerador | Opera geração (usinas GD, geração compartilhada) | Maximizar geração e valor da energia | Performance de geração, gestão/rateio de créditos (GD), gestão de PPA, monetização de ativo |
| **DSO** | Distribuidor | Operador da rede de distribuição | Operar a rede com segurança e hosting capacity | Sinais de rede (RCR/§14a/DOE), ordens de curtailment, telecontrole, visão de capacidade de hospedagem |
| **ORQ** | Orquestrador / Operador da plataforma | Opera o EOS-DENO em si (pode ser a própria empresa ou tenant) | Rodar a plataforma multi-tenant com SLA | Operação multi-tenant, SLA/uptime, saúde de frota, MLOps, config de plataforma, marketplace de módulos |

**Nota de arquitetura:** a plataforma é **multi-tenant desde a fundação**. A comercializadora (COM) é um *tenant*, não a dona — assim como integradores (INT) e agregadores (AGG) podem ser tenants white-label. O ORQ é o papel que opera a infra compartilhada.

---

## 2 · Matriz dos 18 cenários do consumidor *(das imagens em anexo)*

O consumidor (CON) não é um perfil único — são **18 perfis** definidos por **nível de ativos × arranjo comercial**. Isso dita qual bundle de serviços/HW cada UC consome.

**Eixo 1 — Níveis de ativos (acumulativos):**

| Nível | Acrescenta | Ativos acumulados |
|---|---|---|
| N0 | só consumo | medidor |
| N1 | + PV on-grid | + inversor/PV |
| N2 | + bateria (ESS) | + bateria/PCS |
| N3 | + EV charger | + carregador VE |
| N4 | + load shifting / cargas | + cargas controláveis, bomba |
| N5 | + grid services | + flexibilidade agregável |

**Eixo 2 — Arranjos comerciais:** **A** = Cativo · **B** = GD compartilhada (Lei 14.300) · **C** = Mercado livre (ACL).

**Detalhe por célula (18 cenários):**

| Cód | Arranjo + Nível | Ativos | HW sugerido | Modos principais |
|---|---|---|---|---|
| A0 | Cativo, só consumo | medidor | nenhum (nuvem) | monitoramento, conta/tarifa |
| A1 | Cativo + PV | +PV | — / Gateway | autoconsumo, zero-export, reativo, diagnóstico IV |
| A2 | Cativo + bateria | +ESS | Gateway | + backup, peak shaving, otimização básica |
| A3 | Cativo + EV | +EV | Gateway | + EV smart charging (V1G) |
| A4 | Cativo + load shifting | +cargas/bomba | Gateway/Controller | + load shifting (branca/bandeiras), SG-Ready, cenas |
| A5 | Cativo + grid services | +flexibilidade | Controller | + curtailment por ordem, reativo, (DR futuro) |
| B0 | GD compart., só consumo | medidor | nenhum | monitoramento + **rateio/billing de créditos** |
| B1 | GD compart. + PV | +PV | — / Gateway | A1 + geração que gera créditos a ratear |
| B2 | GD compart. + bateria | +ESS | Gateway | A2 + armazenar p/ usar crédito melhor |
| B3 | GD compart. + EV | +EV | Gateway | A3 + coordenação com créditos |
| B4 | GD compart. + load shifting | +cargas/bomba | Gateway/Controller | A4 + otimização de uso de créditos |
| B5 | GD compart. + grid services | +flexibilidade | Controller | A5 + agregação multi-UC |
| C0 | Mercado livre, só consumo | medidor p/ liquidação | nenhum | monitoramento + medição p/ CCEE |
| C1 | Mercado livre + PV | +PV | — / Gateway | A1 + injeção valorada a preço de mercado |
| C2 | Mercado livre + bateria | +ESS | Gateway | arbitragem de preço (carrega barato/descarrega caro) |
| C3 | Mercado livre + EV | +EV | Gateway | EV por preço de mercado |
| C4 | Mercado livre + load shifting | +cargas/bomba | Gateway/Controller | otimização por **tarifa dinâmica plena** (maior ganho) |
| C5 | Mercado livre + grid services | +flexibilidade | Controller | participação em mercado/flexibilidade (conforme regulação) |

> **Ressalva regulatória (de você, registrada):** *grid services* remunerado em BT (A5/B5/C5) e o mercado livre para BT (coluna C) **ainda dependem de evolução regulatória**. Esses cenários entram como **capacidade técnica pronta, com monetização gradual** — explicitado em cada ficha. (Coerente com o bear case nº4 da spec de hardware: receita de flexibilidade BR é hipótese, não fato.)

---

## 3 · Casos de uso — compartilhados vs exclusivos

### 3.1 · Compartilhados (todas as personas consomem)
Monitoramento/telemetria · saúde de ativos · alertas/notificações · relatórios · autenticação/identidade. → **núcleo comum**: serviços que todo bundle inclui.

### 3.2 · Stack do consumidor por nível de ativo (CON)
Cada nível **acrescenta** casos de uso ao anterior:

| Nível | Casos de uso que entram |
|---|---|
| N0 | Monitoramento, conta/tarifa, (medição p/ CCEE em C) |
| N1 | Autoconsumo, zero-export, controle de reativo, diagnóstico de geração (IV) |
| N2 | Backup/ilhamento, peak shaving, otimização básica, arbitragem (em C) |
| N3 | EV smart charging (V1G), coordenação de carga do VE |
| N4 | Load shifting, SG-Ready (bomba), cenas, otimização por tarifa |
| N5 | Curtailment por ordem, serviços ancilares, agregação (flexibilidade) |

### 3.3 · Casos de uso por arranjo comercial (CON)
- **A — Cativo:** otimização por tarifa branca/bandeiras.
- **B — GD compartilhada:** **rateio de créditos** entre UCs, billing de créditos, otimização de uso de crédito, **agregação multi-UC**.
- **C — Mercado livre:** injeção valorada a preço de mercado, **arbitragem de preço**, **medição p/ CCEE**, otimização por tarifa dinâmica plena.

### 3.4 · Casos de uso exclusivos por persona da cadeia
- **INT —** comissionamento, onboarding de ativos, diagnóstico remoto, RMA, gestão de carteira de clientes.
- **COM —** book de clientes, billing de energia, contratos/planos, app white-label, churn/retenção, liquidação CCEE da carteira.
- **AGG —** agregação de portfólio, bidding, qualificação ancilar (FCR/aFRR/mFRR), despacho coordenado, baseline, revenue-share.
- **GER —** performance de geração, geração/rateio de créditos, PPA, monetização de ativo.
- **DSO —** sinais de rede (RCR/§14a/DOE), ordens de curtailment, telecontrole, capacidade de hospedagem.
- **ORQ —** operação multi-tenant, SLA, saúde de frota, MLOps, config, marketplace.

---

## 4 · Ponte para a modularização (microsserviços)

A consequência direta deste mapa: **cada persona/cenário é um bundle de microsserviços**. Exemplos:
- **CON @ A0** → ingestão + telemetria + app de consumo + billing/tarifa. (Bundle mínimo, sem HW.)
- **CON @ C5** → tudo acima + forecasting + otimização + EMS + DERMS + VPP/mercado + CCEE. (Bundle completo.)
- **INT** → núcleo comum + comissionamento + diagnóstico + fleet + portal.
- **AGG** → núcleo comum + agregação + bidding + ancilares + despacho.
- **COM** → núcleo comum + book + billing + white-label + churn + CCEE.

Isso é o que permite **personalizar o produto por persona** sem reescrevê-lo: ativar/desativar serviços. O catálogo de microsserviços e o mapeamento persona × serviço estão em **`eos-deno-matriz-software.md`**.

---

*Personas e casos de uso · camada de software · Projeto EOS-DENO. A matriz dos 18 cenários vem das imagens fornecidas. Lista é referência, não teto.*
