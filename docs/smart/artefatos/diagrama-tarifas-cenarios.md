# Artefato — Diagramas de Tarifas e Cenários

> Diagramas (mermaid) que detalham o **mundo de preços** brasileiro e como ele se conecta à [matriz de cenários](../11-matriz-de-cenarios.md) e aos [modos de operação](../10-modos-de-operacao-e-features.md). Complementa [02](../02-contexto-regulatorio-mercado-br.md) e [04](../04-modelo-de-dominio-e-dados.md).

---

## 1. Tipos de tarifa por arranjo

```mermaid
flowchart TB
  uc[UC de baixa tensão]
  uc --> cat[Cativo]
  uc --> gd[GD compartilhada]
  uc --> ml[Mercado livre]

  cat --> conv[Convencional - monômia]
  cat --> branca[Tarifa Branca - ToU: ponta/intermediário/fora-ponta]
  cat --> band[Bandeiras: verde/amarela/vermelha 1 e 2]

  gd --> creditos[Créditos SCEE + rateio + Fio B]
  gd --> cat2[Sobre tarifa regulada do cativo]

  ml --> contrato[Preço de contrato]
  ml --> pld[PLD / exposição de curto prazo]
```

---

## 2. Sinal de preço → modo de operação

```mermaid
flowchart LR
  subgraph Sinais
    s1[Tarifa branca / ponta]
    s2[Bandeira vermelha]
    s3[Preço dinâmico alto - ML]
    s4[Excedente PV]
    s5[Preço baixo / fora-ponta]
  end
  s1 --> m1[Load shifting: evitar ponta]
  s2 --> m1
  s3 --> m2[Descarregar bateria / vender]
  s4 --> m3[Autoconsumo + carregar bateria/EV]
  s5 --> m4[Carregar bateria/EV / cargas diferíveis]
  m1 --> opt[Otimizador - plano]
  m2 --> opt
  m3 --> opt
  m4 --> opt
  opt --> edge[Edge executa]
```

> Modos referenciados em [10 — Modos de Operação](../10-modos-de-operacao-e-features.md) (#6 load shifting, #7 otimização, #2 autoconsumo, #8 EV).

---

## 3. Alavancas de valor por nível de ativo

```mermaid
flowchart TB
  N1[N1 +PV] --> v1[Autoconsumo / abate tarifa]
  N2[N2 +Bateria] --> v2[Backup + arbitragem/ponta]
  N3[N3 +EV] --> v3[Carga inteligente com excedente/preço]
  N4[N4 +Load shifting] --> v4[Otimização multi-carga por preço/forecast]
  N5[N5 +Grid services] --> v5[Curtailment/reativo/controle de tensão + (futuro) flexibilidade remunerada]
  v1 --> roi[Economia / Receita]
  v2 --> roi
  v3 --> roi
  v4 --> roi
  v5 --> roi
```

---

## 4. Fio B (rampa de cobrança — GD II)

```mermaid
flowchart LR
  a2023[2023: 15%] --> a2024[2024: 30%] --> a2025[2025: 45%] --> a2026[2026: 60%] --> a2027[2027: 75%] --> a2028[2028: 90%] --> a2029[2029: ANEEL revisa metodologia]
```

> Incide sobre o **TUSD Fio B** da **energia injetada**; **autoconsumo instantâneo é isento**. GD I (≤ 6/jan/2023) isenta até 2045. Ver [02](../02-contexto-regulatorio-mercado-br.md).
