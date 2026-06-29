# 11 — Matriz de Cenários de Aplicação (BT Brasil)

> Os **18 cenários** de aplicação do Smart, como uma grade **arranjo comercial × nível de ativos** (3 × 6). Cada célula define ativos, topologia mínima de hardware/software, [modos habilitados](10-modos-de-operacao-e-features.md), [integrações](05-integracao-e-conectividade.md) e notas [regulatórias](02-contexto-regulatorio-mercado-br.md).

> **Decisão do usuário:** adotamos a **grade completa de 18 células** (incluindo os casos "só consumo" N0 como cenários plenos de visibilidade/billing). Hardware referenciado conforme [06](06-especificacao-hardware.md): **Smart Gateway** (cérebro/controle por sinal) e **Smart Meter** (medição *commodity* < 1%), em topologia **separada (T1)** ou **integrada (T2)**.

---

## 1. Os dois eixos

**Arranjos comerciais (colunas):**
| | Arranjo | Mundo de preço |
|---|---|---|
| **A** | Cativo (mercado regulado) | tarifa convencional / branca / bandeiras |
| **B** | GD compartilhada (Lei 14.300) | tarifa regulada **+ créditos SCEE + rateio** |
| **C** | Mercado livre (ACL) | preço de contrato / PLD (BT abrindo até 2027–2028, Lei 15.269/2025) |

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

## 2. Grade completa (18 células)

Legenda HW: **GW** = Smart Gateway · **+M** = Smart Meter dedicado (T1) ou metrologia integrada (T2) · **—** = opcional/só nuvem.

| Nível ↓ \ Arranjo → | **A — Cativo** | **B — GD compartilhada** | **C — Mercado livre** |
|---|---|---|---|
| **N0** só consumo | A0 (—) | B0 (—) | C0 (+M p/ liquidação) |
| **N1** +PV | A1 (— / GW) | B1 (— / GW) | C1 (— / GW) |
| **N2** +bateria | A2 (GW) | B2 (GW) | C2 (GW) |
| **N3** +EV | A3 (GW) | B3 (GW) | C3 (GW) |
| **N4** +load shifting | A4 (GW +M) | B4 (GW +M) | C4 (GW +M) |
| **N5** +grid services | A5 (GW +M) | B5 (GW +M) | C5 (GW +M) |

> Os **modos por nível** valem nos três arranjos; o arranjo adiciona a **camada comercial/regulatória** (preço, créditos, mercado).

---

## 3. Detalhe por célula (as 18)

| Cód. | Arranjo + Nível | Ativos | HW | Modos principais ([10](10-modos-de-operacao-e-features.md)) |
|---|---|---|---|---|
| **A0** | Cativo · só consumo | medidor | — | monitoramento, conta/tarifa, alarmes |
| **A1** | Cativo · +PV | +PV | — / GW | autoconsumo, zero-export, reativo, diagnóstico IV |
| **A2** | Cativo · +bateria | +ESS | GW | + backup, peak shaving, otimização básica, consistência bateria |
| **A3** | Cativo · +EV | +EV | GW | + EV smart charging (V1G) |
| **A4** | Cativo · +load shifting | +cargas/bomba | GW +M | + load shifting (branca/bandeiras), SG-Ready, cenas |
| **A5** | Cativo · +grid services | +flexibilidade | GW +M | + curtailment por ordem, controle de tensão/reativo (DR conforme regulação) |
| **B0** | GD compart. · só consumo | medidor | — | monitoramento + **rateio/billing de créditos** |
| **B1** | GD compart. · +PV | +PV | — / GW | A1 + geração que **gera créditos a ratear** |
| **B2** | GD compart. · +bateria | +ESS | GW | A2 + armazenar p/ usar crédito melhor |
| **B3** | GD compart. · +EV | +EV | GW | A3 + coordenação com créditos |
| **B4** | GD compart. · +load shifting | +cargas/bomba | GW +M | A4 + otimização de uso de créditos |
| **B5** | GD compart. · +grid services | +flexibilidade | GW +M | A5 + agregação multi-UC |
| **C0** | Mercado livre · só consumo | medidor p/ liquidação | +M | monitoramento + **medição apta à CCEE** |
| **C1** | Mercado livre · +PV | +PV | — / GW | A1 + injeção valorada a **preço de mercado** |
| **C2** | Mercado livre · +bateria | +ESS | GW | **arbitragem de preço** (carrega barato / descarrega caro) |
| **C3** | Mercado livre · +EV | +EV | GW | EV por preço de mercado |
| **C4** | Mercado livre · +load shifting | +cargas/bomba | GW +M | otimização por **tarifa dinâmica plena** (maior ganho) |
| **C5** | Mercado livre · +grid services | +flexibilidade | GW +M | participação em mercado/flexibilidade (conforme regulação) |

---

## 4. O que o arranjo muda (overlay comum a qualquer nível)

| Arranjo | Overlay |
|---|---|
| **A — Cativo** | Otimização contra **tarifa regulada**; load shifting usa **branca/bandeiras**; sem liquidação de mercado |
| **B — GD compartilhada** | Tudo de A **+ rateio de créditos SCEE entre UCs**, conciliação, Fio B, [Portal GD](09-apps-web-mobile-e-ux.md)/[billing](08-plataforma-cloud-e-apis.md); pode haver **geração remota** (UC sem PV local, só créditos) |
| **C — Mercado livre** | Otimização contra **preço de contrato/PLD**; **medição para liquidação CCEE**; fluxos de **migração**; tarifa dinâmica plena potencializa load shifting/otimização. Habilitação progressiva (Lei 15.269/2025: BT comercial/industrial até nov/2027, residencial até nov/2028) |

> Detalhes regulatórios de cada overlay em [02](02-contexto-regulatorio-mercado-br.md).

---

## 5. Fichas por nível (válidas nos 3 arranjos)

### N0 — Só consumo
- **Ativos:** medidor. **Topologia:** só-nuvem `[SW]` (em C, **Smart Meter** apto à liquidação).
- **Modos:** [monitoramento](10-modos-de-operacao-e-features.md) (#1); em B, [rateio/billing](10-modos-de-operacao-e-features.md) (#16); em C, medição CCEE.
- **Valor:** visibilidade de consumo, conta, alarmes; em B, gestão de créditos; em C, base para contrato.
- **Persona:** morador / gestor GD.

### N1 — + PV on-grid
- **Ativos:** inversor/PV (+medidor). **Topologia:** só-nuvem (API do fabricante) **ou** **Smart Gateway** p/ controle local.
- **Modos:** monitoramento (#1), **autoconsumo** (#2), **zero-export/limite de injeção** (#5), **controle de reativo** (#14), **diagnóstico IV/AI Health** (#19), config remota/OTA (#17/#18).
- **Integração:** Modbus/SunSpec local ou conector cloud ([05](05-integracao-e-conectividade.md)).
- **Overlay:** A=abate tarifa; B=gera créditos a ratear; C=injeção a preço de mercado.

### N2 — + bateria (ESS)
- **Ativos:** + bateria/PCS (inversor híbrido). **Topologia:** **Smart Gateway**.
- **Modos:** N1 + **backup/ilhamento** (#3, transferência por sinal → ATS externo), **peak shaving** (#4, melhor com Smart Meter), **otimização** (#7), **consistência de bateria** (#19).
- **Overlay:** B armazena p/ usar crédito melhor; C arbitra preço.

### N3 — + EV charger
- **Ativos:** + carregador VE (OCPP). **Topologia:** **Smart Gateway**.
- **Modos:** N2 + **EV smart charging V1G** (#8), automações (#12); **V2H/V2G** (#9) como futuro `[VERIFICAR BR]`.
- **Integração:** **OCPP 1.6/2.0.1** ([05](05-integracao-e-conectividade.md)).
- **Overlay:** A usa branca/fora-ponta; C usa preço de mercado; B coordena com créditos.

### N4 — + load shifting / gestão de cargas
- **Ativos:** + cargas controláveis (smart plug/relé), bomba SG-Ready. **Topologia:** **Smart Gateway + Smart Meter** (T1 ou T2 integrado) — exige medição para deslocar com precisão.
- **Modos:** N3 + **load shifting** (#6), **otimização por preço + forecast** (#7), **bomba SG-Ready** (#10), **gestão de cargas** (#11), **cenas** (#12).
- **Overlay:** A=branca/bandeiras como sinal; C=tarifa dinâmica plena (maior ganho); B=otimiza uso de créditos.

### N5 — + grid services
- **Ativos:** flexibilidade agregável + **medição** robusta (Smart Meter). **Topologia:** **Smart Gateway + Smart Meter**.
- **Modos:** N4 + **grid services/VPP** (#13), **curtailment por ordem (estilo §14a)** (#15), **controle de tensão/reativo** (#14).
- **Integração:** IEEE 2030.5/CSIP, agregação na nuvem ([08](08-plataforma-cloud-e-apis.md)).
- **Valor:** **capacidade técnica pronta**; monetização **gradual** no Brasil — hoje viável: curtailment, **controle de tensão** (ONS autorizado, 2025), reativo, demanda; futuro: mercados de flexibilidade/DR ([02](02-contexto-regulatorio-mercado-br.md)).
- **Overlay:** A/B respondem a ordens da distribuidora + reativo; C participa de mercado conforme a regulação evoluir.

---

## 6. Topologia/HW recomendado por célula

| Célula | HW mínimo | Recomendado | Por quê |
|---|---|---|---|
| A0/B0 | nenhum | — | só visibilidade/billing |
| C0 | Smart Meter | Smart Meter (apto CCEE) | liquidação no mercado livre |
| A1/B1/C1 | nenhum (cloud) | Smart Gateway | controle local de injeção/autoconsumo |
| A2/B2/C2 | Smart Gateway | Smart Gateway | backup + autoconsumo determinístico |
| A3/B3/C3 | Smart Gateway | Smart Gateway | + EV (OCPP) |
| A4/B4/C4 | Smart Gateway | **Gateway + Smart Meter** | medição p/ load shifting/peak shaving |
| A5/B5/C5 | **Gateway + Smart Meter** | **Gateway + Smart Meter** | grid services, medição, controle de tensão |

> HW em [06](06-especificacao-hardware.md); execução dos modos no edge em [07](07-especificacao-firmware-edge.md); quando construir cada nível em [12 — Roadmap](12-roadmap-e-faseamento.md).
