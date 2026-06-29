# 13 — Gaps, Risks & Decisions (EN)

> Record of **confirmed decisions**, remaining **gaps**, and **risks**. PT-BR source: [`../13-gaps-riscos-e-decisoes.md`](../13-gaps-riscos-e-decisoes.md).

---

## 1. Confirmed decisions

| # | Topic | Final decision |
|---|---|---|
| D1 | **Documentation scope** | ✅ **Complete suite** + technical artifacts (OpenAPI, JSON Schema, canonical map, certification checklist, scenario diagrams) |
| D2 | **Hardware** | ✅ **Smart Gateway** (brain + **signal-level** control; drives external contactor/breaker/ATS, no power switching) + **Smart Meter** (commodity, **< 1%**, at board/QGBT). Topologies: **T1 separate** or **T2 integrated**. No "Controller" SKU. OEM/ODM level. See [06](06-hardware-specification.md) |
| D3 | **Integration** | ✅ **Hybrid** local + cloud-to-cloud ([05](05-integration-and-connectivity.md)) |
| D4 | **Personas** | ✅ **4 personas** with roles/permissions ([08](08-cloud-platform-and-apis.md)) |
| D5 | **Scenarios** | ✅ **Full 18-cell grid** ([11](11-application-scenarios-matrix.md)) |
| D6 | **Language** | ✅ **PT-BR + EN** (mirror in `docs/smart/en/`) |
| D7 | **Priority connectors** | ✅ **GoodWe, Deye, Sungrow, Growatt, Huawei, Solis** ([05](05-integration-and-connectivity.md)) |
| D8 | **Brand** | ✅ **"Smart"** is the final name |
| D9 | **Integration map** | ✅ Canonical map + abstraction model + per-vendor templates + compatibility matrix + external-project prompt (markitdown ingestion). See `../integracao/` |

---

## 2. Regulatory items validated in research (Jun/2026)

| Topic | Confirmed |
|---|---|
| **Fio B (Law 14,300)** | ramp **15/30/45/60/75/90%** (2023→2028); **2029** = ANEEL revises methodology. DG I (≤6-Jan-2023) exempt to **2045**. Instantaneous self-consumption exempt |
| **LV free market** | **Law 15,269/2025**: LV commercial/industrial by **Nov/2027**, residential by **Nov/2028**; creates **Supplier of Last Resort (SUI)** |
| **INMETRO inverters** | **Ordinance 140/2022** + **515/2023** (emergency disconnect); scope ≤ 75 kW; applies to inverter, not Gateway/Meter |
| **Grid services / DER** | ANEEL **sandbox** for ancillary services; ONS authorized to contract **voltage control** (2025); **DER observability/operability/controllability** agenda; **CP 001/2026** on LV smart meters |

---

## 3. Remaining gaps

Real manufacturer-API specs (control limits) → external project (D9). Proprietary Modbus/SunSpec maps per model → external project. LV free-market infralegal regulation. Final LV flexibility/DR remuneration rules. Smart Meter metrological class for billing use. ANATEL/EMC costs & timelines. V2G viability in BR. ESS regulation. Business model & pricing. LGPD requirements. Per-distributor connection requirements. **No gap blocks starting** — Phase 0/MVP is viable now; they mainly condition **N5, full free market and cloud control of certain manufacturers**.

## 4. Risks & mitigation

Regulatory (flexibility/DR delay → N5 as technical capability; focus captive/DG/voltage-control value). Technical (no local nor API control → prefer local, flag incompatibility; unsafe command → local validation + mTLS + signing; offline reliability → edge-first fail-safe). Commercial (hardware cost vs value → tiers; cloud-only at N0–N1). Supply (SoC/radios → multi-vendor). Schedule (homologations → start early, pre-certified).

## 5. Open questions

1. Business model/pricing — proposal in [15](15-business-model-and-pricing.md); you still decide HW (sale/lease/HaaS), price ranges, R3/R4 and channel.
2. Metrological class — proposal: EMS = class 1 / 0.5S (≤ 1%); billing = INMETRO RTM 587 + PRODIST M5 + SMF. Confirm?
3. Depth of generated artifacts to expand (full OpenAPI, per-asset JSON Schema?).
4. External integration project — when official maps arrive, run [`../integracao/PROMPT-projeto-externo.md`](../integracao/PROMPT-projeto-externo.md) in another session and merge.
