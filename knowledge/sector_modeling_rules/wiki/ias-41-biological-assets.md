---
concept: ias-41-biological-assets
title: IAS 41 — Biological Assets at Fair Value
theme: accounting-standard
applies_to: [agriculture, agri_inputs, pulp_paper]
confidence: verified
status: draft
---

# IAS 41 — Biological Assets at Fair Value

**What it is.** IAS 41 requires living plants and animals (biological assets) and the
agricultural produce harvested from them to be measured at **fair value less costs to
sell (FVLCTS)**, with every change in that fair value flowing **through profit or
loss** — injecting non-cash, mark-to-market volatility into reported earnings that the
model must isolate from cash operating results.

## Core idea

Most assets sit on the balance sheet at historical cost. IAS 41 breaks that rule for
living things: a standing forest, a soybean crop in the field, or a cattle herd is
re-measured to fair value at every reporting date, and the gain or loss on that
re-measurement hits the income statement immediately (**never OCI**). The logic is that
a biological asset transforms continuously — it grows, degrades, procreates — so cost
becomes a poor proxy for value well before the asset is sold.

Two consequences matter for modeling:

1. **Reported earnings carry a non-cash component.** A jump in pulp or soybean prices
   re-prices the biological asset and books a gain that never touched cash. Leaving it
   inside operating EBITDA makes margins swing with commodity prices in a way that
   misrepresents the cash business.
2. **At harvest, FVLCTS becomes the "deemed cost"** that carries into IAS 2 inventory.
   The handoff point between IAS 41 (growing) and IAS 2 (harvested, held for sale) is
   the harvest date.

There is a narrow carve-out (**IAS 41.30**): when fair value cannot be measured
reliably on initial recognition, a cost model is permitted until it can.

## Applies to sectors

- **Agriculture (row crops)** — soybean, corn, cotton in the field are biological
  assets at FVLCTS; the fair-value line is a recurring distortion to strip out. See
  [[biological-assets-in-model]].
- **Pulp & paper** — the planted eucalyptus forest is the biological asset; its
  fair-value swings are typically large relative to the asset base.
- **Agri-inputs** — relevant where a distributor takes grain as payment (barter) and
  carries grain that may fall under IAS 41 / IAS 2 depending on stage.

The **consumable vs bearer** distinction decides whether an asset even stays in IAS 41
— see [[ias-41-bearer-plants]].

## Mechanics / formulas

- Measurement: `Carrying value = Fair value − costs to sell`, re-struck each period.
- P&L impact: `Gain/(loss) on biological assets = Δ(FVLCTS) over the period`, recognized
  in profit or loss.
- Fair value is generally derived from market prices for the produce, discounted for the
  remaining growth/transport where the asset is immature (IFRS 13 hierarchy).

## Modeling implications

- Build the operating P&L on a **cash/cost basis** and add a **separate, clearly
  labeled fair-value line** (gain/loss on biological assets) that is **excluded from
  operating EBITDA**. The copilot should propose this split by default for any IAS 41
  issuer, never blend the mark-to-market into margin.
- The fair-value line is **non-cash**: it must be reversed out in the cash-flow
  reconciliation.
- Underneath the accounting, the real operating driver is **area × yield × price** (or
  tonnes × EBITDA/t for forestry) — the fair-value line is an overlay, not the driver.

## Pitfalls & nuances

- **Do NOT leave IAS 41 fair-value swings inside operating EBITDA** — they are non-cash
  and volatile; isolate them.
- Do not confuse the IAS 41 re-measurement with a realized trading gain — it reverses as
  the asset is harvested and sold at (or near) the marked value.
- Watch the IAS 41.30 cost-model carve-out for assets whose fair value isn't reliably
  measurable (young plantings, novel crops).

## Related concepts

- [[ias-41-bearer-plants]] — the amendment that decides whether an asset stays in IAS 41
- [[biological-assets-in-model]] — how to structure the fair-value line in the model
- [[ias-2-inventory-costing]] — where FVLCTS becomes deemed cost after harvest
- [[mid-cycle-normalization]] — the cyclical-price problem behind the fair-value swings

## Provenance
- Method cards: [[agriculture]], [[pulp_paper]], [[agri_inputs]]
- Sources: [IAS-41 — IAS 41 Agriculture (IFRS Foundation)](https://www.ifrs.org/issued-standards/list-of-standards/ias-41-agriculture/); practitioner: [CPDBOX-IAS41](https://www.cpdbox.com/how-to-measure-fair-value-in-agriculture-ias-41-and-ifrs-13/), [ACCA-IAS41](https://www.accaglobal.com/gb/en/student/exam-support-resources/dipifr-study-resources/technical-articles/ias-41.html)
- Confidence: ✅ verified (3-0)
