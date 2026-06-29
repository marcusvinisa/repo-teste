# EOS-DENO · Personas & Casos de Uso (camada de software)

> **Estudo de referência curado pelo usuário.** Reproduzido em `referencias/`. Ver [00-absorcao-e-ajustes.md](00-absorcao-e-ajustes.md).

> **Para que serve:** definir *quem* usa a plataforma e *quais casos de uso* cada um tem — para que o software seja **modularizado em microsserviços** e **personalizável por persona** (cada persona/cenário consome um subconjunto de serviços = um bundle). Duas granularidades: as **personas da cadeia** (atores que operam a plataforma) e a **matriz de cenários do consumidor** (como a necessidade varia por ativo × arranjo comercial).

---

## 1 · Personas da cadeia (atores da plataforma)

Sete personas, do consumidor à operação da plataforma. Lista é referência, **não teto** (seguradora, banco, poder concedente podem entrar).

| Cód | Persona | Quem é | Jobs principais | Casos de uso exclusivos |
|---|---|---|---|---|
| **CON** | Consumidor / Prosumidor | Dono da UC (residencial/PME) — varia pelos 18 cenários | Pagar menos, backup, conveniência, transparência | Conta/tarifa, autoconsumo, backup, EV charging, conforto; economia R$/CO₂ |
| **INT** | Integrador / EPC | Instala, comissiona, faz O&M — **beachhead** | Vender, instalar rápido, suportar, escalar carteira | Comissionamento, onboarding de ativos, diagnóstico remoto, RMA, portal multi-cliente |
| **COM** | Comercializadora / Varejista | Vende energia ao consumidor | Adquirir/reter carteira, faturar, gerir contratos | Book, billing de energia, planos/contratos, app white-label, churn/retenção, liquidação CCEE da carteira |
| **AGG** | Agregador / VPP | Agrega DER para mercado/rede | Monetizar flexibilidade da frota | Agregação de portfólio, bidding, qualificação ancilar, despacho coordenado, baseline, revenue-share |
| **GER** | Gerador | Opera geração (usinas GD, geração compartilhada) | Maximizar geração e valor da energia | Performance de geração, gestão/rateio de créditos (GD), PPA, monetização de ativo |
| **DSO** | Distribuidor | Operador da rede de distribuição | Operar a rede com segurança e hosting capacity | Sinais de rede (RCR/§14a/DOE), ordens de curtailment, telecontrole, capacidade de hospedagem |
| **ORQ** | Orquestrador / Operador da plataforma | Opera o EOS-DENO em si | Rodar a plataforma multi-tenant com SLA | Operação multi-tenant, SLA/uptime, saúde de frota, MLOps, config, marketplace |

**Nota de arquitetura:** a plataforma é **multi-tenant desde a fundação**. A comercializadora (COM) é um *tenant*, não a dona — assim como integradores (INT) e agregadores (AGG) podem ser tenants white-label. O ORQ opera a infra compartilhada.

---

## 2 · Matriz dos 18 cenários do consumidor

O consumidor (CON) não é um perfil único — são **18 perfis** por **nível de ativos × arranjo comercial**.

**Níveis de ativos (acumulativos):** N0 só consumo (medidor) · N1 +PV · N2 +bateria (ESS) · N3 +EV charger · N4 +load shifting/cargas · N5 +grid services.

**Arranjos:** **A** Cativo · **B** GD compartilhada (Lei 14.300) · **C** Mercado livre (ACL).

| Cód | Arranjo + Nível | Ativos | HW sugerido | Modos principais |
|---|---|---|---|---|
| A0 | Cativo, só consumo | medidor | nenhum (nuvem) | monitoramento, conta/tarifa |
| A1 | Cativo + PV | +PV | — / Gateway | autoconsumo, zero-export, reativo, diagnóstico IV |
| A2 | Cativo + bateria | +ESS | Gateway | + backup, peak shaving, otimização básica |
| A3 | Cativo + EV | +EV | Gateway | + EV smart charging (V1G) |
| A4 | Cativo + load shifting | +cargas/bomba | Gateway (+Meter) | + load shifting (branca/bandeiras), SG-Ready, cenas |
| A5 | Cativo + grid services | +flexibilidade | Gateway+Meter | + curtailment por ordem, reativo, (DR futuro) |
| B0 | GD compart., só consumo | medidor | nenhum | monitoramento + **rateio/billing de créditos** |
| B1 | GD compart. + PV | +PV | — / Gateway | A1 + geração que gera créditos a ratear |
| B2 | GD compart. + bateria | +ESS | Gateway | A2 + armazenar p/ usar crédito melhor |
| B3 | GD compart. + EV | +EV | Gateway | A3 + coordenação com créditos |
| B4 | GD compart. + load shifting | +cargas/bomba | Gateway (+Meter) | A4 + otimização de uso de créditos |
| B5 | GD compart. + grid services | +flexibilidade | Gateway+Meter | A5 + agregação multi-UC |
| C0 | Mercado livre, só consumo | medidor p/ liquidação | Meter | monitoramento + medição p/ CCEE |
| C1 | Mercado livre + PV | +PV | — / Gateway | A1 + injeção valorada a preço de mercado |
| C2 | Mercado livre + bateria | +ESS | Gateway | arbitragem de preço |
| C3 | Mercado livre + EV | +EV | Gateway | EV por preço de mercado |
| C4 | Mercado livre + load shifting | +cargas/bomba | Gateway (+Meter) | otimização por **tarifa dinâmica plena** |
| C5 | Mercado livre + grid services | +flexibilidade | Gateway+Meter | participação em mercado/flexibilidade (conforme regulação) |

> **Ressalva regulatória:** *grid services* remunerado em BT (A5/B5/C5) e o mercado livre BT (coluna C) **dependem de evolução regulatória** — entram como **capacidade técnica pronta, monetização gradual**.
> *(Nomenclatura de HW harmonizada com a suite Smart: Gateway = controle por sinal; Meter = medidor commodity; sem SKU "Controller".)*

---

## 3 · Casos de uso — compartilhados vs exclusivos

### 3.1 · Compartilhados (todas as personas)
Monitoramento/telemetria · saúde de ativos · alertas/notificações · relatórios · autenticação/identidade → **núcleo comum**.

### 3.2 · Stack do consumidor por nível (CON)
| Nível | Casos de uso que entram |
|---|---|
| N0 | Monitoramento, conta/tarifa, (medição p/ CCEE em C) |
| N1 | Autoconsumo, zero-export, controle de reativo, diagnóstico de geração (IV) |
| N2 | Backup/ilhamento, peak shaving, otimização básica, arbitragem (em C) |
| N3 | EV smart charging (V1G), coordenação de carga do VE |
| N4 | Load shifting, SG-Ready (bomba), cenas, otimização por tarifa |
| N5 | Curtailment por ordem, serviços ancilares, agregação (flexibilidade) |

### 3.3 · Casos de uso por arranjo (CON)
- **A — Cativo:** otimização por tarifa branca/bandeiras.
- **B — GD compartilhada:** rateio de créditos entre UCs, billing de créditos, otimização de uso de crédito, agregação multi-UC.
- **C — Mercado livre:** injeção valorada a preço de mercado, arbitragem de preço, medição p/ CCEE, otimização por tarifa dinâmica plena.

### 3.4 · Casos de uso exclusivos por persona
- **INT** — comissionamento, onboarding de ativos, diagnóstico remoto, RMA, gestão de carteira.
- **COM** — book de clientes, billing de energia, contratos/planos, app white-label, churn/retenção, liquidação CCEE da carteira.
- **AGG** — agregação de portfólio, bidding, qualificação ancilar (FCR/aFRR/mFRR), despacho coordenado, baseline, revenue-share.
- **GER** — performance de geração, geração/rateio de créditos, PPA, monetização de ativo.
- **DSO** — sinais de rede (RCR/§14a/DOE), ordens de curtailment, telecontrole, capacidade de hospedagem.
- **ORQ** — operação multi-tenant, SLA, saúde de frota, MLOps, config, marketplace.

---

## 4 · Ponte para a modularização (microsserviços)
**Cada persona/cenário é um bundle de microsserviços.** Exemplos:
- **CON @ A0** → ingestão + telemetria + app de consumo + billing/tarifa. (Bundle mínimo, sem HW.)
- **CON @ C5** → tudo acima + forecasting + otimização + EMS + DERMS + VPP/mercado + CCEE. (Bundle completo.)
- **INT** → núcleo comum + comissionamento + diagnóstico + fleet + portal.
- **AGG** → núcleo comum + agregação + bidding + ancilares + despacho.
- **COM** → núcleo comum + book + billing + white-label + churn + CCEE.

Ativar/desativar serviços em vez de reescrever o produto. Catálogo em [eos-deno-matriz-software.md](eos-deno-matriz-software.md).

---

*Personas e casos de uso · camada de software · Projeto EOS-DENO. Lista é referência, não teto.*
