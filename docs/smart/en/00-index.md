# Smart — Unified EMS/HEMS Platform · Product Documentation (EN)

> **Smart** is a single energy-management product (EMS/HEMS) made of a **web + mobile app and proprietary hardware**, **vendor-agnostic**, that monitors, controls, configures, commissions and operates inverters and all other energy assets of a **low-voltage (LV) consumer unit in Brazil**. It unifies and surpasses two currently separate products (a cloud app/portal and a hardware gateway), connecting to assets via **manufacturer APIs** (including GoodWe's) **and** via **local protocols** on the hardware — a mixed topology where each function runs in the right layer (software-only, software+hardware, or hardware-only).

**Version:** 0.1 (draft) · **Date:** 2026-06-27 · **Scope:** LV consumer units in Brazil (captive, shared distributed generation, free market).

> 🌐 This is the **English mirror** of the Portuguese suite (`docs/smart/`). The PT-BR documents are the source of truth; language-neutral artifacts (OpenAPI, JSON Schema) are shared under `../artefatos/` and the integration project under `../integracao/`.

---

## Documents

| # | Document | Content |
|---|----------|---------|
| 01 | [Vision & PRD](01-vision-and-prd.md) | Problem, value proposition, positioning, personas, packaging, KPIs |
| 02 | [Regulatory & Market Context (BR)](02-regulatory-market-context-br.md) | ANEEL, DG/Law 14,300, free market, tariffs, grid services, technical norms |
| 03 | [System Architecture](03-system-architecture.md) | Edge/cloud/apps layers, mixed topologies, flows, NFRs, security |
| 04 | [Domain & Data Model](04-domain-and-data-model.md) | Entities, canonical telemetry model, tariff model |
| 05 | [Integration & Connectivity](05-integration-and-connectivity.md) | DAL, local drivers, cloud-to-cloud connectors, vendor matrix |
| 06 | [Hardware Specification](06-hardware-specification.md) | Smart Gateway + Smart Meter family, blocks, I/O, BR certifications |
| 07 | [Firmware / Edge Specification](07-firmware-edge-specification.md) | Stack, modules, edge modes, fail-safe/offline, OTA, security |
| 08 | [Cloud Platform & APIs](08-cloud-platform-and-apis.md) | Microservices, time-series, optimization/forecast, VPP, billing, public API |
| 09 | [Web/Mobile Apps & UX](09-web-mobile-apps-and-ux.md) | App map per persona, key flows, screens, white-label |
| 10 | [Operation Modes & Features](10-operation-modes-and-features.md) | Full catalog with per-layer classification |
| 11 | [Application Scenarios Matrix](11-application-scenarios-matrix.md) | 3 arrangements × 6 levels grid (18 cells), per-scenario sheets |
| 12 | [Roadmap & Phasing](12-roadmap-and-phasing.md) | MVP → dynamic tariff/EV → grid services/VPP, make-vs-buy |
| 13 | [Gaps, Risks & Decisions](13-gaps-risks-and-decisions.md) | Confirmed decisions, gaps, risks, open questions |
| 14 | [Glossary](14-glossary.md) | EN/PT-BR terms |

---

## Confirmed decisions

- **Scope:** complete suite + technical artifacts.
- **Hardware:** **Smart Gateway** (the HEMS brain; **signal-level** control of external contactor/breaker/ATS) + **Smart Meter** (commodity, **< 1%** accuracy, at the entrance board/QGBT). Topologies: **separate (T1)** or **integrated (T2)**. No separate "Controller" SKU.
- **Integration:** **hybrid** local + cloud-to-cloud. Priority connectors: **GoodWe, Deye, Sungrow, Growatt, Huawei, Solis**.
- **Personas:** four (homeowner + installer primary; aggregator + DG manager advanced), with roles & permissions.
- **Scenarios:** full grid of **18 cells**.
- **Language:** PT-BR (source) + EN (this mirror).

---

## Layer convention

| Tag | Meaning |
|-----|---------|
| `[SW]` | Software only (cloud or app) |
| `[SW+HW]` | Requires software **and** proprietary hardware |
| `[HW]` | Hardware/edge only — deterministic, works offline |
| `[BOTH]` | Can be done by the app **or** the hardware |

`[ASSUMPTION]` and `[TO VERIFY]` markers appear throughout.
