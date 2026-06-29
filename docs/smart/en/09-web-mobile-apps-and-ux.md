# 09 — Web/Mobile Apps & UX (EN)

> Smart's surfaces per persona ([01](01-vision-and-prd.md)): **Mobile** for the homeowner, **Web Pro** for installer/aggregator/admin, and **DG Portal** for the shared-generation manager. All on the [cloud platform](08-cloud-platform-and-apis.md) and [canonical model](04-domain-and-data-model.md). PT-BR source: [`../09-apps-web-mobile-e-ux.md`](../09-apps-web-mobile-e-ux.md).

---

## 1. App map

| App | Persona | Platform | Focus |
|---|---|---|---|
| **Smart App (Mobile)** | Homeowner | iOS/Android | savings, comfort, automations, backup, EV |
| **Smart Web Pro** | Installer, aggregator, admin | Responsive web | commissioning, fleet, O&M, OTA, VPP, API |
| **DG Portal** | Shared-DG manager | Web | allocation, reconciliation, multi-CU, statements |

> Web Pro inherits what SEMS+ does well (fleet, remote config, OTA, diagnostics) and makes it **multi-brand**; Mobile inherits the EzManager app's simplicity and extends to multi-brand + Brazilian scenarios.

---

## 2. Feature map per persona

| Capability | Homeowner | Installer | Aggregator | DG manager |
|---|---|---|---|---|
| Energy/flow dashboard | ✅ | ✅ fleet | ✅ portfolio | ✅ per CU |
| Commissioning / asset scan | guided | ✅ full | — | — |
| Operation-mode selection | ✅ simple | ✅ advanced | ✅ policies | — |
| Automations / scenes | ✅ | ✅ | — | — |
| Alarms / notifications | ✅ | ✅ | ✅ | ✅ |
| Reports | ✅ | ✅ | ✅ | ✅ |
| OTA / remote config | — | ✅ | — | — |
| IV / AI Health diagnostics | summary | ✅ | — | — |
| EV smart charging | ✅ | ✅ | — | — |
| Billing / DG allocation | my CU | — | — | ✅ full |
| VPP / grid-services panel | — | — | ✅ | — |
| API / white-label | — | ✅ | ✅ | ✅ |

---

## 3. Key flows

- **Onboarding + commissioning (installer):** provision edge (BLE/Wi-Fi/LAN) → one-click asset scan → register CU + assets (canonical) → set owner, arrangement, tariff, scenario → apply config + OTA.
- **Operation-mode selection (homeowner):** the user chooses **goals** (Savings / Backup / Comfort / Green); the system maps them to [modes](10-operation-modes-and-features.md) and decides the execution layer (critical/offline → edge `[HW]`; otherwise cloud `[SW]`).
- **Automation/scene:** triggers (time, price/flag, PV surplus, battery SoC, presence, EV plugged) → actions (switch load, modulate EV, adjust heat pump, change battery mode); executed at the edge (`[BOTH]`).
- **Billing/allocation (DG manager):** define program, % per CU, validate metering, generate statements ([08](08-cloud-platform-and-apis.md)).
- **VPP panel (aggregator):** view aggregated flexibility, create/observe grid-service events, track dispatch and (future) revenue.

---

## 4. Main screens

Home (Mobile): energy-flow ring (PV/grid/battery/home/EV), day/month savings, backup status (SoC), mode shortcuts. Assets, Energy (power/energy curves, self-consumption/self-sufficiency), Automations, Tariff/Savings. Web Pro: Fleet (map/list, alarms, batch OTA), CU detail (devices, remote parameter config, IV diagnostics, control logs). DG Portal: programs, participating CUs, allocation, reconciliation, statements.

## 5. Design system, accessibility & white-label

Single design system (light/dark, present in SEMS); accessibility and PT-BR-first localization (+EN); **white-label/multi-brand** so installers and retailers apply their brand over the apps/portals — a channel differentiator tied to the public API ([08](08-cloud-platform-and-apis.md)).

## 6. `[SW]` vs also `[HW]`

| App action | Where it actually runs |
|---|---|
| View telemetry/reports | `[SW]` cloud |
| Set goal/mode | `[SW]` configures → runs on `[HW]` if critical |
| PV-surplus / SoC automation | schedule on `[BOTH]` (edge-preferred) |
| Backup/islanding | always `[HW]` |
| Remote inverter parameter config | `[SW]` (via edge/connector) |

Full per-layer catalog in [10 — Operation Modes](10-operation-modes-and-features.md).
