---
concept: ias-41-bearer-plants
title: IAS 41 — Bearer Plant Amendment
theme: accounting-standard
applies_to: [agriculture, pulp_paper]
confidence: verified
status: draft
---

# IAS 41 — Bearer Plant Amendment

**What it is.** The June 2014 amendment to IAS 16 and IAS 41 moved **bearer plants** —
living plants that bear produce repeatedly over many periods and are not themselves sold
as produce — out of IAS 41 fair-value accounting and into **IAS 16** (cost or
revaluation, depreciated like property, plant & equipment), while the **produce growing
on them stays under IAS 41** at fair value.

## Core idea

Before 2014, a grape vine or a rubber tree was re-marked to fair value every period like
any biological asset, even though the plant itself is never sold — it is more like a
factory that produces grapes or latex year after year. The amendment recognized that
such **bearer plants behave like manufacturing equipment**, so they belong in IAS 16:
capitalized at cost, depreciated over their productive life, optionally revalued. The
**produce** they bear (the grapes, the latex, the fruit) remains a biological asset
under IAS 41 until harvest.

The classification test is whether the plant is **harvested whole (consumed)** or
**bears produce repeatedly while remaining in place**:

- **Bearer plant → IAS 16.** Grape vines, rubber trees, oil palms, tea bushes, fruit
  trees. Bears produce for more than one period; not itself the harvested produce.
- **Consumable biological asset → stays IAS 41.** The plant *is* what gets harvested,
  felled, or sold.

## Applies to sectors

- **Agriculture (row crops)** — **annual row crops (soy, corn, cotton) are CONSUMABLE
  biological assets**: the whole plant is harvested each season, so they **stay under
  IAS 41 at FVLCTS**. The bearer-plant carve-out does **not** apply to them. Perennial
  orchards/vineyards a producer might also own *would* route to IAS 16.
- **Pulp & paper** — **eucalyptus planted for pulp is felled (cut down) at harvest**, so
  it is a **consumable biological asset that STAYS under IAS 41**, not a bearer plant.
  Do not depreciate it under IAS 16.

This is the single most common misclassification in both sectors, which is why it earns
its own article.

## Mechanics / formulas

- Bearer plant (IAS 16): capitalize establishment cost → depreciate over productive life
  → optional revaluation. Produce on it (IAS 41): FVLCTS through P&L.
- Consumable asset (IAS 41): FVLCTS through P&L throughout; no depreciation of the plant
  because the plant itself is the produce.

## Modeling implications

- The engine must **route by classification**: annual crops and pulp eucalyptus → IAS 41
  fair-value line ([[biological-assets-in-model]]); any genuine bearer plant (orchard,
  vineyard) → an IAS 16 depreciated-asset schedule.
- Getting this wrong flips a non-cash fair-value line into a depreciation line (or vice
  versa), mis-stating both EBITDA and the asset base.

## Pitfalls & nuances

- **Do NOT apply the bearer-plant/IAS 16 treatment to annual row crops** — they are
  consumable IAS 41 assets.
- **Do NOT depreciate pulp eucalyptus under IAS 16** — it is felled at harvest, hence
  consumable, hence IAS 41.
- The produce on a genuine bearer plant still sits in IAS 41 — the amendment splits the
  plant from its fruit, it does not remove fruit from fair value.

## Related concepts

- [[ias-41-biological-assets]] — the base standard this amendment carves into
- [[biological-assets-in-model]] — modeling the resulting fair-value line
- [[agriculture]] — row crops stay IAS 41
- [[pulp_paper]] — pulp eucalyptus stays IAS 41

## Provenance
- Method cards: [[agriculture]], [[pulp_paper]]
- Sources: [IAS-41-BP-2014 — Agriculture: Bearer Plants, Amendments to IAS 16 and IAS 41 (IFRS Foundation, June 2014)](https://www.ifrs.org/content/dam/ifrs/project/agriculture-bearer-plants/final-agriculture-bearer-plants-june-2014-website.pdf)
- Confidence: ✅ verified (3-0)
