---
concept: real-options
title: Real Options
theme: Corporate finance: investing & cost of capital
status: draft
---

# Real Options

**What it is.** The recognition that some investments carry embedded flexibility — the option to delay, to expand, or to abandon — whose value a static NPV misses, so a project with negative stand-alone NPV can still be worth taking when it buys a valuable option; the promise is capturing that upside, the peril is using "optionality" to rationalize bad investments.

## Core idea

Standard [[hurdle-rate-and-investment-decision]] rules (NPV, ROIC) treat a project as a fixed bet. But many investments give management the *right, not the obligation*, to act later as uncertainty resolves — and that flexibility has value the static calculation ignores. Three project options recur:

- **Option to delay** — an undeveloped reserve or a patent is a *call*: you wait, and develop only if it becomes profitable.
- **Option to expand** — a small initial investment is a beachhead that confers the *right* to enter a larger market later. Drawn as a call: if the present value of the expansion's cash flows stays below the cost of expanding, you don't expand and lose only the initial outlay; if it exceeds the cost, you expand and capture the upside.
- **Option to abandon** — the ability to walk away (a *put*) puts a floor under the downside.

So the correct value of such a project is its DCF base case *plus* the value of the embedded option. The right posture is **not to choose** between DCF and real options but to combine them: DCF alone under-values promising-but-uncertain projects and leads to under-investment; real options applied carelessly over-value risky projects and encourage over-investment.

Even when the option cannot be priced precisely, its *logic* tells you **when it is most valuable** — a big target market and high uncertainty about its size and your ability to enter. That is exactly the situation of **young firms entering large, uncertain markets**, so real-option arguments map most naturally to the early life cycle.

## Across the life cycle

- **Young / high-growth firms** are the natural home of the option to expand: accept a negative-NPV beachhead because it buys the option to enter a big, uncertain market later. This is *why* growth and real-option arguments cluster at the young end — and why they must be disciplined, not asserted (see [[valuing-young-and-startups]]).
- **Mature firms** carry options too (capacity expansion, new geographies), but with lower uncertainty the option value is thinner and the static NPV does most of the work.
- **Declining and distressed firms** flip to the **option to abandon** and to the most important late-life option of all: **equity itself as a call option** on the firm's assets. With limited liability, equity is a residual claim struck at the face value of debt — so it retains value even when the firm "owes more than it owns," and *more* uncertainty in firm value *raises* equity value (risk becomes the equity holder's friend). This overlay stops a pure DCF from wrongly zeroing out distressed equity — the full mechanics are in [[equity-as-option]].

## Mechanics / formulas

The general structure:

```
Value with option = Static NPV (often < 0) + Value of the embedded real option
```

The expansion option mapped onto a **call**:

| Option input | Real-investment analogue |
|---|---|
| Underlying asset value (S) | PV of cash flows from the future expansion |
| Strike price (K) | Cost of the expansion |
| Time to expiry (t) | Window in which the option can be exercised |
| Volatility (σ) | Uncertainty about the expansion's value |

Option value rises with **market size** and with **uncertainty**. Priced with binomial or Black–Scholes machinery — but the underlying differs from a listed option in ways that make it harder (see pitfalls).

**The three "is this option real?" tests** — the disciplining contribution that keeps the method honest:

1. **Is the first investment a prerequisite for the second?** (No prerequisite → no exclusive option, just a future opportunity available to everyone.)
2. **Does it confer an exclusive or competitive right?**
3. **Is the competitive advantage sustainable?**

Value comes only from **sustainable excess returns** — a positive, durable ROIC − cost-of-capital spread ([[roic-and-excess-returns]]) — not from the cash flows per se. An option that fails these tests is worth little.

## Pitfalls & nuances

- **Real options are notoriously hard to value.** The underlying asset is not traded (no clean replicating portfolio), price paths aren't continuous, variance isn't constant or known, and exercise isn't instantaneous (early exercise is common). Treat point estimates with humility.
- **The biggest peril is rhetorical abuse.** "Real options" is easily invoked to justify investments that fail financial muster. The three tests exist precisely to stop a real-option narrative from papering over a negative-NPV core.
- **Don't price only the upside.** As usually applied, real options value *revenue* uncertainty and ignore *cost* uncertainty — adding cost uncertainty keeps the method disciplined.
- **No option without a prerequisite.** If the initial investment is not genuinely required for the later one, there is no exclusive option, only a generic opportunity worth little.
- **The option must rest on a moat.** Without a sustainable competitive advantage, the "option" generates no excess returns and therefore no value.
- **Risk-helps-value is specific to options.** In a distressed firm, higher volatility raises equity value — the opposite of the healthy-firm intuition. Don't generalize it to ordinary cash-flow valuation.

## Related concepts

- [[hurdle-rate-and-investment-decision]] — the static NPV/IRR the option value supplements
- [[roic-and-excess-returns]] — the sustainable spread that gives an option its value
- [[equity-as-option]] — the late-life real option: distressed equity as a call on firm assets
- [[valuing-declining-and-distressed]] — where the option to abandon and equity-option overlay apply
- [[valuing-young-and-startups]] — the young-firm setting where expansion options cluster
- [[uncertainty-in-valuation]] — the uncertainty that gives options value, handled honestly
- [[corporate-lifecycle]] — why optionality matters most at the young (and distressed) ends

## Provenance

- Chapter notes: [[cap_06_investing]], [[cap_13_valuing_declining]]
- Sources: [The Promise and Peril of Real Options](https://pages.stern.nyu.edu/~adamodar/) (realopt.pdf, local Damodaran paper), [Making Real Options Really Work (van Putten & MacMillan, HBR, Dec 2004)](https://hbr.org/2004/12/making-real-options-really-work), [Option-to-expand calculator (expand.xls)](https://pages.stern.nyu.edu/~adamodar/pc/)
- Raw (gitignored): reference/damodaran_clc/text/Ch6.txt, reference/damodaran_clc/text/realopt.txt
