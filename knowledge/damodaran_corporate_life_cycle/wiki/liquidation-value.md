---
concept: liquidation-value
title: Liquidation Value
theme: Valuing mature & declining firms
status: draft
---

# Liquidation Value

**What it is.** The proceeds from selling a firm's assets piecemeal to the highest bidders, net of forced-sale discounts and liquidation taxes — an asset-sale *floor* and a check on the going-concern value, decisive when assets are worth more sold or redeployed elsewhere than kept operating (i.e., when they earn below the cost of capital).

## Core idea

Most healthy firms are worth more as going concerns than in liquidation, so the going-concern DCF governs. But for a declining or distressed firm whose existing assets earn **below the cost of capital** ([[roic-and-excess-returns]]), the rational move is to shrink — divest or liquidate the value-destroying assets — and liquidation value becomes the relevant anchor. The liquidator's signal is simple: when liquidation value exceeds the going-concern (or market) value, selling or breaking up beats operating.

Liquidation value is computed as a sum-of-the-parts by asset rather than by business — closely related to [[sum-of-the-parts-octopus]] and to the break-up analysis of declining firms. It is the natural partner of the distress blend in [[valuing-declining-and-distressed]], where it supplies the distress-sale value.

## Across the life cycle

- **Young / growth:** assets are worth far more deployed than sold (their value is in future cash flows), so liquidation value is irrelevant and far below intrinsic value.
- **Mature:** liquidation value rises in relevance for asset-heavy firms but still typically sits below the going concern; it matters mainly as a break-up check for conglomerates.
- **Decline / distress (this concept):** the binding consideration. For bad businesses, liquidation can exceed the going concern, and a *forced* liquidation (debt coming due) draws discounted prices that must be netted out. End-game holding companies are valued essentially as liquidation/SOTP of their stakes.

## Mechanics / formulas

**The estimate.**

```
Liquidation value = Σ asset-sale proceeds (to highest bidders)
                  − fire-sale discount (deeper the faster the forced sale)
                  − liquidation taxes (gains on low/zero book-value assets)
```

Distribute proceeds in **absolute-priority order**: senior debt → subordinated / mezzanine debt → equity residual. The model surfaces the liquidator's signal whenever liquidation value (net of costs) exceeds the equity value implied by the going concern.

**Why it can exceed going-concern value.** Three drivers: (1) individual assets are worth more redeployed by a different owner; (2) — working the other way — a *forced* sale draws discounted prices because buyers smell urgency; (3) liquidation triggers tax consequences, especially on old, low-book-value assets.

**The going-concern terminal alternative.** In a DCF terminal value, an asset-liquidation premium can be credited where assets fetch more divested than retained — raising the terminal value above the pure perpetuity (see [[terminal-value]] and the negative-growth math in [[valuing-declining-and-distressed]]).

**Voluntary vs. court-driven.** Outside bankruptcy, the board assents and a liquidator sells assets and distributes proceeds; under bankruptcy the liquidator answers to the court and the process tends to be **more costly**, eating further into proceeds. Liquidation investing pays only when the acquisition price stays **below** liquidation value, costs are controlled, assets are **liquid**, and the market value sits far below liquidation value.

## Pitfalls & nuances

- **Book value ≠ liquidation value.** The single most common error. In a bad business, buyers won't pay book for assets with poor underlying economics; book-scaled multiples make declining firms look like false bargains.
- **Ignoring fire-sale discounts and taxes.** The faster the forced sale, the deeper the discount; gains on low-book assets are taxed — both shrink net proceeds.
- **Business entanglements.** Assets that only function as part of an operating whole can't be valued individually; a clean piecemeal sum overstates realizable value.
- **Mechanically asserting a break-up gain.** A break-up only adds value when the sum-of-parts gain outweighs lost economies of scale, internal-capital-market access, and synergies.
- **Treating the floor as the answer.** Liquidation is a floor and a check; the valuation is the *higher* of going-concern and liquidation, not liquidation by default.

## Related concepts

- [[valuing-declining-and-distressed]] — supplies the distress-sale value in the blend
- [[distress-probability]] — weights liquidation against the going concern
- [[sum-of-the-parts-octopus]] — liquidation value as an asset-by-asset SOTP / break-up
- [[roic-and-excess-returns]] — assets earning below the cost of capital are liquidation candidates
- [[terminal-value]] — the asset-liquidation premium in a DCF terminal value
- [[equity-as-option]] — liquidation/asset value is the underlying the equity option strikes against
- [[value-of-cash]] — cash and non-operating assets in the asset-sale sum
- [[activist-investing]] — liquidators and break-up specialists as the old-age investor class
- [[fighting-aging]] — accepting decline and shrinking vs. denying it

## Provenance
- Chapter notes: [[cap_13_valuing_declining]], [[cap_17_investing_old_age]]
- Sources: [Valuing Declining and Distressed Companies (SSRN 1428022)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1428022); [The GE End Game: Bataan Death March or Turnaround Play? (Nov 2018)](https://aswathdamodaran.blogspot.com/2018/11/the-ge-end-game-bataan-death-march-or.html); [The Yahoo Chronicles: Is this the end game? (Dec 2015)](https://aswathdamodaran.blogspot.com/2015/12/the-yahoo-chronicles-is-this-end-game.html); [Book value multiples by industry (pbvdata.xls)](https://pages.stern.nyu.edu/~adamodar/pc/datasets/pbvdata.xls)
- Raw (gitignored): reference/damodaran_clc/text/Ch13.txt, reference/damodaran_clc/text/Ch17.txt
