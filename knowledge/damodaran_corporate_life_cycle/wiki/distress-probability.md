---
concept: distress-probability
title: Distress / Default Probability
theme: Valuing mature & declining firms
status: draft
---

# Distress / Default Probability

**What it is.** The cumulative odds, over the DCF horizon, that a firm fails before reaching its terminal year — estimated from bond-rating default tables, backed out of the firm's bond price, or predicted by a probit model — and used to weight a going-concern value against a distress-sale value.

## Core idea

Distress is the wild card that separates "declining" from "dying." When it hits, the firm's life *terminates* and all cash flows beyond that point are lost — so a going-concern DCF, which assumes survival to stable growth, overstates value. The fix is to estimate a **cumulative probability of distress** over the forecast horizon and blend the going-concern value with a distress-sale value (see [[valuing-declining-and-distressed]]).

A key feedback loop makes the probability *dynamic*: a rising debt-to-equity ratio — from big payouts, divestitures, or deteriorating earnings — pushes up the cost of debt ([[cost-of-debt-and-synthetic-rating]]) *and* the probability of distress simultaneously. The same lever feeds [[cost-of-capital]] and the failure odds, so the two cannot be estimated independently.

## Mechanics / formulas

Estimate the probability **cumulatively** over the horizon (often 10 years), by any of three methods:

**(a) From the bond rating.** Map the rating to a historical cumulative default probability. Illustrative cumulative figures: AAA/AA ≈ 0.03%, A ≈ 0.25%, BBB ≈ 0.40%, B ≈ 2.4%, CCC/CC ≈ 4.3% (10-year), rising steeply for the lowest tiers. A Moody's B1 firm in the chapter's case carries a ~23.7% failure probability.

**(b) Back it out of the bond price (Solver).** Solve for the annual default probability `π` that makes the bond's promised coupons and principal — each multiplied by the survival probability `(1 − π)^t` and discounted at the riskfree rate — equal the observed market price. Worked example: a 12% coupon, 8-year bond trading at $653 with a 5% riskfree rate solves to `π ≈ 13.53%` annually. Cumulative survival over 10 years = `(1 − 0.1353)^10 = 23.37%`, so cumulative `P_distress = 1 − 0.2337 = 76.63%`.

**(c) Statistical / probit model.** Build a bankruptcy indicator (1 = failed, 0 = survived) and regress it on beginning-of-period financials, e.g. `Distress Dummy = a + b·(Debt/Capital) + c·(Operating Margin)`, to predict the probability out of sample.

**The distress-sale value.** Estimate it as a **percent of book value** (lower in a bad economy or when peers are also distressed) **or** as a **percent of the going-concern DCF value** — *never* as the full PV of expected cash flows. In the worked case, a distress-sale of 25% of $14,531M book capital = $3,633M, which is below $7,647M book debt, so distress-sale equity = $0.

**The blend it feeds.**

```
Value of Equity = DCF equity value × (1 − P_distress) + Distress-sale equity value × P_distress
```

Worked: going-concern equity $3.22/share, distress-sale equity $0, P_distress = 76.63% → `3.22 × (1 − 0.7663) + 0 × 0.7663 = $0.75/share`. A relative-valuation analogue substitutes a healthy-peer relative value for the DCF term, or adjusts the multiple by rating directly. An APV form sets `Expected Bankruptcy Cost = (Unlevered firm value − Distress-sale value) × P_distress`.

## Across the life cycle

- **Young firms** carry a *failure* probability too, but it is driven by cash burn and survival runway, not by leverage and ratings — see [[failure-probability]] for the start-up analogue.
- **Mature firms** typically have negligible distress probability; it surfaces only with disruption or an over-levered balance sheet.
- **Declining / distressed firms** are where this concept lives: a deteriorating rating and a climbing D/E push the cumulative odds up, and the blend becomes material.

## Pitfalls & nuances

- **Annual vs. cumulative.** The blend needs the *cumulative* probability over the horizon; an annual π must be compounded into a survival probability first.
- **Distress-sale value = full DCF.** If you set it equal to the going-concern value, distress has no effect — defeating the exercise.
- **Static debt ratio.** Letting D/E (hence Kd and P_distress) stay fixed while the firm pays out cash or divests understates the risk; the rate must migrate.
- **Unreliable distressed betas.** Betas from long historical windows are unreliable for distressed firms and can even *fall* as the stock decouples from the market — don't lean on them.
- **"Big firms can't fail."** Enron and Kmart rebut the purist claim that large, listed firms with unlimited capital access never liquidate.

## Related concepts

- [[valuing-declining-and-distressed]] — the parent valuation that consumes P(distress)
- [[equity-as-option]] — the alternative lens when face debt exceeds firm value
- [[liquidation-value]] — the source of the distress-sale value in the blend
- [[cost-of-debt-and-synthetic-rating]] — the rating that supplies method (a)
- [[cost-of-capital]] — moves with the same rising D/E that drives P(distress)
- [[capital-structure-tradeoff]] — the bankruptcy-cost side of the leverage trade-off
- [[failure-probability]] — the young-firm analogue (cash-burn-driven, not leverage-driven)
- [[uncertainty-in-valuation]] — distress as a probability-weighted, not point, estimate

## Provenance
- Chapter notes: [[cap_13_valuing_declining]]
- Sources: [Valuing Equity in Firms in Distress (Damodaran, eqnotes/distress.pdf)](https://pages.stern.nyu.edu/~adamodar/pdfiles/eqnotes/distress.pdf); [Valuing Distressed and Declining Companies (Damodaran, NewDistress.pdf)](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/NewDistress.pdf); [Bed, Bath & Beyond valuation (BB&B2022.xlsx)](https://pages.stern.nyu.edu/~adamodar/pc/blog/BB&B2022.xlsx)
- Raw (gitignored): reference/damodaran_clc/text/Ch13.txt
