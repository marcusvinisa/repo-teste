# 01 — Vision & PRD (EN)

> Requirements and vision for **Smart**, a single residential/small-scale energy-management product (EMS/HEMS) that unifies cloud, apps and proprietary hardware under one brand, **vendor-agnostic**, for low-voltage consumer units in Brazil. PT-BR source: [`../01-visao-e-prd.md`](../01-visao-e-prd.md).

---

## 1. Context & problem

Two tool categories exist today that **don't work well together** and leave gaps:

1. **Manufacturer cloud portals/apps** (e.g., GoodWe SEMS+). Great to **monitor** and **remotely configure** **that brand's** assets, but: locked to one brand; cloud-dependent (no cloud, no control); no low-latency **deterministic local control**; shallow orchestration of **third-party loads** (EV, heat pump, plugs).
2. **Hardware gateways** (e.g., EzManager3000). Bring local control and load integration, but: rigid asset-count limits; strong tie to the vendor ecosystem; market/optimization intelligence centered on European dynamic tariffs, not Brazil.

### What Smart does that neither does alone

| Gap | Smart's answer |
|---|---|
| Per-brand silo | **Device Abstraction Layer (DAL)** with local drivers + multi-brand cloud connectors → [05](05-integration-and-connectivity.md) |
| "App or hardware" | **Mixed topology**: each function runs in the right layer (`[SW]`/`[SW+HW]`/`[HW]`/`[BOTH]`) |
| No offline control | **Edge-first** with local fail-safe → [07](07-firmware-edge-specification.md) |
| European context | **15+ Brazilian scenarios** (captive / shared DG / free market) → [11](11-application-scenarios-matrix.md) |
| Home → grid | Same product scales to **VPP/grid services and shared DG** → [08](08-cloud-platform-and-apis.md) |

---

## 2. Value proposition

> **"One product to see, control and monetize all of a consumer unit's energy — any brand, with or without cloud."**

1. **Savings & autonomy** — maximize self-consumption, shift loads to cheap hours, cut the bill (white/ToU/dynamic tariff/flags), reliable backup.
2. **Agnostic & future-proof** — works with multi-brand inverters, batteries, EV chargers, heat pumps and loads.
3. **Market-ready** — enables shared DG (credit allocation), free-market migration, and future grid-services/VPP participation without changing platforms.

---

## 3. Personas & jobs-to-be-done

| Persona | Who | Jobs | Primary surface |
|---|---|---|---|
| **Homeowner** (primary) | LV residential/small-business owner | "Pay less, have backup, control my home simply" | Mobile app |
| **Installer/integrator** (primary) | EPC, solar integrator, O&M | "Commission fast, monitor a fleet, configure/update remotely" | Web Pro |
| **Retailer/aggregator (VPP)** (advanced) | Retailer, flexibility aggregator | "Aggregate and dispatch flexibility, bill services" | Web Pro + API |
| **Shared-DG manager** (advanced) | Shared-generation/cooperative admin | "Allocate credits across CUs and reconcile" | DG Portal |

Roles & permissions in [08](08-cloud-platform-and-apis.md); flows per persona in [09](09-web-mobile-apps-and-ux.md).

---

## 4. Product principles

1. **Agnostic by design** — every integration goes through the DAL.
2. **Right layer for each function** — critical/offline control at the edge; heavy intelligence and aggregation in the cloud; experience in the app.
3. **Hybrid, not either/or** — local **and** cloud-to-cloud coexist; Smart picks the best path per asset ([05](05-integration-and-connectivity.md)).
4. **Secure & deterministic** — `[HW]` guarantees behavior without internet; idempotent commands.
5. **Progressive scale** — the same product covers N0 (consumption only) to N5 (grid services) without re-architecting ([11](11-application-scenarios-matrix.md)).
6. **Brazil-compliance first** — PRODIST, ANEEL, INMETRO, ANATEL and local commercial arrangements are requirements ([02](02-regulatory-market-context-br.md)).

---

## 5. Packaging & tiers

| Tier | Audience | Hardware | Core |
|---|---|---|---|
| **Smart Lite** `[SW]` | Captive/DG, consumption or PV only | None (via manufacturer API/cloud) | Monitoring, bills, reports, alarms |
| **Smart Home** `[SW+HW]` | +Battery, +EV, +loads | **Smart Gateway** | Self-consumption, backup, EV smart charging, automations, white/ToU |
| **Smart Home+** `[SW+HW]` | +Load shifting + dynamic tariff | **Gateway + Smart Meter** | Price+forecast optimization, own metering, peak shaving |
| **Smart Grid** `[SW+HW]` | +Grid services / VPP / free market | **Gateway + Smart Meter** | Flexibility dispatch, aggregation, reactive control, billing |
| **Smart Pro / Fleet** `[SW]` | Installer/aggregator | — | Commissioning, fleet, OTA, O&M, API, white-label |
| **Smart DG** `[SW]` | Shared-DG manager | — | Allocation, reconciliation, multi-CU, credit billing |

Hardware in [06](06-hardware-specification.md); make-vs-buy and pricing in [12](12-roadmap-and-phasing.md). Revenue model is an `[ASSUMPTION]` to validate ([13](13-gaps-risks-and-decisions.md)).

---

## 6. Competitive positioning

- **vs gridX / Kiwigrid (DE):** mature, agnostic platforms centered on EU regulation (§14a, dynamic tariffs). Smart brings that sophistication to **shared DG, free market and Brazilian white/flag tariffs**.
- **vs SmartFox (AT):** strong PV-surplus and load control, but hardware-centric/DACH. Smart adds **multi-brand cloud + VPP + per-persona apps**.
- **vs Lifepowr (BE):** strong aggregation/V2X; Smart delivers the same **home→grid continuum** with proprietary hardware and BR compliance.
- **vs SEMS+/EzManager (GoodWe, the sources):** Smart **decouples from the brand**, keeps what they do well (monitoring, remote config, OTA, IV/AI Health diagnostics, load gateway) and adds multi-brand, edge-first and Brazilian regulatory context.

---

## 7. Success metrics (KPIs) `[ASSUMPTION]`

Average bill savings per tier; self-consumption & self-sufficiency ratios; multi-brand coverage (supported models); commissioning time per CU; offline-control availability; flexibility revenue per aggregated CU; CUs per DG manager and allocation accuracy; homeowner & installer NPS.

---

## 8. MVP vs future (summary)

- **MVP (Phase 0):** multi-brand monitoring, self-consumption, commissioning/remote config, mobile+web, captive/DG at N0–N2.
- **Phase 1:** white/ToU/dynamic tariff + load shifting + EV smart charging + battery.
- **Phase 2:** grid services, VPP, free market, shared-DG billing/allocation.

Detail and entry/exit criteria in [12 — Roadmap](12-roadmap-and-phasing.md).
