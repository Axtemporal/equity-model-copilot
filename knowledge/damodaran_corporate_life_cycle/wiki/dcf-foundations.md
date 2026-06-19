---
concept: dcf-foundations
title: DCF Foundations
theme: Valuation foundations
status: draft
---

# DCF Foundations

**What it is.** Discounted cash flow valuation estimates intrinsic value as the present value of a business's expected future cash flows, discounted at a risk-adjusted rate — and every DCF, at any life-cycle stage, reduces to the same four inputs: cash flows from existing assets, the value added by growth, the risk in those cash flows, and a terminal value that imposes closure on an infinite-lived going concern.

## Core idea

DCF rests on one descriptive principle: an asset is worth the cash it is expected to generate, adjusted for the time value of money and for risk. Putting that into practice means grappling with three things at once — how to *define* the cash flows, how to fold *risk* into the discount rate, and how to handle the *timing* of cash flows across the forecast. It needs neither advanced mathematics nor faith in modern portfolio theory; it is a practical investor's tool, not an academic abstraction.

Damodaran decomposes every intrinsic valuation into **four value drivers**, framed as four questions:

1. **Cash flows from existing assets** — *What do assets in place earn?* Base earnings reflecting the earning power of current assets, net of taxes and the reinvestment needed just to sustain them.
2. **The value of growth** — *What does growth add (or destroy)?* Future cash flow = expected earnings − the reinvestment required to generate the growth. Growth creates value only when it earns **excess returns** (return on capital above the cost of capital — see [[roic-and-excess-returns]]).
3. **Risk in the cash flows** — *How risky are they?* Captured in the discount rate: a beta in the cost of equity, a default spread in the cost of debt; riskier cash flows are discounted harder. See [[cost-of-capital]].
4. **Terminal value** — *When does the firm reach steady state, and what then?* The length of the growth window comes from the strength of competitive advantages (the [[moat]]); beyond it, cash flows grow at a constant, economy-capped rate forever. See [[terminal-value]].

A sound DCF need not be elaborate: a handful of well-chosen operational drivers — revenue growth (market size × share), operating margin (pricing power × efficiency), and reinvestment efficiency — carries the value.

## Equity vs firm DCF

There are two internally consistent levels at which to run a DCF; mixing them is a classic error:

- **Firm (enterprise) valuation** discounts cash flows to *all* claimholders — [[fcff]] (pre-debt, after reinvestment) — at the blended **cost of capital (WACC)**. The result is the value of operating assets; subtract net debt (and, per IFRS-16 guidance, leases) and add non-operating assets to bridge to equity.
- **Equity valuation** discounts cash flows to equity only — [[fcfe]] (after debt payments and reinvestment) — at the **cost of equity**. The result is the value of equity directly. (The dividend discount model is the special case where FCFE is proxied by actual dividends.)

Done consistently, both routes give the same equity value. The firm approach is preferred when leverage is expected to change materially over time, since debt cash flows need not be modelled explicitly — useful for young and high-growth firms whose capital structure is still in flux.

## Across the life cycle

The DCF *identity* is invariant, but the cash-flow path and the reliance on terminal value shift dramatically:

- **Young firms** show negative cash flows early, turning positive only as they scale; a much larger share of value sits in later-year cash flows and terminal value. See [[valuing-young-and-startups]].
- **Mature firms** show positive cash flows immediately with little growth ahead — more value in near-term cash flows. See [[valuing-mature]].
- **Declining firms** may show *shrinking* cash flows, with a legitimately negative perpetual growth rate. See [[valuing-declining-and-distressed]].

The balance of [[narrative-to-numbers]] tracks the same arc: story-dominated when young, numbers-dominated when old.

## Mechanics / formulas

The master identity:

`Value = Σ_{t=1..n} E(CF_t) / (1 + r)^t  +  [E(CF_{n+1}) / (r − g)] / (1 + r)^n`

The first term is the PV of cash flows over the explicit horizon (n years); the second is the PV of the terminal value (a stable-growth perpetuity). Everything else in a DCF is a way of estimating E(CF_t), r, and the steady-state inputs. The discount rate r is WACC for an FCFF valuation, cost of equity for an FCFE valuation.

## Pitfalls & nuances

- **Mixing levels** — discounting FCFF at the cost of equity, or FCFE at WACC, mis-states value; keep numerator and discount rate on the same level.
- **Terminal-value dominance is not a flaw.** That the terminal piece carries most of a growth firm's value is a property of its life-cycle position, not a defect of DCF — the terminal base-year inputs are themselves set by the growth-phase assumptions (see [[terminal-value]]).
- **False precision.** DCF demands embracing uncertainty, keeping the model simple, and staying transparent — not pretending to perfect data (see [[uncertainty-in-valuation]]).
- **Forgetting the spread.** Growth modelled without checking ROIC > cost of capital adds value on the spreadsheet that the business never earns.

## Related concepts

- [[fcff]] — the firm-level cash flow, discounted at WACC
- [[fcfe]] — the equity-level cash flow, discounted at cost of equity
- [[terminal-value]] — the fourth input; closure on a going concern
- [[cost-of-capital]] — the risk input as a discount rate
- [[roic-and-excess-returns]] — why growth only counts when ROIC > cost of capital
- [[narrative-to-numbers]] — the discipline behind each input
- [[intrinsic-vs-relative-valuation]] — DCF is the value game, distinct from pricing
- [[uncertainty-in-valuation]] — handling the noise in every input

## Provenance
- Chapter notes: [[cap_09_valuation_101]]
- Sources: [Discounted Cashflow Valuations (DCF): Academic Exercise, Sales Pitch or Investing Tool?](https://aswathdamodaran.blogspot.com/2015/02/discounted-cashflow-valuations-dcf.html); local paper valuesurvey.pdf ("A Survey of Valuation Approaches"); Damodaran tool fcffsimpleginzu.xlsx ([pages.stern.nyu.edu](https://pages.stern.nyu.edu/~adamodar/pc/fcffsimpleginzu.xlsx))
- Raw (gitignored): reference/damodaran_clc/text/Ch9.txt
