# Damodaran — The Corporate Life Cycle (knowledge base)

Distilled knowledge base built from Aswath Damodaran's companion site to
*The Corporate Life Cycle: Business, Investment, and Management Implications*
(Penguin/Portfolio, 2024) — <https://pages.stern.nyu.edu/~adamodar/New_Home_Page/CLC.htm>.

**What this is.** One distilled note per book chapter (20), plus two synthesis
notes. All notes paraphrase Damodaran's frameworks in our own words with
provenance to the original slides/papers/posts. See [`_schema.md`](_schema.md)
for the note contract and [`_sources.md`](_sources.md) for the full bibliography.

**Three folders (llm-wiki, CLAUDE.md decision #9),** with this `index.md` +
`_schema.md` + `_sources.md` + the two synthesis notes as the entry point:
- [`sources/`](sources/README.md) — **layer 1**, the immutable raw material you add (the
  AI reads but never edits); gitignored. The original book scans this study was first
  built from live, legacy, under `reference/damodaran_clc/` at the repo root.
- [`chapters/`](chapters/) — the 20 **by-chapter notes** (`cap_01 … cap_20`).
- [`wiki/`](wiki/index.md) — **layer 2**, the *by-concept* view (cross-linked concept
  articles).

**The central thesis.** A company's stage in the corporate life cycle —
start-up, young growth, high growth, mature, decline — should drive how its
corporate finance, valuation, investing approach, and management are framed.
There is no one-size-fits-all method; the right tool depends on where the firm
sits on the arc. This is directly relevant to the copilot's assumption layer,
which must pick projection methods that fit each company's stage.

## Two ways in
- 🧭 **Concept wiki** → [`wiki/index.md`](wiki/index.md) — 46 cross-linked concept articles (one concept per file), the LLM-wiki view (CLAUDE.md decision #9). Best for "what is X / how does X change by stage".
- 📖 **By chapter** → the 20 chapter notes below. Best for "what does the book say in chapter N".

## Synthesis (read first)
- [`00_framework_lifecycle.md`](00_framework_lifecycle.md) — the unifying life-cycle framework across all 20 chapters *(Stage 3)*
- [`application_to_copilot.md`](application_to_copilot.md) — life-cycle stage → per-line projection method, valuation approach, financing & payout policy; mapped to the engine's method cards *(Stage 3)*

## Chapters

### The Lead In
- [`cap_01_unifying_theory.md`](chapters/cap_01_unifying_theory.md) — A Search for a Unifying Theory
- [`cap_02_basics.md`](chapters/cap_02_basics.md) — The Basics of the Corporate Life Cycle
- [`cap_03_measures_determinants.md`](chapters/cap_03_measures_determinants.md) — Measures and Determinants
- [`cap_04_transitions.md`](chapters/cap_04_transitions.md) — Transitions

### Corporate Finance
- [`cap_05_corpfin_101.md`](chapters/cap_05_corpfin_101.md) — Corporate Finance 101: A Life Cycle Perspective
- [`cap_06_investing.md`](chapters/cap_06_investing.md) — Investing across the Life Cycle
- [`cap_07_financing.md`](chapters/cap_07_financing.md) — Financing across the Life Cycle
- [`cap_08_cash_return.md`](chapters/cap_08_cash_return.md) — Cash Return: Dividends and Buybacks

### Valuation
- [`cap_09_valuation_101.md`](chapters/cap_09_valuation_101.md) — Valuation 101
- [`cap_10_valuing_young.md`](chapters/cap_10_valuing_young.md) — Valuing Young and Start-up Businesses
- [`cap_11_valuing_high_growth.md`](chapters/cap_11_valuing_high_growth.md) — Valuing High Growth Businesses
- [`cap_12_valuing_mature.md`](chapters/cap_12_valuing_mature.md) — Valuing Mature Businesses
- [`cap_13_valuing_declining.md`](chapters/cap_13_valuing_declining.md) — Valuing Declining Businesses

### Investing
- [`cap_14_investment_philosophies.md`](chapters/cap_14_investment_philosophies.md) — Investment Philosophies 101
- [`cap_15_investing_youth.md`](chapters/cap_15_investing_youth.md) — Investing in Youth
- [`cap_16_investing_middle_age.md`](chapters/cap_16_investing_middle_age.md) — Investing in Middle Age
- [`cap_17_investing_old_age.md`](chapters/cap_17_investing_old_age.md) — Investing in Old Age

### Management
- [`cap_18_managing.md`](chapters/cap_18_managing.md) — Managing across the Life Cycle
- [`cap_19_fighting_aging.md`](chapters/cap_19_fighting_aging.md) — Fighting Aging
- [`cap_20_serenity.md`](chapters/cap_20_serenity.md) — In Search of Serenity

## Build status
- [x] Stage 1 — scaffold + raw material downloaded/extracted/rendered
- [x] Stage 2 — 20 chapter notes distilled
- [x] Stage 3 — synthesis notes
- [x] Stage 4 — QA pass (structure, cross-links, gitignore, verbatim-copy check)

## Compliance
Public sources only. Frameworks are described, never turned into investment
recommendations. No verbatim copying of the copyrighted source material —
distillation and paraphrase only, with provenance.
