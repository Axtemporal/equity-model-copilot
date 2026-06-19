---
concept: biological-assets-in-model
title: Modeling IAS 41 Fair-Value Swings
theme: driver-pattern
applies_to: [agriculture, pulp_paper]
confidence: verified
status: draft
---

# Modeling IAS 41 Fair-Value Swings

**What it is.** The modeling pattern for IAS 41 issuers: build the operating P&L on a
**cash/cost basis** and add a **separate, clearly labeled fair-value line** (gain/loss on
biological assets) that is **excluded from operating EBITDA** and reversed in cash flow —
so the analyst sees real operating margin, not mark-to-market noise, with the genuine
driver (area × yield × price, or tonnes × EBITDA/t) underneath.

## Core idea

[[ias-41-biological-assets]] forces living assets to fair value through P&L, injecting a
non-cash, commodity-price-driven swing into reported earnings. Left inside EBITDA, it
makes margins lurch with prices in a way that misrepresents the cash business. The fix is
structural separation:

1. Model the **operating result** on cash/cost economics — the physical driver times
   price, minus cash cost.
2. Add the **IAS 41 fair-value re-measurement** as its own line, **below** operating
   EBITDA, flagged non-cash.
3. **Reverse** it in the cash-flow reconciliation (it never touched cash).

## Applies to sectors

- **Agriculture (row crops)** — driver is **hectares × yield (t/ha) × price** per crop,
  with the safra calendar driving timing; the IAS 41 line on the standing crop is the
  overlay. Owned **farmland** is often a separate NAV block.
- **Pulp & paper** — driver is **tonnes × utilization × EBITDA/t** per business unit; the
  IAS 41 line on the planted eucalyptus forest is the overlay.

Both assets are **consumable** (harvested/felled whole) and therefore stay in IAS 41 —
see [[ias-41-bearer-plants]].

## Mechanics / formulas

- Operating: `EBITDA(operating) = Σ (volume × price − cash cost)` — no fair-value line.
- Overlay: `Gain/(loss) on biological assets = Δ FVLCTS`, recognized below operating
  EBITDA, non-cash.
- At harvest, FVLCTS becomes the **deemed cost** carried into IAS 2 inventory
  ([[ias-2-inventory-costing]]).

## Modeling implications

- The copilot proposes the **EBITDA / fair-value split by default** for any IAS 41 issuer.
- For pulp, layer the **Brent → cash cost** linkage (chemicals/inputs are oil-linked) and
  **separate FX sensitivity on revenue vs cost** (USD revenue, partly-BRL cost).
- For agriculture, keep **owned land as a separate NAV block** (cost or appraised),
  distinct from the farming DCF — a sum-of-the-parts where land can dominate.

## Pitfalls & nuances

- **Do NOT leave fair-value swings inside operating EBITDA** — isolate the non-cash line.
- **Do NOT model flat yields** (agriculture) — yield varies with weather/safra; price and
  FX are volatile and often hedged.
- **Do NOT net FX** (pulp) — revenue (USD) and cost (partly BRL) have different
  sensitivities; model them separately.

## Related concepts

- [[ias-41-biological-assets]] — the standard behind the fair-value line
- [[ias-41-bearer-plants]] — why these assets stay in IAS 41
- [[ias-2-inventory-costing]] — where FVLCTS becomes deemed cost at harvest
- [[mid-cycle-normalization]] — the commodity-price cycle driving the swings

## Provenance
- Method cards: [[agriculture]], [[pulp_paper]]
- Sources: [IAS-41 (IFRS Foundation)](https://www.ifrs.org/issued-standards/list-of-standards/ias-41-agriculture/); [XP-PULP-2022 — XP Investimentos, Suzano initiation (Dec 2022)] (operating drivers 🟡 single-source)
- Confidence: ✅ verified (3-0) for the IAS 41 split; pulp operating drivers 🟡 seed
