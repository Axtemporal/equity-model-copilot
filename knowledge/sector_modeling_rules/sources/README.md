# sources/ — raw material layer (drop zone)

This is **layer 1** of the three-layer llm-wiki (CLAUDE.md decision #9): the **immutable
raw material** the wiki is distilled from. One subfolder per sector. **You add files
here** as you expand the sector study and deepen existing sectors; the AI **reads but
never edits** this layer.

```
sector_modeling_rules/
├── sources/   ← layer 1: raw material (this folder) — you add, AI reads only
├── sectors/   ← the 12 by-sector method cards (the "by-sector" view)
├── wiki/      ← layer 2: AI-distilled concept articles, cross-linked, provenance
└── index.md, _schema.md, _sources.md   ← entry point + contract + bibliography
```

## What goes here

Earnings releases, conference-call transcripts, equity-research reports, regulatory
texts (ANP, ANS, MEC, ANM/CFEM, IFRS/CPC standards), investor presentations, sector
studies — the verifiable primary/secondary material behind each claim in the wiki.

Drop them under the matching sector subfolder:

```
sources/oil_and_gas/        sources/metals_mining/      sources/fuel_distribution/
sources/petrochemicals/     sources/steel/              sources/agriculture/
sources/agri_inputs/        sources/pulp_paper/         sources/healthcare/
sources/education/          sources/tech_saas/          sources/auto/
```

**Adding a new sector?** Create `sources/<new_sector>/`, add a row to
[`../wiki/_concepts.md`](../wiki/_concepts.md) for each new concept, then the wiki
article(s) and (optionally) a new method card. Keep slugs consistent across all three.

## Rules

- **Immutable & read-only for the AI.** The assumption session and research rounds
  *read* these to ground and verify claims; they never rewrite them. You are the only
  one who adds/removes files here.
- **Gitignored for copyright.** Everything under `sources/` is in `.gitignore` (only this
  `README.md` and the per-sector `.gitkeep` skeleton are tracked). Proprietary releases,
  transcripts and paywalled research must **never** be committed — same rule as
  `Example models/`, `Knowledge Base/`, and `reference/`.
- **Provenance, not copying.** Wiki articles **distil** from these files and cite them in
  their Provenance block (by source ID in [`../_sources.md`](../_sources.md) + hyperlink
  where public); they never paste verbatim. When you add a file, if it backs a wiki
  claim, add/point to an entry in `../_sources.md`.
- **Method over numbers.** Point-in-time figures in these files are dated illustrations,
  never values to hardcode into the model.

## How a research round uses this

A deep-research / assumption round reads the relevant `sources/<sector>/` files first,
then proposes or upgrades a claim, tagging confidence (✅ verified / 🟡 seed /
⚠️ to-verify) against what the source actually supports — grounding in verifiable
material instead of model memory, which is the whole point of the layer.
