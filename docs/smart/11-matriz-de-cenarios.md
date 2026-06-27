# 11 — Matriz de Cenários de Aplicação (BT Brasil)

> Os cenários de aplicação do Smart, como uma grade **arranjo comercial × nível de ativos**. Cada célula define ativos presentes, topologia mínima de hardware/software, [modos habilitados](10-modos-de-operacao-e-features.md), [integrações](05-integracao-e-conectividade.md) e notas [regulatórias](02-contexto-regulatorio-mercado-br.md).

---

## 1. Os dois eixos

**Arranjos comerciais (colunas):**
| | Arranjo | Mundo de preço |
|---|---|---|
| **A** | Cativo (mercado regulado) | tarifa convencional / branca / bandeiras |
| **B** | GD compartilhada (Lei 14.300) | tarifa regulada **+ créditos SCEE + rateio** |
| **C** | Mercado livre (ACL) | preço de contrato / PLD |

**Níveis de ativos (linhas):**
| Nível | Acrescenta | Ativos acumulados |
|---|---|---|
| **N0** | (nada) só consumo | medidor |
| **N1** | + PV on-grid | + inversor/PV |
| **N2** | + bateria (ESS) | + bateria/PCS |
| **N3** | + EV charger | + carregador VE |
| **N4** | + load shifting / gestão de cargas | + cargas controláveis, bomba |
| **N5** | + grid services | + flexibilidade agregável |

---

## 2. Reconciliação: 15 vs 18 células `[VERIFICAR — confirmar com o usuário]`

A grade completa é **3 arranjos × 6 níveis = 18 células**. Você indicou **15 cenários verdadeiros**.

**Reconciliação proposta (a mais limpa):** os **15 cenários núcleo** são **N1–N5 × {A,B,C}** = 5 níveis de ativos × 3 arranjos = **15**. As **3 células N0** (só consumo, sem ativo controlável/gerador — uma para cada arranjo) ficam como **linha-base de visibilidade/billing**, fora dos 15 cenários do produto de **controle** (afinal, um EMS/HEMS sem ativo a gerenciar só monitora/fatura).

> Ou seja: a contagem 15 bate exatamente quando excluímos os três casos "só consumo". **Confirme** se é esta a intenção; caso queira manter os N0 como cenários plenos, a grade vira 18. Registrado também em [13](13-gaps-riscos-e-decisoes.md).

---

## 3. Grade completa (18 células; 15 núcleo destacados)

Legenda: ✅ = cenário núcleo (1 dos 15) · ▫️ = baseline (N0, visibilidade/billing) · HW sugerido: **G**=Gateway, **C**=Controller, **—**=opcional/nuvem.

| Nível ↓ \ Arranjo → | **A — Cativo** | **B — GD compartilhada** | **C — Mercado livre** |
|---|---|---|---|
| **N0** só consumo | ▫️ A0 (—) | ▫️ B0 (—) | ▫️ C0 (—) |
| **N1** +PV | ✅ A1 (— / G) | ✅ B1 (— / G) | ✅ C1 (— / G) |
| **N2** +bateria | ✅ A2 (G) | ✅ B2 (G) | ✅ C2 (G) |
| **N3** +EV | ✅ A3 (G) | ✅ B3 (G) | ✅ C3 (G) |
| **N4** +load shifting | ✅ A4 (G/C) | ✅ B4 (G/C) | ✅ C4 (G/C) |
| **N5** +grid services | ✅ A5 (C) | ✅ B5 (C) | ✅ C5 (C) |

**15 núcleo = todas as células N1–N5.** Os modos por nível valem nos três arranjos; o arranjo adiciona a **camada comercial/regulatória** (preço, créditos, mercado).

---

## 4. O que o arranjo muda (overlay comum a todos os níveis)

| Arranjo | Overlay sobre qualquer nível N1–N5 |
|---|---|
| **A — Cativo** | Otimização contra **tarifa regulada**; load shifting usa **branca/bandeiras**; sem liquidação de mercado |
| **B — GD compartilhada** | Tudo de A **+ rateio de créditos SCEE entre UCs**, conciliação, Fio B, [Portal GD](09-apps-web-mobile-e-ux.md)/[billing](08-plataforma-cloud-e-apis.md); pode haver **geração remota** (UC sem PV local mas com créditos) |
| **C — Mercado livre** | Otimização contra **preço de contrato/PLD**; **medição para liquidação CCEE**; fluxos de migração; tarifa dinâmica plena habilita melhor o load shifting/otimização |

> Detalhes regulatórios de cada overlay em [02](02-contexto-regulatorio-mercado-br.md).

---

## 5. Fichas por nível (válidas nos 3 arranjos)

### N0 — Só consumo (baseline) ▫️
- **Ativos:** medidor. **Topologia:** só-nuvem `[SW]` (ou leitura de medidor).
- **Modos:** [monitoramento](10-modos-de-operacao-e-features.md) (#1); em B, [rateio/billing](10-modos-de-operacao-e-features.md) (#16).
- **Valor:** visibilidade de consumo, conta, alarmes; em B, gestão de créditos.
- **Persona:** morador / gestor GD. **Fora dos 15** (sem ativo a controlar).

### N1 — + PV on-grid ✅ (A1, B1, C1)
- **Ativos:** inversor/PV (+medidor). **Topologia:** só-nuvem (via API do fabricante) **ou** Gateway para controle local.
- **Modos:** monitoramento (#1), **autoconsumo** (#2, se houver carga local), **zero-export/limite de injeção** (#5), **controle de reativo** (#14), **diagnóstico IV/AI Health** (#19), config remota/OTA (#17/#18).
- **Integração:** Modbus/SunSpec local ou conector cloud ([05](05-integracao-e-conectividade.md)).
- **Valor:** maximizar uso da geração, conformidade de injeção, O&M.
- **Overlay:** A=abate tarifa; B=gera créditos a ratear; C=injeção valorada a preço de mercado.

### N2 — + bateria (ESS) ✅ (A2, B2, C2)
- **Ativos:** + bateria/PCS (inversor híbrido). **Topologia:** **Gateway** recomendado (controle local).
- **Modos:** N1 + **backup/ilhamento** (#3), **peak shaving** (#4, melhor com Controller/CT), **otimização** básica (#7), **consistência de bateria** (#19).
- **Valor:** backup, mais autoconsumo, alívio de ponta.
- **Overlay:** B armazena para usar crédito melhor; C arbitra preço (carrega barato/descarrega caro).

### N3 — + EV charger ✅ (A3, B3, C3)
- **Ativos:** + carregador VE (OCPP). **Topologia:** **Gateway**.
- **Modos:** N2 + **EV smart charging V1G** (#8), automações (#12); **V2H/V2G** (#9) como futuro `[VERIFICAR BR]`.
- **Integração:** **OCPP 1.6/2.0.1** ([05](05-integracao-e-conectividade.md)).
- **Valor:** carregar com excedente PV / horário barato sem estourar a casa.
- **Overlay:** A usa branca/fora-ponta; C usa preço de mercado; B coordena com créditos.

### N4 — + load shifting / gestão de cargas ✅ (A4, B4, C4)
- **Ativos:** + cargas controláveis (smart plug/relé), bomba SG-Ready. **Topologia:** **Gateway** ou **Controller** (se precisar de medição/relés de potência).
- **Modos:** N3 + **load shifting** (#6), **otimização por preço + forecast** (#7), **bomba SG-Ready** (#10), **gestão de cargas** (#11), **cenas** (#12).
- **Integração:** EEBus/SG-Ready, smart plugs ([05](05-integracao-e-conectividade.md)).
- **Valor:** deslocar consumo para barato/excedente; conforto automatizado.
- **Overlay:** A=tarifa branca/bandeiras como sinal; C=tarifa dinâmica plena (maior ganho); B=otimiza uso de créditos.

### N5 — + grid services ✅ (A5, B5, C5)
- **Ativos:** flexibilidade agregável + **medição** robusta. **Topologia:** **Controller** (CT, relés, 4G, backup).
- **Modos:** N4 + **grid services/VPP** (#13), **curtailment por ordem (estilo §14a)** (#15), **controle de reativo** (#14).
- **Integração:** IEEE 2030.5/CSIP, agregação na nuvem ([08](08-plataforma-cloud-e-apis.md)).
- **Valor:** **capacidade técnica pronta**; monetização **gradual** no Brasil ([02](02-contexto-regulatorio-mercado-br.md)). Hoje: curtailment/reativo/demanda; futuro: mercados de flexibilidade.
- **Overlay:** A/B respondem a ordens da distribuidora + reativo; C participa de mercado/contratos de flexibilidade conforme regulação evoluir.

---

## 6. Resumo de topologia/HW recomendado por célula

| Célula | HW mínimo | HW recomendado | Por quê |
|---|---|---|---|
| A0/B0/C0 | nenhum | — | só visibilidade/billing |
| A1/B1/C1 | nenhum (cloud) | Gateway | controle local de injeção/autoconsumo |
| A2/B2/C2 | Gateway | Gateway | backup + autoconsumo determinístico |
| A3/B3/C3 | Gateway | Gateway | + EV (OCPP) |
| A4/B4/C4 | Gateway | **Controller** se precisa CT/relés | medição + cargas de potência |
| A5/B5/C5 | **Controller** | **Controller** | grid services, medição, 4G, backup |

> HW em [06](06-especificacao-hardware.md); execução dos modos no edge em [07](07-especificacao-firmware-edge.md); planejamento de quando construir cada nível em [12 — Roadmap](12-roadmap-e-faseamento.md).
