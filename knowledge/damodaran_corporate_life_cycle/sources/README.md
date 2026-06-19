# sources/ — raw material layer (drop zone)

This is **layer 1** of the three-layer llm-wiki (CLAUDE.md decision #9): the **immutable
raw material** the wiki and chapter notes are distilled from. **You add files here** as
you expand and deepen the Damodaran study; the AI **reads but never edits** this layer.

```
damodaran_corporate_life_cycle/
├── sources/    ← layer 1: raw material (this folder) — you add, AI reads only
├── chapters/   ← the 20 by-chapter notes (cap_01 … cap_20)
├── wiki/       ← layer 2: AI-distilled concept articles, cross-linked, provenance
└── index.md, _schema.md, _sources.md, 00_framework_lifecycle.md, application_to_copilot.md
                ← entry point + contract + bibliography + synthesis notes
```

## What goes here

Damodaran papers, blog posts, datasets, lecture slides, valuation spreadsheets — the
verifiable public material behind each claim in the chapter notes and wiki.

> **Legacy raw location.** The original book scans this study was first built from live in
> [`reference/damodaran_clc/`](../../../reference/damodaran_clc/) at the repo root
> (`img/` page scans + `text/ChNN.txt`), gitignored for copyright. The wiki's Provenance
> blocks point there (`reference/damodaran_clc/text/ChNN.txt`). New raw material should be
> dropped **here** in `sources/` going forward; the legacy `reference/` scans stay put.

## Rules

- **Immutable & read-only for the AI.** Research/distillation rounds *read* these to
  ground and verify claims; they never rewrite them. You are the only one who adds here.
- **Gitignored for copyright.** Everything under `sources/` is in `.gitignore` (only this
  `README.md` is tracked) — same rule as `reference/`, `Example models/`, `Knowledge Base/`.
- **Provenance, not copying.** Wiki articles and chapter notes **distil** from these and
  cite them (by hyperlink + `[[cap_NN]]`); never paste verbatim.
- **No investment advice.** Frameworks described, never turned into a recommendation.
