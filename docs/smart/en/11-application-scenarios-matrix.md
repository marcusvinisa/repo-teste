# 11 — Application Scenarios Matrix (LV Brazil) (EN)

> Smart's **18 application scenarios** as a grid of **commercial arrangement × asset level** (3 × 6). Each cell defines assets, minimum hardware/software topology, enabled [modes](10-operation-modes-and-features.md), [integrations](05-integration-and-connectivity.md) and [regulatory](02-regulatory-market-context-br.md) notes. PT-BR source: [`../11-matriz-de-cenarios.md`](../11-matriz-de-cenarios.md).

> **User decision:** the **full 18-cell grid** is adopted (including the "consumption only" N0 cases as full visibility/billing scenarios). Hardware per [06](06-hardware-specification.md): **Smart Gateway** (brain/signal-level control) and **Smart Meter** (commodity, < 1%), in **separate (T1)** or **integrated (T2)** topology.

---

## 1. The two axes

**Commercial arrangements (columns):**
| | Arrangement | Price world |
|---|---|---|
| **A** | Captive (regulated market) | conventional / white / flag tariff |
| **B** | Shared DG (Law 14,300) | regulated tariff **+ SCEE credits + allocation** |
| **C** | Free market (ACL) | contract price / PLD (LV opening by 2027–2028, Law 15,269/2025) |

**Asset levels (rows):** N0 consumption only · N1 +grid PV · N2 +battery (ESS) · N3 +EV charger · N4 +load shifting/load management · N5 +grid services.

---

## 2. Full grid (18 cells)

HW legend: **GW** = Smart Gateway · **+M** = dedicated Smart Meter (T1) or integrated metrology (T2) · **—** = optional/cloud-only.

| Level ↓ \ Arrangement → | **A — Captive** | **B — Shared DG** | **C — Free market** |
|---|---|---|---|
| **N0** consumption only | A0 (—) | B0 (—) | C0 (+M for settlement) |
| **N1** +PV | A1 (— / GW) | B1 (— / GW) | C1 (— / GW) |
| **N2** +battery | A2 (GW) | B2 (GW) | C2 (GW) |
| **N3** +EV | A3 (GW) | B3 (GW) | C3 (GW) |
| **N4** +load shifting | A4 (GW +M) | B4 (GW +M) | C4 (GW +M) |
| **N5** +grid services | A5 (GW +M) | B5 (GW +M) | C5 (GW +M) |

> Per-level **modes** apply across all three arrangements; the arrangement adds the **commercial/regulatory overlay** (price, credits, market).

---

## 3. Per-cell detail (the 18)

| Code | Arrangement + Level | Assets | HW | Main modes ([10](10-operation-modes-and-features.md)) |
|---|---|---|---|---|
| **A0** | Captive · consumption only | meter | — | monitoring, bill/tariff, alarms |
| **A1** | Captive · +PV | +PV | — / GW | self-consumption, zero-export, reactive, IV diagnostics |
| **A2** | Captive · +battery | +ESS | GW | + backup, peak shaving, basic optimization, battery consistency |
| **A3** | Captive · +EV | +EV | GW | + EV smart charging (V1G) |
| **A4** | Captive · +load shifting | +loads/heat pump | GW +M | + load shifting (white/flags), SG-Ready, scenes |
| **A5** | Captive · +grid services | +flexibility | GW +M | + ordered curtailment, voltage/reactive control (DR as regulation evolves) |
| **B0** | Shared DG · consumption only | meter | — | monitoring + **credit allocation/billing** |
| **B1** | Shared DG · +PV | +PV | — / GW | A1 + generation that **creates credits to allocate** |
| **B2** | Shared DG · +battery | +ESS | GW | A2 + store to use credits better |
| **B3** | Shared DG · +EV | +EV | GW | A3 + coordination with credits |
| **B4** | Shared DG · +load shifting | +loads/heat pump | GW +M | A4 + credit-usage optimization |
| **B5** | Shared DG · +grid services | +flexibility | GW +M | A5 + multi-CU aggregation |
| **C0** | Free market · consumption only | settlement meter | +M | monitoring + **CCEE-grade metering** |
| **C1** | Free market · +PV | +PV | — / GW | A1 + injection valued at **market price** |
| **C2** | Free market · +battery | +ESS | GW | **price arbitrage** (charge cheap / discharge expensive) |
| **C3** | Free market · +EV | +EV | GW | EV at market price |
| **C4** | Free market · +load shifting | +loads/heat pump | GW +M | optimization with **full dynamic tariff** (highest gain) |
| **C5** | Free market · +grid services | +flexibility | GW +M | market/flexibility participation (as regulation allows) |

---

## 4. What the arrangement changes (overlay for any level)

| Arrangement | Overlay |
|---|---|
| **A — Captive** | Optimize against **regulated tariff**; load shifting uses **white/flags**; no market settlement |
| **B — Shared DG** | All of A **+ SCEE credit allocation across CUs**, reconciliation, Fio B, [DG Portal](09-web-mobile-apps-and-ux.md)/[billing](08-cloud-platform-and-apis.md); may include **remote generation** (CU with no local PV, only credits) |
| **C — Free market** | Optimize against **contract price/PLD**; **CCEE settlement metering**; **migration** flows; full dynamic tariff boosts load shifting. Progressive enablement (Law 15,269/2025: LV commercial/industrial by Nov/2027, residential by Nov/2028) |

Regulatory detail in [02](02-regulatory-market-context-br.md).

---

## 5. Recommended HW per cell

| Cell | Min HW | Recommended | Why |
|---|---|---|---|
| A0/B0 | none | — | visibility/billing only |
| C0 | Smart Meter | Smart Meter (CCEE-grade) | free-market settlement |
| A1/B1/C1 | none (cloud) | Smart Gateway | local injection/self-consumption control |
| A2/B2/C2 | Smart Gateway | Smart Gateway | backup + deterministic self-consumption |
| A3/B3/C3 | Smart Gateway | Smart Gateway | + EV (OCPP) |
| A4/B4/C4 | Smart Gateway | **Gateway + Smart Meter** | metering for load shifting/peak shaving |
| A5/B5/C5 | **Gateway + Smart Meter** | **Gateway + Smart Meter** | grid services, metering, voltage control |

> HW in [06](06-hardware-specification.md); edge execution in [07](07-firmware-edge-specification.md); when to build each level in [12 — Roadmap](12-roadmap-and-phasing.md).
