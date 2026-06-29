# 15 — Business Model & Pricing (Proposal)

> **`[PROPOSAL — user's business decision]`** Revenue model, per-tier/persona pricing and go-to-market for Smart. Not final: a starting point with options and a recommendation. Links to [01 — Vision/PRD](01-vision-and-prd.md) (tiers), [11 — Scenarios](11-application-scenarios-matrix.md) and [12 — Roadmap](12-roadmap-and-phasing.md). PT-BR source: [`../15-modelo-de-negocio-e-precificacao.md`](../15-modelo-de-negocio-e-precificacao.md).

---

## 1. Revenue streams

| # | Stream | Description | Who pays |
|---|---|---|---|
| R1 | **Hardware** | Sale or lease of **Smart Gateway** / **Smart Meter** ([06](06-hardware-specification.md)) | Owner or installer |
| R2 | **Software subscription (SaaS)** | Per **CU**, tiered by asset level ([01](01-vision-and-prd.md)) | Owner / installer |
| R3 | **Market-services fee** | % of **VPP/grid-services** revenue and arbitrage (when available) | Aggregator / owner |
| R4 | **Shared-DG fee** | Per participating CU or % of allocated credits | DG manager |
| R5 | **White-label / API license** | Platform under a channel brand (installer/retailer) | Channel/partner |
| R6 | **Professional services** | Commissioning, integration, premium support | Installer / end client |

---

## 2. Pricing per tier (indicative proposal) `[ASSUMPTION]`

> Values are **placeholders** for discussion — not validated market prices.

| Tier ([01](01-vision-and-prd.md)) | Hardware | Subscription | Note |
|---|---|---|---|
| **Smart Lite** `[SW]` | — | free or low/CU/mo | API monitoring; entry point |
| **Smart Home** `[SW+HW]` | Gateway (sale/lease) | monthly/CU | self-consumption, backup, EV, automations |
| **Smart Home+** `[SW+HW]` | Gateway + Smart Meter | monthly/CU (higher) | price optimization + load shifting |
| **Smart Grid** `[SW+HW]` | Gateway + Smart Meter | monthly/CU + **R3** | grid services/VPP + revenue share |
| **Smart Pro/Fleet** `[SW]` | — | per seat/CU managed | installer/aggregator; volume |
| **Smart DG** `[SW]` | — | per participating CU (**R4**) | DG manager |

---

## 3. Model options (pick one primary)

| Option | Logic | Pros | Cons |
|---|---|---|---|
| **A — Hardware + SaaS** (recommended) | sell/lease HW + recurring per-CU subscription | recurring revenue, value-aligned; classic HEMS | needs installed base to scale |
| **B — HaaS (everything as a service)** | hardware bundled into a single monthly fee | low entry barrier for the customer | capital-intensive; churn risk |
| **C — Platform/wholesale (B2B2C)** | sell to installers/retailers who resell | scales via channel, white-label (R5) | lower per-CU margin; channel-dependent |
| **D — Energy-as-a-service / savings share** | charge % of generated savings/revenue | full outcome alignment | complex measurement/attribution; cash flow |

> **Recommendation:** **A** as the base (HW + per-CU SaaS), with **C** (channel/white-label) for scale and **R3/R4** activating at level N5 and arrangement B. **D** as an optional offer for large accounts/aggregators.

---

## 4. Unit-economics considerations `[ASSUMPTION]`

- **Hardware margin:** OEM/ODM with pre-certified radios cuts COGS ([06](06-hardware-specification.md)/[12](12-roadmap-and-phasing.md)).
- **LTV/CAC:** recurring subscription (R2) supports channel CAC; leasing (R1) lowers the barrier.
- **Churn:** lower in tiers with installed hardware and active automations (healthy functional lock-in).
- **Market revenue (R3):** **optional and gradual** — depends on LV flexibility regulation ([02](02-regulatory-market-context-br.md)); should not be the near-term plan's base.
- **DG (R4):** predictable per participating CU; grows with program size.

---

## 5. Go-to-market

- **Primary channels:** solar integrators/EPCs (install HW and resell SaaS) and **retailers** (when the LV free market opens — [02](02-regulatory-market-context-br.md)).
- **White-label (R5):** lets the channel use its own brand over the app/portal ([09](09-web-mobile-apps-and-ux.md)).
- **Entry:** **Smart Lite** (monitoring) as a low-friction entry → upsell to hardware tiers.
- **Shared DG:** partner with shared-generation administrators/cooperatives (R4).

---

## 6. Open decisions (for the user)

1. **Hardware: sale vs lease vs HaaS** (defines cash and entry barrier).
2. **Subscription price range** per tier (needs BR willingness-to-pay research).
3. **Revenue share (R3)** — percentage and regulatory trigger.
4. **DG fee (R4)** — fixed per CU or % of credits.
5. **Channel strategy** — direct-to-consumer vs B2B2C via installers/retailers.

> Once you decide 1–5, I'll turn this proposal into a **finalized model** with a price table and a simple projection.
