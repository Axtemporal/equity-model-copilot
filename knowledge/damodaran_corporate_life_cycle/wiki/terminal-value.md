---
concept: terminal-value
title: Terminal Value
theme: Valuation foundations
status: draft
---

# Terminal Value

**What it is.** The terminal value is the device that imposes closure on an infinite-lived going concern: it is the present value, as of the end of an explicit forecast horizon, of all cash flows beyond that horizon, capitalised as a constant-growth perpetuity at the rate r − g — and for growth firms it routinely accounts for the bulk of total value.

## Core idea

A business can in principle last forever, but no analyst can forecast cash flows one year at a time to infinity. The terminal value solves this by splitting valuation in two: an **explicit forecast** of n years, modelled in detail, followed by a **steady state** in which cash flows are assumed to grow at a constant rate g forever. The steady-state stream is collapsed into a single number — a perpetuity — placed at year n, then discounted back to today.

The engine is the growing-perpetuity formula `CF / (r − g)`. The denominator `r − g` is the "spread" between the discount rate and the perpetual growth rate: the smaller it is, the larger the terminal value, which is why terminal value is acutely sensitive to both inputs. The terminal value is not a separate model — it is the same DCF identity (see [[dcf-foundations]]) applied once the firm has reached maturity, so the steady-state inputs (reinvestment, risk, growth) must be those of a *mature* firm.

## Mechanics / formulas

The full DCF with terminal value:

`Value today = Σ_{t=1..n} E(CF_t)/(1+r)^t  +  [E(CF_{n+1})/(r − g)] / (1+r)^n`

The bracketed term is the terminal value at year n; the trailing discount factor brings it to the present. In stable-growth perpetuity form, by level:

- Firm: `Terminal firm value = FCFF_{n+1} / (WACC − g)` (see [[fcff]])
- Equity (FCFE): `Terminal equity value = FCFE_{n+1} / (Cost of equity − g)` (see [[fcfe]])
- Equity (dividends, Gordon growth): `DPS_{n+1} / (Cost of equity − g)`

**The economy cap.** The perpetual g cannot exceed the long-run nominal growth rate of the economy (use nominal g with a nominal r). A firm growing faster than the economy forever would eventually *become* the economy — impossible. In practice g is anchored near the risk-free rate.

**Steady-state consistency.** At the terminal point the firm must be given mature characteristics: lower costs of debt and equity, a higher debt ratio, and a chosen terminal return on capital. Some analysts set terminal ROC equal to the cost of capital (no excess return, so growth adds no value); Damodaran prefers preserving some firm-specific flexibility so a durable [[moat]] can keep ROC above the cost of capital in perpetuity (see [[roic-and-excess-returns]]).

## Across the life cycle

- **Young / high growth:** because cash flows are low or negative early and large late, terminal value can be **80%, 90%, even more than 100%** of total value. This is normal, not a DCF flaw — the year-5 or year-10 base-year inputs that feed the terminal calculation are *themselves* determined by the growth-phase story, so changing that story changes terminal value dramatically. The high terminal share is a property of the firm's life-cycle position. See [[valuing-high-growth]] and [[narrative-to-numbers]].
- **Mature:** a smaller fraction of value sits in the terminal piece, because near-term cash flows are large and growth is modest. See [[valuing-mature]].
- **Decline:** a **negative perpetual g is legitimate** here. A shrinking business genuinely contracts forever; "negative growth rates forever" is not impossible, and forcing g to be non-negative overstates the value of a declining firm. See [[valuing-declining-and-distressed]].

## Pitfalls & nuances

- **Breaking the economy cap** — the single most common terminal-value error; g above nominal GDP growth manufactures value.
- **Mismatched terminal inputs** — keeping growth-phase margins, reinvestment or risk in the perpetuity inflates value; the firm must look mature at the terminal point.
- **Treating high terminal share as a defect.** For a growth firm it is expected; the cure for the discomfort is to interrogate the *base-year* inputs, not to truncate the growth period artificially.
- **Waiting too long to converge.** Scale and competition lower growth fast; high-growth windows beyond ~10 years are rare and should be justified — and even shorter for compressed-life-cycle tech (see [[compressed-lifecycle-tech]]).
- **Refusing a negative g for a declining firm** — overstates the floor; pair it with distress probability where relevant (see [[valuing-declining-and-distressed]]).

## Related concepts

- [[dcf-foundations]] — terminal value is the fourth of the four DCF inputs
- [[fcff]] — `FCFF_{n+1} / (WACC − g)` is the firm-level terminal block
- [[fcfe]] — the equity-level terminal block
- [[roic-and-excess-returns]] — terminal growth adds value only if ROC > cost of capital
- [[valuing-high-growth]] — where terminal value dominates total value
- [[valuing-declining-and-distressed]] — where negative perpetual growth is legitimate
- [[moat]] — what justifies a terminal ROC above the cost of capital
- [[uncertainty-in-valuation]] — terminal inputs are where false precision creeps in

## Provenance
- Chapter notes: [[cap_09_valuation_101]], [[cap_11_valuing_high_growth]]
- Sources: local paper valuesurvey.pdf ("A Survey of Valuation Approaches"); [Myth 5.4: Negative Growth Rates Forever? Impossible! (Nov 2016)](https://aswathdamodaran.blogspot.com/); [The Aging of the Tech Sector (Feb 2015)](https://aswathdamodaran.blogspot.com/2015/02/the-aging-of-tech-sector-pricing.html)
- Raw (gitignored): reference/damodaran_clc/text/Ch9.txt, reference/damodaran_clc/text/Ch11.txt
