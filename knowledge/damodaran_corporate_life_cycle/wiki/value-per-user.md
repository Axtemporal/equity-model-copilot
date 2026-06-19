---
concept: value-per-user
title: Valuing Users, Subscribers & Customers
theme: Valuing young & high-growth firms
status: draft
---

# Valuing Users, Subscribers & Customers

**What it is.** A disaggregated valuation that builds a user-driven company's worth from the bottom up — `value = PV(existing users) + PV(new users) − PV(corporate drag)` — with per-user cash flow net of servicing cost and tax, an explicit churn/renewal rate, and a customer-acquisition cost that makes a new user worth *less* than an existing one.

## Core idea
For platforms, subscription services and marketplaces, value is generated one user at a time, so it can be *built* one user at a time. The intrinsic version decomposes the firm into three pieces:

- **Existing users** — the present value of the after-tax cash flow each current user throws off over their (finite) life, weighted by how long they are likely to stay.
- **New users** — users the firm will acquire in the future, each worth an existing user *minus* the cost to acquire them, then time-discounted.
- **Corporate drag** — overhead (G&A and other costs) that cannot be traced to any individual user, computed as a residual and capitalised, then *subtracted*.

This is the constructive answer to the crude "price per user" (or EV-per-subscriber) shortcut. A raw EV/user figure treats all users as equal and ignores growth, intensity, churn, acquisition cost, the revenue model and corporate overhead — so it is *pricing*, not value (see [[pricing-game-vs-value-game]] and [[intrinsic-vs-relative-valuation]]). The disaggregated model fixes each of those omissions, and is best run alongside a top-down [[valuing-young-and-startups]] / [[valuing-high-growth]] DCF as a cross-check, with the gap reconciled rather than either trusted alone.

## Across the life cycle
The user-based view matters most for young and high-growth platform firms, where the user base *is* the business and the corporate P&L is still loss-making. As such a firm matures, per-user economics stabilise (churn settles, CAC falls relative to lifetime value, corporate drag shrinks as a share of revenue) and the disaggregated and aggregate valuations converge. Sticky, intense user bases also carry the most [[real-options]] upside — the option to expand into adjacent businesses — though that premium should stay modest unless loyalty, usage intensity and *proprietary* data genuinely support it.

## Mechanics / formulas
**The headline identity:**

```
Value of the company = PV(Existing Users) + PV(New Users) − PV(Corporate Drag)
```

**Existing user.** Value = PV of *after-tax cash flow per user* over the user's life, weighted by the **renewal rate**. Churn is destiny: a 90% annual renewal rate implies only ~43% survival into year 8 of a 15-year life. Crucially, cash flow per user is revenue per user **net of servicing cost and tax** — *not* revenue (a $120 subscriber costing $30 to service and taxed at 20% yields ~$72 of cash flow, not $120).

**New user.** `Value of a new user = value of an existing user − customer-acquisition cost (CAC)`, then time-discounted. Spending too much to acquire users *destroys* value, exactly as over-paying for growth does anywhere — so losses spent *acquiring* users are worth more than losses spent *servicing* them.

**Corporate drag.** Residual = total operating costs − servicing cost − acquisition cost; capitalise it. High *fixed* drag amplifies both upside and downside, with implosion risk if user growth stalls.

**Five first-principle traps to avoid:** user immortality (ignoring churn), treating revenue as cash flow, "new-user magic" (free growth), corporate-cost vacuums (forgetting untraceable overhead), and suspending competitive dynamics. A practical corollary: **fixed-cost** models (economies of scale) are worth more than variable-cost ones, and growth from **revenue-per-existing-user** is worth more than growth from raw new-user count.

## Pitfalls & nuances
- **Naïve EV/user comparables.** Applying one firm's per-user value to another ignores cost structure — pasting a fixed-cost platform's per-user value onto a variable-cost rival (whose content/servicing cost scales with users) wildly overstates value. The right move is to adjust for the cost structure, which can cut the imputed value by ~80%.
- **Revenue ≠ cash flow per user.** Always strip out servicing cost and tax.
- **Forgetting CAC.** New users are worth *less* than existing ones; omitting acquisition cost makes growth look free.
- **Ignoring corporate drag.** The user-level math can look great while untraceable overhead quietly consumes the value.
- **Labelling.** A per-user *pricing* number must be tagged as pricing with its comparables and method, never presented as intrinsic value or as a recommendation (compliance).

## Related concepts
- [[valuing-young-and-startups]] — the top-down DCF this disaggregated model cross-checks
- [[valuing-high-growth]] — where user growth, fade and margin convergence meet
- [[growth-investing]] — the investing-side counterpart to user-driven growth firms
- [[intrinsic-vs-relative-valuation]] — why raw EV/user is pricing, not value
- [[pricing-game-vs-value-game]] — the broader pricing-vs-value distinction
- [[real-options]] — the optionality premium for sticky, intense, data-rich user bases
- [[fcfe]] — the after-tax cash-flow logic applied at the per-user level
- [[uncertainty-in-valuation]] — renewal rate and CAC are high-leverage inputs to vary in scenarios

## Provenance
- Chapter notes: [[cap_15_investing_youth]], [[cap_10_valuing_young]]
- Sources: [Going to Pieces: Valuing Users, Subscribers and Customers (SSRN 3175652)](https://ssrn.com/abstract=3175652), [Valuing Users (full text mirror)](https://leeds-faculty.colorado.edu/bhagat/Valuing-Users.pdf), [The Compressed Tech Life Cycle: The Investor Challenge](https://aswathdamodaran.blogspot.com/2015/12/the-compressed-tech-life-cycle-investor.html)
- Raw (gitignored): reference/damodaran_clc/text/Ch15.txt, reference/damodaran_clc/text/Ch10.txt
