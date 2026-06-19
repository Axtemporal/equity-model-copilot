---
concept: fcff
title: Free Cash Flow to Firm (FCFF)
theme: Valuation foundations
status: draft
---

# Free Cash Flow to Firm (FCFF)

**What it is.** Free cash flow to the firm is the cash a business generates from operations for *all* its claimholders — debt and equity together — measured before debt payments but after taxes and after the reinvestment needed to sustain and grow the business; it is the cash flow discounted at the cost of capital (WACC) in a firm-level DCF.

## Core idea

FCFF answers the question *how much cash does the operating business throw off, irrespective of how it is financed?* By stopping before any payment to lenders, it isolates the cash flow of the enterprise from the choice of capital structure. That is why it pairs with **WACC** — a blended, capital-structure-weighted discount rate — and why discounting it yields the value of the *whole firm* (operating assets), from which equity is reached by netting out non-equity claims.

This is the firm side of the equity-vs-firm choice in [[dcf-foundations]]. Its counterpart is [[fcfe]], the cash flow left for equity *after* debt. The two are linked: FCFF minus after-tax interest plus net new borrowing gives FCFE.

## FCFF vs FCFE

| | FCFF (free cash flow to firm) | FCFE (free cash flow to equity) |
|---|---|---|
| Claimholders | All (debt + equity) | Equity only |
| Position vs debt | **Pre**-debt payment | **After** debt payment |
| Starts from | After-tax operating income, EBIT × (1 − tax) | Net income |
| Discount rate | **Cost of capital (WACC)** | **Cost of equity** |
| PV gives | Value of the whole firm → subtract net debt for equity | Value of equity directly |
| Best when | Leverage is expected to shift over time | Leverage is stable and explicitly modelled |

Done consistently, both routes reach the same equity value. The firm/FCFF route is preferred when the capital structure is in flux — common for young and high-growth firms — because it does not require modelling each year's debt cash flows explicitly, only the debt ratios and rates that feed WACC.

## Across the life cycle

The *shape* of FCFF over time tracks the life cycle:

- **Young / high growth:** FCFF is low or deeply negative early, because EBIT is thin or negative *and* reinvestment to fund growth is heavy; it turns positive only as growth fades and margins climb. Most value therefore sits in later years and [[terminal-value]]. See [[valuing-high-growth]].
- **Mature:** FCFF is positive and substantial immediately, with modest growth ahead; near-term cash flows carry most of the value. See [[valuing-mature]].
- **Declining:** FCFF may *shrink* over time, and reinvestment can go negative as the firm divests capacity. See [[valuing-declining-and-distressed]].

Because FCFF deducts reinvestment, the way reinvestment is sized matters: for scaling firms Damodaran ties it to revenue change through a sales-to-capital ratio rather than to noisy capex (see [[valuing-high-growth]]).

## Mechanics / formulas

`FCFF = EBIT × (1 − tax rate) − (Capital expenditures − Depreciation) − Change in non-cash working capital`

Equivalently, the firm-level stable-growth perpetuity (the terminal building block) is:

`Value of firm = FCFF_1 / (WACC − g)`

with g capped at the growth rate of the economy. For a scaling firm, reinvestment is often re-expressed as `Reinvestment_t = ΔRevenues_t / (sales-to-capital ratio)`, so `FCFF_t = EBIT_t × (1 − tax) − Reinvestment_t`. The IFRS-16 convention used in the project deducts lease payments in FCFF and treats leases as debt in the EV→equity bridge.

## Pitfalls & nuances

- **Discounting FCFF at the cost of equity** — a level mismatch; FCFF belongs with WACC.
- **Forgetting to bridge to equity.** PV of FCFF is *firm* value; subtract net debt (and leases, per IFRS-16) and add non-operating assets / cash to reach equity, then divide by shares.
- **Treating depreciation as cash.** Reinvestment is net capex (capex − depreciation) plus the change in working capital, not gross figures.
- **Volatile reinvestment.** Year-to-year capex and working-capital swings are noisy for growth firms; size reinvestment off revenue change via sales-to-capital instead.

## Related concepts

- [[dcf-foundations]] — FCFF is the firm-level route through the four DCF inputs
- [[fcfe]] — the equity-level counterpart, after debt
- [[cost-of-capital]] — WACC, the rate FCFF is discounted at
- [[terminal-value]] — `FCFF_1 / (WACC − g)` is the perpetuity engine
- [[roic-and-excess-returns]] — reinvestment adds value only at ROIC > WACC
- [[valuing-high-growth]] — where reinvestment is sized via sales-to-capital
- [[intrinsic-vs-relative-valuation]] — FCFF DCF is the value game

## Provenance
- Chapter notes: [[cap_09_valuation_101]]
- Sources: local paper valuesurvey.pdf ("A Survey of Valuation Approaches"); [Earnings and Cashflows: A Primer on Free Cash Flow (Oct 2022)](https://aswathdamodaran.blogspot.com/); Damodaran tool fcffsimpleginzu.xlsx ([pages.stern.nyu.edu](https://pages.stern.nyu.edu/~adamodar/pc/fcffsimpleginzu.xlsx))
- Raw (gitignored): reference/damodaran_clc/text/Ch9.txt
