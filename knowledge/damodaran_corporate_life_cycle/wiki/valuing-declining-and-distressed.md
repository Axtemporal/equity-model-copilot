---
concept: valuing-declining-and-distressed
title: Valuing Declining & Distressed Firms
theme: Valuing mature & declining firms
status: draft
---

# Valuing Declining & Distressed Firms

**What it is.** Valuing a firm whose revenues are flat or shrinking, whose margins are compressing, and that may face a real chance of not surviving — which means inverting the growth-firm template (negative growth, negative reinvestment, cash flows exceeding earnings) and, for the distressed subset, blending the going-concern value with a distress-sale value weighted by the probability of failure.

## Core idea

Conventional going-concern DCF and relative valuation **systematically overstate** the value of declining and especially distressed firms, because both implicitly assume the firm survives to a stable, ever-growing terminal state. For a declining firm the correct picture is the mirror image of the growth story: **negative revenue growth, margins falling toward (or below) the industry average, negative reinvestment** (divestitures that release cash), and **cash flows that exceed earnings**. None of these are modeling errors to smooth away — for a business earning below its cost of capital, shrinking is the *value-maximizing* path ([[roic-and-excess-returns]]).

The valuation begins with a story about *why* the business is shrinking and *how management will respond*, then layers on distress machinery for firms that face truncation: a cumulative probability of failure ([[distress-probability]]), a blend with a distress-sale value, and — for the deeply distressed — recognition that [[equity-as-option]] retains value even past technical insolvency. Divestiture-heavy firms are valued with [[sum-of-the-parts-octopus]].

## Across the life cycle

- **Mature → decline transition:** the six tell-tale signs appear — stagnant/declining revenues, shrinking margins, asset divestitures, occasional desperation acquisitions, big payouts (sometimes exceeding earnings), and a debt load taken on in healthier days now becoming a burden.
- **Decline (this concept):** value is dominated by assets-in-place running down, plus the resolution of distress. The default trajectory *inverts* the growth template.
- **Distress / end-game:** the firm may not reach its terminal year at all; the going-concern DCF must be blended with a distress-sale value, and equity valued as an option. See [[liquidation-value]].

## Mechanics / formulas

**Negative growth via the reinvestment identity.** The standard `g = Reinvestment Rate × ROIC` still holds — with a *negative* reinvestment rate (net divestiture = cash inflow). Example: g = −5%, ROIC = 7.5% → Reinvestment Rate = g/ROIC = −66.67% (the firm releases cash equal to 66.67% of after-tax operating income each year).

**Terminal value with negative growth.** `TV = FCFF_(n+1) / (r − g)`; a negative g *enlarges* the denominator, so it is perfectly well-defined. With $100M after-tax operating income, r = 10%, g = −5%: `TV = 100 / (0.10 − (−0.05)) = $666.67M`. Crediting an asset-liquidation premium (assets fetch more divested than retained) raises the same case to ≈$1,111M. **Decision rule:** if ROIC < cost of capital, negative growth (shrinking) *adds* value and growth destroys it — the inverse of the healthy-firm intuition. See [[terminal-value]].

**The going-concern build.** `FCFF = Revenue × Operating Margin × (1 − t) − Reinvestment`, with revenue trending down, margin converging to (or below) the industry average, reinvestment negative, and the discount rate *migrating over time* as a distressed-high debt ratio normalizes toward a target. Then the usual bridge: PV(FCFF) + PV(TV) + cash → firm value; − debt → equity value; − equity options → common equity.

**The distress blend (the headline formula).**

```
Value of Equity = DCF equity value × (1 − P_distress) + Distress-sale equity value × P_distress
```

Estimate the distress-sale value as a *fraction of book value or of going-concern value* — never as the full PV of expected cash flows (if it were, distress wouldn't matter). The probability of distress is built from the rating, backed out of the bond price, or estimated by probit — see [[distress-probability]]. Equivalently, expected cash flows can be haircut period by period: `Expected CF_t = CF_t × (1 − P_distress,t)`.

**Management response drives the inputs.** The forecast shape depends on which of four responses management adopts — **denial** (negative growth, long-term decline, status-quo reinvestment, rising failure risk), **desperation** (acquisition blips that fade, volatile risk — "value destruction on steroids"), **acceptance** (short-term shrinkage then a steady-state smaller firm, negative reinvestment, stable risk), or **reinvention** (near-term decline then migration to a new-business profile). Run a 3P test (possible / plausible / probable) on any turnaround narrative before letting it lift the numbers.

## Pitfalls & nuances

- **The going-concern overstatement.** Assuming survival to a terminal nirvana ignores truncation; layer in distress.
- **Refusing negative growth or negative reinvestment.** Both are legitimate; forcing them non-negative overstates value.
- **The relative-valuation bargain trap.** A declining firm in a healthy sector *looks* cheap on low multiples — that is the market correctly penalizing worse growth, thinner margins, and higher risk. Control for fundamentals; never read a low EV/Sales or P/B as a bargain. Book value is a dangerous liquidation proxy. See [[valuation-multiples]].
- **Believing management's turnaround plan uncritically** — it "can easily lead to fairy tales"; the 3P test is the guard.
- **Distress-sale value = full DCF.** Defeats the entire point of the blend.

## Related concepts

- [[distress-probability]] — the P(distress) that weights the blend
- [[equity-as-option]] — why distressed equity isn't zero
- [[liquidation-value]] — the asset-sale floor and check
- [[sum-of-the-parts-octopus]] — the tool for divestiture-heavy firms
- [[terminal-value]] — where negative perpetual growth is legitimate
- [[roic-and-excess-returns]] — when shrinking creates value (ROIC < cost of capital)
- [[valuing-mature]] — the prior stage this one inverts
- [[fcff]] — the cash flow being discounted and truncated
- [[real-options]] — the option to abandon and the equity-option overlay
- [[activist-investing]] — can push back on desperate management and reset the path

## Provenance
- Chapter notes: [[cap_13_valuing_declining]]
- Sources: [Valuing Declining and Distressed Companies (Damodaran, SSRN 1428022)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1428022); [Myth 5.4: Negative Growth Rates Forever? Impossible! (Nov 2016)](https://aswathdamodaran.blogspot.com/2016/11/myth-54-negative-growth-rates-forever.html); [No Light at the End of the Tunnel: Investing in Bad Businesses (May 2015)](https://aswathdamodaran.blogspot.com/2015/05/no-light-at-end-of-tunnel-investing-in.html); [Bed, Bath & Beyond valuation (BB&B2022.xlsx)](https://pages.stern.nyu.edu/~adamodar/pc/blog/BB&B2022.xlsx)
- Raw (gitignored): reference/damodaran_clc/text/Ch13.txt
