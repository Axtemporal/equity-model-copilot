"""Sector coverage gate (Fase 1, step 1.5) + a standalone "what can we model?" report.

Deterministic, no AI: classifies a sector into a coverage tier by reading the disk — the
method card, the machine-readable delta schema, and the known build engines. Two uses:
  1. BLOCK the Fase 1 intake (with the list of what IS modelable) when the confirmed sector
     has no path downstream — so detection can never confirm a dead-end sector.
  2. Answer "o que dá pra modelar hoje?" as a plain CLI report.

Tiers (no sector hardcoded — derived from what exists on disk):
  A (full)    — card + delta: fully specified for intake + grounding.
  B (partial) — card only (no delta yet): intake degraded, the build falls back to generic.
  C (none)    — no card -> blocked.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from . import canonical_schema as cs

ROOT = Path(__file__).resolve().parent.parent
CARDS_DIR = ROOT / "knowledge" / "sector_modeling_rules" / "sectors"

TIER_FULL = "A"
TIER_PARTIAL = "B"
TIER_NONE = "C"


@dataclass
class Coverage:
    sector: str
    tier: str
    has_card: bool
    has_delta: bool

    @property
    def blocked(self) -> bool:
        return self.tier == TIER_NONE


class SectorCoverageError(Exception):
    """Raised by assert_supported when the sector has no knowledge base (Tier C)."""

    def __init__(self, sector: str, full: list[str], partial: list[str]):
        self.sector = sector
        self.full = full
        self.partial = partial
        super().__init__(
            f"no sector knowledge base for {sector!r}. Today you can model — "
            f"full (card + delta): {', '.join(full) or '(none)'}; "
            f"partial (card only, no machine schema): {', '.join(partial) or '(none)'}. "
            f"Pick one of these, or author the card + delta for {sector!r} first."
        )


def _has_card(sector: str) -> bool:
    return (CARDS_DIR / f"{sector}.md").exists()


def coverage(sector: str) -> Coverage:
    has_card = _has_card(sector)
    has_delta = cs.has_delta(sector)
    if not has_card:
        tier = TIER_NONE
    elif has_delta:
        tier = TIER_FULL
    else:
        tier = TIER_PARTIAL
    return Coverage(sector, tier, has_card, has_delta)


def available_cards() -> list[str]:
    """Slugs that have a method card (excludes schema/index files starting with '_')."""
    if not CARDS_DIR.exists():
        return []
    return sorted(p.stem for p in CARDS_DIR.glob("*.md") if not p.stem.startswith("_"))


def by_tier() -> dict[str, list[str]]:
    """{'A': [...], 'B': [...]} over every sector that has a card."""
    out: dict[str, list[str]] = {TIER_FULL: [], TIER_PARTIAL: []}
    for sector in available_cards():
        cov = coverage(sector)
        if cov.tier in out:
            out[cov.tier].append(sector)
    return out


def assert_supported(sector: str) -> Coverage:
    """The Fase 1 gate. Return the Coverage if modelable; raise SectorCoverageError if blocked."""
    cov = coverage(sector)
    if cov.blocked:
        tiers = by_tier()
        raise SectorCoverageError(sector, tiers[TIER_FULL], tiers[TIER_PARTIAL])
    return cov


def report() -> str:
    """Human-readable 'what can we model today?' summary."""
    tiers = by_tier()
    lines = ["Sector coverage:"]
    lines.append(f"  [A] full (card + delta): {', '.join(tiers[TIER_FULL]) or '(none)'}")
    lines.append(f"  [B] partial (card only, no machine schema): {', '.join(tiers[TIER_PARTIAL]) or '(none)'}")
    return "\n".join(lines)


if __name__ == "__main__":
    print(report())
