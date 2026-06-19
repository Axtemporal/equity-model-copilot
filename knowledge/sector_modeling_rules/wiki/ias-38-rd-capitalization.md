---
concept: ias-38-rd-capitalization
title: IAS 38 vs ASC 730 — R&D / Software Capitalization
theme: accounting-standard
applies_to: [tech_saas, auto]
confidence: verified
status: draft
---

# IAS 38 vs ASC 730 — R&D / Software Capitalization

**What it is.** Under **IAS 38** (IFRS) research is expensed but **development is
capitalized once all six criteria are met**; under **US-GAAP ASC 730** R&D is **expensed
as incurred** (with separate ASC 350-40 rules for internal-use software) — so the same
spending produces a different asset base and margin profile depending on the issuer's
framework, which the model must read rather than assume.

## Core idea

R&D-heavy companies look materially different on the two frameworks:

- **IAS 38 (IFRS):** **research is expensed**; **development is capitalized only if all
  six criteria** are met — technical feasibility, intention to complete, ability to
  use/sell, probable future economic benefits, adequate resources to complete, and
  reliable measurement of the cost. Capitalized development becomes an intangible
  amortized over its useful life.
- **ASC 730 (US-GAAP):** **R&D expensed as incurred** — no development-capitalization
  judgment. Internal-use software has its own capitalization regime under **ASC 350-40**.

The capitalization choice **materially changes reported margins and the asset base**: an
IFRS filer capitalizing development shows higher near-term margins and an amortizing
intangible; a US-GAAP filer expensing it shows lower margins and no such asset.

## Applies to sectors

- **Tech / SaaS** — capitalized-software policy drives the intangible asset and its
  amortization; read the issuer's framework before modeling margins.
- **Auto / OEM** — development capitalization matters for EV/autonomy spend. **Tesla
  reports under US-GAAP / ASC 730** (R&D expensed as incurred), so there is no
  capitalized-development asset to model for it.

Both cards share this overlay (and the software deferred-revenue overlay), so it lives in
one article.

## Mechanics / formulas

- IFRS: research → expense; development meeting the six criteria → capitalize as
  intangible → amortize over useful life.
- US-GAAP: R&D → expense as incurred; internal-use software per ASC 350-40 stage-based
  capitalization.

## Modeling implications

- The copilot must **identify the issuer's framework** (IFRS vs US-GAAP) before proposing
  R&D / software treatment, because it changes the margin bridge and the intangible
  schedule.
- For an IFRS filer, build a **capitalized-development schedule** with amortization; for a
  US-GAAP filer (e.g. Tesla), R&D flows straight through opex with no such asset.

## Pitfalls & nuances

- **Do NOT assume a capitalization policy** — IAS 38 and ASC 730 differ; comparing
  margins across a US-GAAP and an IFRS peer without normalizing is misleading.
- Distinguish development (potentially capitalized under IFRS) from research (always
  expensed) — the six criteria are the gate.

## Related concepts

- [[ifrs-15-performance-obligations]] — the revenue-recognition overlay shared with these sectors
- [[arr-roll-forward]] — the SaaS revenue engine the capitalized cost supports
- [[saas-unit-economics]] — metrics that interact with capitalized vs expensed cost
- [[tech_saas]] / [[auto]] — the two cards this overlay governs

## Provenance
- Method cards: [[tech_saas]], [[auto]]
- Sources: [KPMG-RD-2025 — R&D costs: IFRS Accounting Standards vs US GAAP (KPMG, 2025)](https://kpmg.com/us/en/articles/2025/rd-costs-ifrs-accounting-standards-us-gaap.html)
- Confidence: ✅ verified (3-0)
