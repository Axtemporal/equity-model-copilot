---
concept: cost-of-debt-and-synthetic-rating
title: Cost of Debt & Synthetic Ratings
theme: Corporate finance: financing & cash return
status: draft
---

# Cost of Debt & Synthetic Ratings

**What it is.** The pre-tax cost of debt built up from the firm's own fundamentals — interest coverage maps to a credit rating, the rating to a default spread, and the spread plus the risk-free rate gives Kd — a self-consistent loop that lets the cost of debt be *derived from the debt schedule* rather than typed in as a standalone assumption.

## Core idea

The cost of debt is not the historical coupon a firm happens to pay; it is the rate at which the firm could borrow *today*, given its risk. Damodaran estimates it with a **synthetic rating**: instead of waiting for an agency to assign a letter grade (which many firms, and most of a Brazilian coverage list, lack), you infer the rating from how comfortably operating income covers interest, then read off the default spread the market charges that rating.

This matters because Kd is one of the two ingredients of the [[cost-of-capital]], and because it is the term that *moves* as a firm changes its leverage. In the [[capital-structure-tradeoff]], the pre-tax cost of debt is what rises as you borrow more — and the synthetic-rating loop is the mechanism that makes it rise.

## Across the life cycle

The same coverage-to-rating logic applies at every stage, but the inputs shift with age, so the *output* — Kd — falls as a firm matures:

- **Start-up / young growth.** Operating income is thin, zero, or negative, so interest coverage is undefined or far below 1. Any synthetic rating lands deep in junk territory; the implied Kd is punitive. This is the quantitative root of "young firms have no debt capacity": lenders must charge much higher rates, add restrictive covenants, *and* demand an equity kicker, so true debt to a young firm is really a hybrid.
- **High → mature growth.** Coverage climbs above 1 and keeps rising; the synthetic rating improves and the spread compresses.
- **Mature stable.** High, stable operating income produces strong coverage, an investment-grade synthetic rating, and the lowest Kd — exactly when the firm has the most debt capacity to use it.
- **Decline.** Coverage erodes as earnings shrink; the rating and Kd can deteriorate again even if the firm is not adding debt.

## Mechanics / formulas

The estimation loop, run at each candidate level of debt:

```
1.  Interest expense   = trial debt × borrowing rate
2.  Interest coverage  = EBIT / interest expense
3.  Coverage  →  synthetic credit rating      (a coverage-to-rating table)
4.  Rating    →  default spread               (a rating-to-spread table)
5.  Pre-tax cost of debt (Kd)  = risk-free rate + default spread
6.  After-tax Kd  = Kd_pretax × (1 − effective tax rate)
```

The loop is **self-referencing**: a higher trial debt level raises interest expense (step 1), which lowers coverage (step 2), which lowers the rating (step 3), which widens the spread (step 4), which raises Kd (step 5) — and so feeds back into the next iteration's interest. As you push leverage up:

- coverage drops → synthetic rating drops → default spread rises → **pre-tax Kd rises**, and
- once interest expense exceeds taxable income (EBIT), the **tax shield caps out**: the effective tax rate in step 6 falls, so after-tax Kd stops declining.

On the equity side of the same WACC build, more debt raises the **levered beta** (relever beta to the new D/E), lifting the cost of equity in parallel. Running the loop across 0%–90% leverage traces the U-shaped cost of capital and locates the optimal debt ratio.

**Weighted-average Kd for a real debt schedule.** When a firm carries several tranches (different indexers, spreads, currencies, plus lease liabilities under IFRS 16), the WACC's debt cost is the weighted average across the schedule — computed by formula from the tranche table, never a single typed cell.

## Pitfalls & nuances

- **Coverage, not the existing coupon, drives Kd.** A firm paying a low legacy coupon can still face a high marginal cost of debt if its coverage has deteriorated.
- **Cap the tax benefit on actual taxable income.** The `(1 − tax rate)` term assumes the firm is fully taxable; with loss carryforwards or a low effective rate (and, in Brazil, the JCP interaction) the after-tax Kd is higher than the textbook formula implies.
- **Negative or near-zero EBIT breaks step 2.** For young or loss-making firms, coverage is meaningless; the synthetic rating defaults to the lowest grade and the result should be read as "no meaningful debt capacity," not a precise rate.
- **The loop, not a guess, is the discipline.** Typing in a cost of debt invites the "debt is cheaper" illusion; deriving Kd from coverage forces the cost to rise honestly with leverage.

## Related concepts

- [[cost-of-capital]] — Kd is one of WACC's two inputs; this is how the debt half is estimated
- [[capital-structure-tradeoff]] — the rising-Kd term that produces the U-shaped cost of capital
- [[debt-capacity-by-stage]] — coverage and ratings improve with age, raising capacity
- [[roic-and-excess-returns]] — WACC (which Kd feeds) is the hurdle the firm must beat
- [[fcff]] — discounted at WACC, of which after-tax Kd is a component
- [[distress-probability]] — the rating/spread machinery also underlies default odds

## Provenance

- Chapter notes: [[cap_07_financing]]
- Sources: [Graham, "How Big Are the Tax Benefits of Debt?" (JF 2000)](https://people.duke.edu/~jgraham/HowBigFinalJF.pdf), [Damodaran, "A Tesla 2017 Update: A Disruptive Force and a Debt Puzzle"](https://aswathdamodaran.blogspot.com/2017/08/a-tesla-2017-update-disruptive-force.html), [optimal capital-structure tool (capstru.xls)](https://pages.stern.nyu.edu/~adamodar/pc/capstru.xls), [marginal tax rate by country](https://pages.stern.nyu.edu/~adamodar/pc/datasets/countrytaxrates.xlsx)
- Raw (gitignored): reference/damodaran_clc/text/Ch7.txt
