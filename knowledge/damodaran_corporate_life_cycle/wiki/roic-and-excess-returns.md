---
concept: roic-and-excess-returns
title: ROIC & Excess Returns
theme: Corporate finance: investing & cost of capital
status: draft
---

# ROIC & Excess Returns

**What it is.** The single value test in corporate finance: a firm creates value only when its return on invested capital exceeds its cost of capital — the positive *spread* (ROIC − cost of capital) is the excess return, and growth multiplies value only when that spread is positive.

## Core idea

Return on invested capital (ROIC) measures the after-tax return the firm earns on the capital actually tied up in operations; the [[cost-of-capital]] is what that capital costs. The gap between them is the **excess return** (economic profit, EVA). When the spread is positive, a dollar invested becomes worth more than a dollar — value is created. When it is negative, the firm is destroying value even while reporting accounting profits.

This makes the spread, **not growth and not margin in isolation, the headline value test**. The most load-bearing corollary in the whole framework: **growth multiplies value when the spread is positive and destroys it when the spread is negative.** A firm growing fast at a negative spread is digging a deeper hole; a firm shrinking out of negative-spread businesses is creating value. So sustainable competitive advantage — a [[moat]] — not speed of growth, is the real value driver.

The empirical reality is uncomfortable: across the global universe, **roughly 80% of firms earn returns below their cost of capital** (about 57% in milder samples). "There is not a single sector or region where a majority of firms earn more than their hurdle rates." Growth, in aggregate, is therefore more likely to destroy value than create it — which reframes the [[hurdle-rate-and-investment-decision]] as primarily a discipline against over-investment.

ROIC also decomposes into operating drivers: **ROIC = invested-capital turnover (sales/capital) × NOPAT margin (profit/sales)** — mapping to cost-leadership vs. differentiation strategies. And, per Mauboussin, it is the **change** in ROIC, more than its absolute level, that drives shareholder returns, because markets already price current quality and reward improvement.

## Across the life cycle

ROIC rises from deeply negative to modestly positive with age, but the *spread* stays thin or negative at every stage — value creation is hard throughout. Damodaran's US age-decile data (July 2022):

| | Youngest decile (~5 yr) | Oldest decile (~140 yr) |
|---|---|---|
| Median ROIC | deeply negative (≈ −58% to −75%) | modestly positive (~5%) |
| Median cost of capital | ~9.3% | ~7.0% |
| Firms with negative returns | very high (~47% on capital) | much lower (~23% on capital) |

- **Young firms** earn ROIC far below their (high) cost of capital — a deeply negative spread that the entire valuation bets will turn positive as they scale.
- **Mature firms** are where positive spreads are most achievable, and where moat width determines how long ROIC stays above the cost of capital before fading toward it.
- **Declining firms** typically earn *below* the cost of capital on existing assets, which is exactly why shrinking (negative reinvestment) creates value for them — the inverted logic of [[valuing-declining-and-distressed]].

Because market-wide ROICs **mean-revert toward the cost of capital** under competition, a forecast should fade excess returns to zero in the terminal phase unless a durable moat justifies persistence.

## Mechanics / formulas

```
ROIC = After-tax operating income (NOPAT) / Invested capital
       NOPAT            = EBIT × (1 − tax rate)
       Invested capital = BV equity + BV debt − Cash & marketable securities

ROE  = Net income / Book value of equity

Excess return (spread) = ROIC − Cost of capital            (equity version: ROE − Cost of equity)
Economic profit / EVA  = (ROIC − Cost of capital) × Invested capital

Decomposition: ROIC = (Sales / Invested capital) × (NOPAT / Sales)
                      └─ capital turnover ──┘   └── NOPAT margin ──┘
```

**Decision rule:** value is created iff ROIC > cost of capital. Growth adds value above that line and subtracts below it.

**Required accounting adjustments** (raw accounting returns are noisy and misleading):

- **Capitalize R&D** — move it into invested capital and operating income (tech ROICs look inflated mainly because R&D is expensed, not capitalized).
- **Treat operating leases as debt** — add them to invested capital.
- **Strip one-time / restructuring charges** out of operating income.
- **Net out cash** from invested capital.
- **Use consistent book-value timing** (beginning-of-period or average, applied consistently).

## Pitfalls & nuances

- **Unadjusted ROIC misleads, especially across companies.** Without the R&D/lease/one-time/cash adjustments, cross-company comparisons (e.g. coverage-consistency checks across same-sector peers) are unreliable.
- **Growth is not the value driver — the spread is.** A rising-revenue line can hide value destruction; surface ROIC − cost of capital explicitly so negative-spread growth is visible.
- **High accounting ROIC ≠ high value.** Tech's headline ROIC is partly an artifact of expensing R&D; differentiation-driven margin durability matters more than a single year's level.
- **Improvement is what pays.** Markets price current quality already; the investing edge is in spotting *improving* ROIC, and the destruction in deteriorating ROIC.
- **For private firms, mind the cost-of-equity side.** Consider the total beta when the owner is undiversified, so the spread isn't measured against an understated hurdle.

## Related concepts

- [[cost-of-capital]] — the benchmark ROIC must beat
- [[hurdle-rate-and-investment-decision]] — the spread is the value test behind the hurdle rule
- [[moat]] — what keeps the spread positive (and the fade slow)
- [[corporate-finance-first-principles]] — the value objective all three decisions serve
- [[valuing-declining-and-distressed]] — where a negative spread makes shrinking value-accretive
- [[fcff]] — the cash flow a positive spread generates
- [[corporate-lifecycle]] — the arc along which ROIC and the spread evolve

## Provenance

- Chapter notes: [[cap_06_investing]]
- Sources: [Data Update 5 for 2024: Profitability (Jan 2024)](https://aswathdamodaran.blogspot.com/2024/01/data-update-5-for-2024-profitability.html), [Return on Capital (ROC), ROIC and ROE: Measurement and Implications](https://pages.stern.nyu.edu/~adamodar/) (SSRN 1105499, full text via Stern), [ROIC and the Investment Process (Mauboussin & Callahan, Morgan Stanley / Counterpoint Global)](https://marcellus.in/story/roic-and-the-investment-process/), [Excess returns by industry datasets](https://pages.stern.nyu.edu/~adamodar/pc/datasets/EVA.xls)
- Raw (gitignored): reference/damodaran_clc/text/Ch6.txt
