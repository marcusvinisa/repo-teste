# 02 — Regulatory & Market Context (Brazil) (EN)

> Map of Brazil's regulatory and commercial environment for **low-voltage (LV, Group B)** electricity, which defines Smart's requirements and limits. Grounds the [scenarios matrix](11-application-scenarios-matrix.md) and the [operation modes](10-operation-modes-and-features.md). Time-sensitive items marked `[TO VERIFY]`. PT-BR source: [`../02-contexto-regulatorio-mercado-br.md`](../02-contexto-regulatorio-mercado-br.md).

---

## 1. Institutional actors

| Acronym | Role |
|---|---|
| **ANEEL** | Regulator — DG rules, tariffs, quality, PRODIST |
| **ONS** | System operator — runs the grid and contracts **ancillary services** |
| **CCEE** | Clearing chamber — accounts and settles the market (regulated & free) |
| **MME / CNPE** | Energy policy (market opening, directives) |
| **DisCo** | Distributor — CU connection, metering, captive billing |
| **Retailer** | Sells energy in the free market, including to small consumers |

---

## 2. The three commercial arrangements

| Arrangement | What it is | Who bills energy | Smart implication |
|---|---|---|---|
| **A — Captive** | Regulated market; CU buys from the local DisCo at the regulated tariff | DisCo | Optimize against **regulated tariff** (conventional/white/flags); focus on self-consumption and load shifting |
| **B — Shared DG** | Distributed generation whose credits are split among several CUs (Law 14,300) | DisCo (with **SCEE** applying credits) | **Allocation** management, generation×consumption reconciliation, credit-usage optimization → [Smart DG](08-cloud-platform-and-apis.md) |
| **C — Free market (ACL)** | CU contracts energy from a retailer, outside the regulated tariff | Retailer + DisCo (wire use) | Optimize against **contract price/PLD**, settlement metering, migration |

---

## 3. Distributed Generation (DG) — Law 14,300/2022 & REN 1,000/2021

**Law 14,300/2022** created the legal framework for micro/mini distributed generation; operational rules are consolidated in **ANEEL REN No. 1,000/2021** (replacing REN 482/2012 and 414/2010), with updates such as **REN 1,059/2023** `[TO VERIFY current version]`.

- **Microgeneration:** installed power **≤ 75 kW**. **Minigeneration:** **> 75 kW** up to **3 MW** `[TO VERIFY]`.
- **Compensation modalities (SCEE):** local self-consumption; **remote self-consumption**; **shared generation** (consortium/cooperative); **EMUC** (multiple-CU developments, e.g., condominiums).

### Credits & "Fio B"
- Injected energy yields **credits** (kWh) to offset consumption (typically 60-month validity).
- Law 14,300 ended full free wire use: for those connected **from 7-Jan-2023 (DG II)**, gradual **TUSD Fio B** charging on **injected energy**, annual ramp **15/30/45/60/75/90%** (2023→2028); from **2029** ANEEL **revises** the methodology (CNPE) — **not** automatically 100%. Those who filed access **by 6-Jan-2023 (DG I)** keep **grandfathering** (Fio B exemption) **until 2045**. **Instantaneous self-consumption is exempt** — only injected energy is charged.

**Product impact:** the savings engine must model per-CU credit, applicable Fio B, credit validity/allocation and the inject-now vs self-consume/store trade-off. See [04](04-domain-and-data-model.md) and [10](10-operation-modes-and-features.md).

---

## 4. Free market (ACL) & LV opening

- Market splits into **ACR** (regulated) and **ACL** (free).
- Since **Jan/2024**, all **Group A** (HV/MV) consumers may migrate to the ACL, possibly served by a **retailer**.
- **LV opening — now with a legal milestone:** **Law No. 15,269/2025 (24-Nov-2025)** started opening the free market to LV. Announced schedule: by **Nov/2027** for LV **commercial & industrial** consumers, and by **Nov/2028** for **residential**. The law creates the **Supplier of Last Resort (SUI)**. ANEEL is preparing the **regulatory improvements** (metering, contracting) toward **2027**. `[TO VERIFY infralegal regulation in progress]`

**Product impact:** arrangement C should be ready to go live **when LV opens**, requiring CCEE-grade settlement metering, contract/PLD modeling instead of regulated tariff, and **migration** flows. Treat as **Phase 2** ([12](12-roadmap-and-phasing.md)).

---

## 5. LV tariff structure (Group B)

| Component | Description | Smart use |
|---|---|---|
| **TUSD** | Distribution system use tariff (wire) | Cost basis; basis for DG Fio B |
| **TE** | Energy tariff | Consumed-energy cost |
| **Conventional tariff** | Single energy price (R$/kWh) | Savings baseline |
| **White tariff** | Optional **ToU** with 3 periods: **peak**, **intermediate**, **off-peak** | Enables **load shifting** and smart charging |
| **Tariff flags** | **green/yellow/red 1 & 2** surcharge per generation cost | Short-term price signal |

> In the captive market there is **no hourly dynamic market tariff** like Europe; the available price signal is **white tariff + flags**. Full dynamic pricing appears only in the **free market** (contract/PLD). The optimizer must support **both worlds** — see [08](08-cloud-platform-and-apis.md) and [10](10-operation-modes-and-features.md).

---

## 6. Grid services in Brazil (level N5)

Unlike Europe (FCR/aFRR open to residential aggregators), in Brazil:

- **Ancillary services** are contracted by **ONS** (frequency control, operating reserve, reactive support, restoration) — historically from large generators.
- **Recent progress (2025–2026):** ANEEL created a **regulatory sandbox** to test **competitive ancillary-services contracting** (first projects in Minas Gerais substations) and **authorized ONS to contract voltage-control ancillary services** (Oct/2025; TSA 2026 ≈ R$ 10.41/Mvar-h). The regulatory agenda includes **observability, operability and controllability of DER**.
- **Smart metering in LV:** ANEEL **Public Consultation No. 001/2026** on **modernizing metering / smart meters** in LV — a key enabler for grid services and residential free market.
- **Storage + revenue stacking:** ANEEL recognizes distributed storage potential (arbitrage, demand response, voltage support). Still, a **broad, paid market for residential LV flexibility** is **under construction** — N5 should be built as **ready technical capability**, monetizing as regulation evolves. `[TO VERIFY final rules]`

**Product impact:** build N5 as ready capability (metering, telemetry, dispatch, aggregation — [08](08-cloud-platform-and-apis.md)) with monetization gated by regulation. Near-term viable: **ordered curtailment**, **voltage/reactive control**, **contracted demand management** — a Brazilian functional analog to Germany's §14a.

---

## 7. Technical norms & certification

- **PRODIST Module 3** — DG access/connection procedures.
- **ABNT NBR 16149/16150** (inverter grid-interface), **16274** (PV system docs/commissioning), **NBR IEC 62116** (anti-islanding), **16690** (PV array installations).
- **INMETRO** — compulsory certification of PV equipment (modules, **inverters**, charge controllers, batteries) under **Ordinance 140/2022**, amended by **515/2023** (emergency disconnection device); scope ≤ 75 kW; since **2-May-2025**, only inverters **> 10 kW** compliant with 140/2022 may be made/imported. *(Applies to the **inverter**, not the Smart Gateway/Meter — see [06](06-hardware-specification.md).)*
- **ANATEL** — mandatory homologation of any RF product (Wi-Fi/BT/4G) — applies to **Smart hardware**.
- **EV / storage:** **NBR IEC 61851** (EV conductive charging) and **62196** (connectors); ESS regulation **under construction** `[TO VERIFY]`.
- **Metering:** DG requires a **bidirectional meter** differentiating **consumed** vs **injected** energy (**PRODIST Module 5**, REN 956/2021). A **billing** meter needs an **INMETRO-approved model** (RTM **Ordinance 587/2012** — classes D 0.2% / C 0.5% / B 1.0% / A 2.0%). The **free market** requires **SMF/CCEE-grade** metering (mass memory 5–60 min for ≥ 32 days, RTC sync to GMT-3, ABNT/IEC) `[TO VERIFY by size]`.

---

## 8. Implications for Smart

1. **Two price worlds:** captive = regulated tariff; free = contract/PLD — engine needs both ([08](08-cloud-platform-and-apis.md)).
2. **Shared DG = allocation + credits + Fio B:** needs multi-CU billing/reconciliation ([08](08-cloud-platform-and-apis.md)).
3. **Grid services = ready capability, gradual monetization:** build N5 without depending on a market that doesn't yet exist in LV ([11](11-application-scenarios-matrix.md)).
4. **Hardware must be born BR-certifiable:** ANATEL + INMETRO(meter) + ABNT from design ([06](06-hardware-specification.md)).
5. **Connection follows PRODIST/ABNT:** the product must **respect** (not bypass) inverter protections (anti-islanding) and injection limits ([07](07-firmware-edge-specification.md)).
