---
concept: cost-of-capital
title: Cost of Capital (WACC)
theme: Corporate finance: investing & cost of capital
status: draft
---

# Cost of Capital (WACC)

**What it is.** The blended, market-value-weighted average of the cost of equity and the after-tax cost of debt — the single rate that serves as the hurdle for investing, the target to minimize when financing, the trigger for returning cash, and the discount rate for valuing.

## Core idea

Damodaran calls the cost of capital the **"Swiss Army knife of finance"**: one number used in four roles. It is the **hurdle rate** for the [[hurdle-rate-and-investment-decision]] (new investments must beat it), the **optimizer** for the [[capital-structure-tradeoff]] (the mix that minimizes it maximizes firm value), the **divining rod** for the [[cash-return-dividends-buybacks]] decision (return cash when no project clears it), and the **discount rate** for valuation ([[dcf-foundations]], applied to [[fcff]]).

It is built bottom-up from two costs and a set of weights. The **cost of equity** is the return equity investors require given the riskiness of the firm's operations; the **cost of debt** is the rate the firm would pay on long-term borrowing today, after the tax shield. The two are combined at **market-value weights** — not book weights, which break down (around 10% of US firms have negative book equity).

A central discipline: estimate every input **in the currency of the cash flows**, keep it **current** (today's risk-free rate, today's rating — not the historical book interest rate), and treat it as **dynamic**, because the level drifts down as a firm matures.

## Across the life cycle

The cost of capital **falls with age**, and its components shift in step. Damodaran's US age-decile data (July 2022) gives the gradient:

| | Youngest decile (~5 yr) | Oldest decile (~140 yr) |
|---|---|---|
| Median cost of capital | ~9.3% | ~7.0% |
| Quartile range | ~8.7% / ~9.6% | ~6.7% / ~8.9% |

The market median sits around **8%**. The driver is the **beta**, which is not a fixed trait but should *decline over the life cycle* as the business de-risks:

- **Business risk** — young firms are riskier because their product and market are unproven; risk falls as demand stabilizes.
- **Operating leverage** — young firms often carry higher fixed costs relative to revenue; this eases with scale.
- **Financial leverage** — young firms borrow little, so this driver is small early and grows as firms mature and lever up (the financing rotation of [[corporate-finance-first-principles]]).

The modeling consequence: in a forecast of a young firm, let the **WACC drift down** and the **beta drift toward 1** as it matures, rather than holding a constant discount rate.

## Mechanics / formulas

```
Cost of capital = Cost of equity × E/(D+E) + After-tax cost of debt × D/(D+E)

Cost of equity        = Rf + (Relative risk measure × Equity Risk Premium)   [CAPM: relative risk = β]
After-tax cost of debt = (Rf + Default spread) × (1 − marginal tax rate)
```

**The inputs:**

- **Risk-free rate (Rf)** — a long-term, default-free government rate in the currency of analysis; differences across currencies are mostly expected-inflation differences and wash out if cash-flow inflation is matched. (If the government bond carries default risk, net out the sovereign spread.)
- **Equity Risk Premium (ERP)** — the price of equity risk; prefer the *implied/forward* ERP backed out of current index levels and expected cash flows over a backward-looking historical premium (July 2022 implied ERP ≈ 6.01%). Set it by *where the company does business*, not merely where it is incorporated — relevant for firms with cross-border revenue. Rule of thumb: ERP ≈ 2× the Baa default spread.
- **Relative risk (β)** — the asset's risk relative to the average. Damodaran is agnostic about the exact measure; substitutes for when you distrust price-based betas include the **total beta** (σ_stock / σ_market) and **relative standard deviation** for undiversified owners (the practical tool for private firms), accounting/earnings betas, and **sector-average betas** to kill single-regression noise.
- **Default spread** — the bond-market price of risk, set by the firm's *current* rating; see [[cost-of-debt-and-synthetic-rating]].
- **Tax rate** — the *marginal* (not effective) rate for the shield, and only while the firm is actually making money (no shield during operating losses).
- **Weights** — market values of debt and equity, updated dynamically as the firm matures.

## Pitfalls & nuances

- **Don't over-engineer the discount rate.** Damodaran's first lesson: the cross-firm cost-of-capital spread is narrow (~80% of US firms between 5.2% and 10%), so **cash-flow errors dwarf discount-rate errors**. Spend the effort on revenue, margin, and reinvestment.
- **The cost of capital is not a receptacle for fears.** Don't bury discrete risks (FDA failure, project flop) in the rate — use probabilities and decision trees. See [[uncertainty-in-valuation]].
- **Keep it current and currency-consistent.** A frozen historical cost of capital, or one estimated in the wrong currency, biases value; default spreads and the ERP move over time.
- **Use market-value weights, marginal tax.** Book weights break down; the effective tax rate understates the marginal shield.
- **Watch for agenda-driven rates.** Discount-rate fiddling is where bias quietly enters a valuation — every input should carry a method and a source.
- **Wire the cost of debt from the debt schedule.** The weighted-average cost of the actual tranches (indexes, spreads) should feed the WACC by formula, never a standalone typed number.

## Related concepts

- [[hurdle-rate-and-investment-decision]] — the cost of capital *as* the hurdle rate
- [[cost-of-debt-and-synthetic-rating]] — how the Kd component is built from a rating
- [[capital-structure-tradeoff]] — the mix that minimizes the cost of capital
- [[roic-and-excess-returns]] — the return the cost of capital is measured against
- [[fcff]] — the cash flow the WACC discounts
- [[dcf-foundations]] — the valuation role of the cost of capital
- [[uncertainty-in-valuation]] — where discrete risks belong instead of the discount rate
- [[corporate-lifecycle]] — the arc along which the WACC fades

## Provenance

- Chapter notes: [[cap_06_investing]]
- Sources: [The Cost of Capital: The Swiss Army Knife of Finance](https://pages.stern.nyu.edu/~adamodar/) (costofcapital.pdf, local Damodaran paper), [Data Update 5 for 2024: Profitability (Jan 2024)](https://aswathdamodaran.blogspot.com/2024/01/data-update-5-for-2024-profitability.html), [Cost of capital by industry datasets](https://pages.stern.nyu.edu/~adamodar/pc/datasets/wacc.xls)
- Raw (gitignored): reference/damodaran_clc/text/Ch6.txt, reference/damodaran_clc/text/costofcapital.txt
