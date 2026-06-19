"""3-pass label resolver (Fase 1, step 1.3): map raw input labels to canonical schema labels.

Deterministic muscle first, AI only on the residue:
  pass 1  exact — normalized exact match against the sector's canonical label set.
  pass 2  alias — the curated/learned bilingual alias dictionary (PT/EN, report variants).
  pass 3  fuzzy — difflib ratio above a FIXED cutoff (a typo catcher only, not the workhorse).

What survives all three is the residual the AI semantic layer (step 1.3b) resolves; the routing
to the LLM is a Python threshold here, never an LLM judgment about "close enough".
"""
from __future__ import annotations

import difflib
from dataclasses import dataclass

from . import canonical_schema as cs
from .alias_dictionary import AliasDictionary

FUZZY_CUTOFF = 0.86  # fixed policy: below this a line is residual, not a guess

EXACT = "exact"
ALIAS = "alias"
FUZZY = "fuzzy"
UNRESOLVED = "unresolved"


@dataclass
class Match:
    raw: str
    canonical: str | None
    method: str           # exact | alias | fuzzy | unresolved
    score: float          # 1.0 for exact/alias, the ratio for fuzzy, 0.0 for unresolved
    sheet: str | None = None


def _targets(sector: str) -> dict[str, tuple[str, str]]:
    """{normalized_canonical: (canonical_label, sheet)} for the sector's required labels."""
    out: dict[str, tuple[str, str]] = {}
    for sheet, labels in cs.required_labels(sector).items():
        for canonical in labels:
            out[cs.normalize(canonical)] = (canonical, sheet)
    return out


def _sheet_of(canonical: str, targets: dict[str, tuple[str, str]]) -> str | None:
    return next((sheet for c, sheet in targets.values() if c == canonical), None)


def resolve_label(raw: str, targets: dict[str, tuple[str, str]],
                  aliases: AliasDictionary, *, cutoff: float = FUZZY_CUTOFF) -> Match:
    key = cs.normalize(raw)
    if key in targets:
        canonical, sheet = targets[key]
        return Match(raw, canonical, EXACT, 1.0, sheet)

    canonical = aliases.resolve(raw)
    if canonical is not None:
        return Match(raw, canonical, ALIAS, 1.0, _sheet_of(canonical, targets))

    close = difflib.get_close_matches(key, list(targets), n=1, cutoff=cutoff)
    if close:
        canonical, sheet = targets[close[0]]
        ratio = difflib.SequenceMatcher(None, key, close[0]).ratio()
        return Match(raw, canonical, FUZZY, ratio, sheet)

    return Match(raw, None, UNRESOLVED, 0.0, None)


def resolve(raw_labels, sector: str, *, aliases: AliasDictionary | None = None,
            cutoff: float = FUZZY_CUTOFF) -> list[Match]:
    """Resolve every raw label against the sector's canonical schema (3 deterministic passes)."""
    targets = _targets(sector)
    aliases = aliases or AliasDictionary.load()
    return [resolve_label(raw, targets, aliases, cutoff=cutoff) for raw in raw_labels]


def residual(matches: list[Match]) -> list[str]:
    """Raw labels no deterministic pass resolved — the set the AI semantic layer handles."""
    return [m.raw for m in matches if m.method == UNRESOLVED]
