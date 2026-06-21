"""Period-grid normalization (Fase 1, step 1.3b) — sector-agnostic, pure header logic.

Reads arbitrary period headers and reorders them into the canonical interleaved grid
(1Q 2Q 3Q 4Q ANO 1Q 2Q 3Q 4Q ANO …), tolerant of how the analyst laid them out: quarters and
annuals in any order, in separate blocks, with a blank gap column between them, and in common
spellings (1Q23, 1Q2023, Q1 2023, Q1'23, 1T23 (PT), FY2023, FY23, 2023, 2023A, 12M23).

Canonical tokens: a quarter is "{q}Q{yy}" (e.g. "1Q23"); a year is "{yyyy}" (e.g. "2023").
Columns before the first period (label/unit) are metadata and ignored. A column inside the
period region whose header does not parse is DROPPED if empty (a separator/blank) but FLAGGED
if it carries data — never silently discarded.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

# quarter: 1Q23 / 1Q2023 / 1T23 / 1 Q 23 / 1Q'23   (group1 = quarter, group2 = year)
_Q_LEADING = re.compile(r"^([1-4])\s*[QT]\s*['/ ]?\s*(\d{2}|\d{4})$", re.IGNORECASE)
# quarter: Q1 2023 / Q1'23 / T1 2023               (group1 = quarter, group2 = year)
_Q_TRAILING = re.compile(r"^[QT]\s*([1-4])\s*['/ ]?\s*(\d{2}|\d{4})$", re.IGNORECASE)
# annual, 4-digit: 2023 / FY2023 / FY 2023 / 2023A / 12M2023
_A_FULL = re.compile(r"^(?:FY|12M|CY|EX)?\s*'?(\d{4})\s*[AE]?$", re.IGNORECASE)
# annual, 2-digit: requires a disambiguating prefix so a bare '23' is not a period
_A_SHORT = re.compile(r"^(?:FY|12M|CY)\s*'?(\d{2})\s*[AE]?$", re.IGNORECASE)


def _year4(raw: str) -> int:
    n = int(raw)
    return n if n >= 1000 else 2000 + n


@dataclass(frozen=True)
class Period:
    token: str         # canonical "1Q23" or "2023"
    year: int          # 4-digit
    quarter: int       # 1..4, or 0 for an annual column

    @property
    def is_annual(self) -> bool:
        return self.quarter == 0

    @property
    def order_key(self) -> tuple[int, int]:
        # within a year: 1Q,2Q,3Q,4Q then the annual (rank 5) — the canonical interleave
        return (self.year, self.quarter if self.quarter else 5)


def parse_period(header) -> Period | None:
    """Parse one header cell into a canonical Period, or None if it is not a period."""
    if header is None:
        return None
    s = str(header).strip()
    if not s:
        return None
    for pat in (_Q_LEADING, _Q_TRAILING):
        m = pat.match(s)
        if m:
            q, year = int(m.group(1)), _year4(m.group(2))
            return Period(f"{q}Q{year % 100:02d}", year, q)
    for pat in (_A_FULL, _A_SHORT):
        m = pat.match(s)
        if m:
            year = _year4(m.group(1))
            return Period(f"{year}", year, 0)
    return None


@dataclass
class GridResult:
    order: list[str] = field(default_factory=list)        # canonical tokens, interleaved order
    col_to_token: dict = field(default_factory=dict)      # original column key -> canonical token
    dropped: list = field(default_factory=list)           # empty/separator headers removed
    flagged: list = field(default_factory=list)           # unparseable headers that carry DATA


def normalize_grid(headers) -> GridResult:
    """Reorder period columns into the canonical interleaved grid.

    `headers` is an iterable of (column_key, raw_header, has_data). column_key must be sortable
    (a column index). Columns before the first period column are treated as metadata and ignored.
    """
    parsed = [(key, raw, has_data, parse_period(raw)) for key, raw, has_data in headers]
    period_keys = [key for key, _raw, _hd, p in parsed if p is not None]
    if not period_keys:
        return GridResult()
    first = min(period_keys)

    col_to_token: dict = {}
    uniq: dict[str, Period] = {}
    dropped, flagged = [], []
    for key, raw, has_data, p in parsed:
        if p is not None:
            col_to_token[key] = p.token
            uniq.setdefault(p.token, p)
        elif key < first:
            continue                      # leading metadata (label / unit columns)
        elif has_data:
            flagged.append(raw)           # non-period header with data — surfaced, not placed
        else:
            dropped.append(raw)           # blank / separator column
    order = [tok for tok, _p in sorted(uniq.items(), key=lambda kp: kp[1].order_key)]
    return GridResult(order=order, col_to_token=col_to_token, dropped=dropped, flagged=flagged)


def missing_quarters(input_last: str, actual_last: str) -> list[str]:
    """Quarter tokens strictly AFTER `input_last` up to and including `actual_last`.

    The deterministic half of the staleness check (Fase 1, step 1.8b): given the input's last
    reported quarter and the company's actual last released quarter (looked up + cited by the AI),
    enumerate the gap. Empty if the input is current (or ahead), or if either token isn't a quarter.
    """
    a, b = parse_period(input_last), parse_period(actual_last)
    if not a or not b or a.is_annual or b.is_annual:
        return []
    out, year, quarter = [], a.year, a.quarter
    while (year, quarter) != (b.year, b.quarter):
        quarter += 1
        if quarter > 4:
            quarter, year = 1, year + 1
        if (year, quarter) > (b.year, b.quarter):
            break
        out.append(f"{quarter}Q{year % 100:02d}")
    return out
