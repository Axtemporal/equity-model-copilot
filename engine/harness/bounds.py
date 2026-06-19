"""Value sanity bounds — the unit check (Fase 1, step 1.7) and the post-build value gate (4.4).

Deterministic and hallucination-free: the LLM never does this arithmetic, it only explains a
flag. Two checks:
  - unit_outliers(series): flags a value that deviates by orders of magnitude from the line's
    OWN historical median — the "reported in R$ '000 where the template expects R$ mn" (~1000x)
    error, caught without any external baseline.
  - within(value, lo, hi): a generic range guard for the post-build value-sanity gate.
"""
from __future__ import annotations

from dataclasses import dataclass
from statistics import median

UNIT_RATIO_FLAG = 100.0  # >= this fold vs the series median (or <= its reciprocal) => suspect


@dataclass
class Outlier:
    period: str
    value: float
    median: float
    ratio: float


def _numeric(series: dict) -> list[tuple[str, float]]:
    out = []
    for period, value in series.items():
        if isinstance(value, (int, float)) and value == value:  # exclude NaN
            out.append((str(period), float(value)))
    return out


def unit_outliers(series: dict, *, ratio_flag: float = UNIT_RATIO_FLAG) -> list[Outlier]:
    """Periods whose value is ~`ratio_flag`x off the line's own median magnitude (likely a unit
    error). Needs >= 3 non-zero numeric points to have a stable baseline; otherwise returns []."""
    points = [(p, v) for p, v in _numeric(series) if v != 0]
    if len(points) < 3:
        return []
    med = median(abs(v) for _, v in points)
    if med == 0:
        return []
    flagged = []
    for period, value in points:
        ratio = abs(value) / med
        if ratio >= ratio_flag or ratio <= 1.0 / ratio_flag:
            flagged.append(Outlier(period, value, med, ratio))
    return flagged


def within(value, lo: float | None = None, hi: float | None = None) -> bool:
    """True iff value is present and inside [lo, hi] (either bound optional)."""
    if value is None:
        return False
    if lo is not None and value < lo:
        return False
    if hi is not None and value > hi:
        return False
    return True
