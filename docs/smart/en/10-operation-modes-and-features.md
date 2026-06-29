# 10 — Operation Modes & Features Catalog (EN)

> Full catalog of what Smart does, with the **mandatory per-layer classification** (`[SW]` software-only · `[SW+HW]` software+hardware · `[HW]` hardware/edge-only · `[BOTH]` app or hardware) and **which layer executes and why**. PT-BR source: [`../10-modos-de-operacao-e-features.md`](../10-modos-de-operacao-e-features.md).

---

## Summary table

| # | Mode / Feature | Layer | Runs on | Minimum assets |
|---|---|---|---|---|
| 1 | Monitoring / telemetry | `[SW]` / `[BOTH]` | cloud (edge optional) | any |
| 2 | Self-consumption | `[HW]` | edge | PV + (battery) |
| 3 | Backup / UPS / intentional islanding | `[HW]` | edge + hybrid inverter | battery + hybrid |
| 4 | Peak shaving / demand limit | `[HW]` | edge (Smart Meter) | metering + load/battery |
| 5 | Zero-export / injection limit | `[HW]` | edge | PV + metering |
| 6 | Load shifting (white/ToU/dynamic) | `[BOTH]` | cloud plans, edge executes | controllable load / battery |
| 7 | Price + forecast optimization | `[SW+HW]` | cloud plans, edge executes | battery/loads |
| 8 | EV smart charging (V1G) | `[SW+HW]` | edge modulates | EV charger |
| 9 | V2H / V2G | `[SW+HW]` | edge + bidirectional inverter | bidirectional EV `[TO VERIFY]` |
| 10 | Heat pump (SG-Ready) | `[SW+HW]` | edge | SG-Ready heat pump |
| 11 | Load management (plug/relay) | `[BOTH]` | edge/app | smart plug/relay |
| 12 | Scheduling / scenes / automations | `[BOTH]` | edge executes | any controllable |
| 13 | Grid services / VPP | `[SW+HW]` | cloud aggregates, edge dispatches | flexibility + metering |
| 14 | Reactive / power-factor control | `[HW]` | edge + inverter | inverter |
| 15 | Ordered curtailment (§14a-style) | `[SW+HW]` | cloud signals, edge limits | inverter/loads |
| 16 | Shared-DG allocation/management | `[SW]` | cloud | per-CU metering |
| 17 | Commissioning / remote config | `[SW]` + `[HW]` | app/cloud → edge | any |
| 18 | OTA (device & fleet) | `[SW+HW]` | cloud → edge | hardware/asset |
| 19 | IV diagnostics / AI Health / battery consistency | `[SW]` | cloud | inverter/battery |

---

## Notes per mode

- **Self-consumption `[HW]`** — fast PV↔load↔battery loop; must not depend on cloud. N1+.
- **Backup/islanding `[HW]`** — immediate local transition; Gateway commands transfer (signal → external ATS) and respects inverter **anti-islanding** ([02](02-regulatory-market-context-br.md)). N2+.
- **Peak shaving `[HW]`** — measure & act in seconds (Smart Meter / integrated Gateway); relevant where there's **contracted demand**/peak cost. N2+/N4+.
- **Zero-export `[HW]`** — fast response to not violate access-permit limits. N1+.
- **Load shifting `[BOTH]`** — plan from cloud (tariff/forecast), execution local; depends on **white/flags** (captive) or **market price** (free). N4+.
- **Price + forecast optimization `[SW+HW]`** — heavy compute in cloud ([08](08-cloud-platform-and-apis.md)); execution/fallback at edge; both price worlds. N4+.
- **EV smart charging (V1G) `[SW+HW]`** — real-time current modulation via OCPP. N3+.
- **V2H / V2G `[SW+HW]`** — needs bidirectional hardware and evolving BR regulation `[TO VERIFY]`. N3+/N5 (future).
- **Heat pump (SG-Ready) `[SW+HW]`** — 4-state SG-Ready/EEBus signal applied at edge. N4+.
- **Load management `[BOTH]`** — measure & switch common loads by priority. N4+.
- **Scheduling/scenes `[BOTH]`** — rules trigger→action; defined in app/cloud, **executed at edge** (survive offline). N3+.
- **Grid services / VPP `[SW+HW]`** — cloud aggregates/optimizes; edge executes with local guarantees; monetization gradual in BR ([02](02-regulatory-market-context-br.md)). N5.
- **Reactive / PF control `[HW]`** — fast local loop. N1+/N5.
- **Ordered curtailment `[SW+HW]`** — DisCo order via cloud, **limit guaranteed at edge** (BR analog to Germany's §14a). N5 (and N1+ for injection limit).
- **Shared-DG allocation `[SW]`** — reconciliation + **credit allocation** across CUs (Law 14,300). Arrangement B, all levels.
- **Commissioning / remote config `[SW]`+`[HW]`** — asset discovery (one-click scan), parameter config (mode, grid-connection, safety, battery), in bulk.
- **OTA `[SW+HW]`** — cloud-orchestrated, A/B applied at edge ([07](07-firmware-edge-specification.md)).
- **IV diagnostics / AI Health / battery consistency `[SW]`** — data/AI analysis in cloud (inherited from SEMS, now multi-brand).

> Which modes turn on in each cell of the grid: [11 — Application Scenarios Matrix](11-application-scenarios-matrix.md).
