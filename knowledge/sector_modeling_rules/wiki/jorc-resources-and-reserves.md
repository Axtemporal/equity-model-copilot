---
concept: jorc-resources-and-reserves
title: JORC / CRIRSCO — Resources vs Reserves
theme: accounting-standard
applies_to: [metals_mining]
confidence: verified
status: draft
---

# JORC / CRIRSCO — Resources vs Reserves

**What it is.** The JORC Code (and the broader CRIRSCO family) classifies a miner's
mineral inventory into **Mineral Resources** (Inferred → Indicated → Measured, rising
confidence) and **Ore Reserves** (Probable, Proved), defines the **conversion mapping**
between them, and lists the **Modifying Factors** that turn a geological resource into an
economically mineable reserve — the discipline that bounds a mine plan and its valuation.

## Core idea

Just as an E&P company is valued on certified barrels ([[spe-prms-reserve-categories]]),
a miner is valued on **certified reserves**, not on the full geological resource. The two
inventories are **non-additive, different-confidence** estimates and must never be
conflated:

- **Mineral Resources** — Inferred (lowest confidence) → Indicated → Measured (highest).
- **Ore Reserves** — Probable, Proved. These are the **economically mineable** subset of
  the resource, after applying the Modifying Factors.

**Value reserves, not resources** (weighted by confidence tier). The **2P (Proved +
Probable)** tier is the valuation base case, mirroring O&G.

## Applies to sectors

- **Metals & mining** — directly: per-mine reserve roll-forwards bound the production
  schedule. See [[reserve-based-nav]] and [[c1-aisc-mining]].
- Parallels **oil & gas** ([[spe-prms-reserve-categories]]) almost line for line — same
  reserves-vs-resources logic, same UoP depletion ([[uop-depletion]]).

## Mechanics / formulas

**Conversion mapping (encode the exact paths):**

- **Indicated → Probable only.**
- **Measured → Proved** (high confidence in Modifying Factors) **or Probable** (where
  Modifying Factors carry uncertainty).
- **Proved Ore Reserve** = the economically mineable part of a **Measured** Resource
  (highest confidence).
- **Probable Ore Reserve** = the economically mineable part of an **Indicated** (or
  sometimes Measured) Resource.

**Modifying Factors** — the criteria that convert a resource to a reserve: **mining,
processing, metallurgical, infrastructure, economic, marketing, legal, environmental,
social and governmental** (the list is "not restricted to" these). These are what make a
resource usable in a mine plan / DCF/NAV.

**Inferred Resources must NOT be converted to an Ore Reserve** — there is no direct link
from Inferred to Proved or Probable. **Exclude Inferred from the mineable / reserve-
backed production and DCF base.** (Nuance: Inferred may carry option value in *some* NAV
approaches, but never in the base mine plan.)

## Modeling implications

- Build **one tab per mine** with a reserve roll-forward (opening − production ±
  revisions ± acquisitions = closing); the production schedule reads from this and never
  exceeds reserves.
- Route resource categories correctly: only Indicated/Measured feed the reserve base;
  **Inferred is excluded** from the reserve-backed schedule.
- The reserve base also drives [[uop-depletion]].

## Pitfalls & nuances

- **Do NOT count Inferred Resources** in a mineable/DCF schedule — value reserves only.
- **Do NOT confuse resources with reserves** — non-additive, different-confidence
  inventories.
- **Do NOT model perpetual production** — bound it by the reserve base, with UoP
  depletion.

## Related concepts

- [[spe-prms-reserve-categories]] — the O&G analogue
- [[reserve-based-nav]] — valuing the reserve-bounded mine plan
- [[uop-depletion]] — the reserve base drives DD&A
- [[ifrs-6-ee-capitalization]] — exploration cost capitalization (shared with O&G)
- [[c1-aisc-mining]] — the cost stack that decides which reserves are economic

## Provenance
- Method cards: [[metals_mining]]
- Sources: [JORC-2012 — Australasian Code for Reporting of Exploration Results, Mineral Resources and Ore Reserves (JORC, 2012)](https://www.jorc.org/docs/JORC_code_2012.pdf) (corroborated by Geoscience Australia, SciELO)
- Confidence: ✅ verified (round 2, 2-0 / 3-0)
