"""Fase 1 mapping manifest — the audited record of how a raw input became a canonical one.

Every flattened input line reaches exactly one terminal disposition; the manifest carries that,
the resolution method + confidence + provenance, the per-slot content-sufficiency matrix, and
the currency/staleness block. Written to disk (models/<company>/fase1_manifest.yaml) so the
Fase 1 PASS is read from artifacts, never from conversation memory.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field

import yaml

# line dispositions (every flattened line ends in exactly one)
MAPPED = "mapped"
DECLARED_ZERO = "declared_zero"
CONTEXTUAL = "contextual"
ESCALATED = "escalated"
DROPPED = "dropped"
PENDING = "pending"

# required-slot content-sufficiency statuses
SLOT_MAPPED = "mapped"
SLOT_DECLARED_ZERO = "declared_zero"
SLOT_ABSENT = "absent"


AI_WEB_FETCH = "ai_web_fetch"   # method tag for an opt-in web-fetched scalar (provenance enforced)


@dataclass
class LineRecord:
    raw_label: str
    sheet: str
    cell: str | None = None
    unit: str | None = None
    values: dict = field(default_factory=dict)      # period -> value
    canonical: str | None = None
    method: str = "unresolved"                       # exact|alias|fuzzy|ai|ai_web_fetch|unresolved
    confidence: float = 0.0
    role: str | None = None
    disposition: str = PENDING
    provenance: str = ""
    # provenance for an AI web-fetched value (enforced by the writer; never silently kept)
    source_url: str = ""
    source_date: str = ""
    user_accepted: bool = False


@dataclass
class SlotCoverage:
    slot: str
    sheet: str
    status: str                                       # mapped|declared_zero|absent


@dataclass
class Manifest:
    company: str
    sector: str | None
    lines: list = field(default_factory=list)         # list[LineRecord]
    coverage: list = field(default_factory=list)      # list[SlotCoverage]
    residual: list = field(default_factory=list)      # raw labels no pass resolved
    currency: dict = field(default_factory=dict)      # filled by step 1.8b (staleness)

    @property
    def missing_required(self) -> list:
        return [c for c in self.coverage if c.status == SLOT_ABSENT]

    @property
    def content_sufficient(self) -> bool:
        return not self.missing_required

    def rollups(self) -> dict:
        """{canonical: [LineRecord]} where >1 record mapped to the same canonical (summed at
        write). Surfaced so the user/AI confirms the sum (and catches an aggregate-plus-its-
        components double-count) — the checksum-vs-reported-subtotal safeguard."""
        groups: dict[str, list] = {}
        for record in self.lines:
            if record.canonical and record.disposition == MAPPED:
                groups.setdefault(record.canonical, []).append(record)
        return {canonical: recs for canonical, recs in groups.items() if len(recs) > 1}

    def material_residue(self) -> list:
        """Residual lines that carry numeric data — candidates for user disposition (vs noise
        like section headers / subtotal labels that carry no values)."""
        residual = set(self.residual)
        return [r for r in self.lines if r.raw_label in residual
                and any(isinstance(v, (int, float)) for v in r.values.values())]

    def to_dict(self) -> dict:
        return {
            "company": self.company,
            "sector": self.sector,
            "content_sufficient": self.content_sufficient,
            "missing_required": [c.slot for c in self.missing_required],
            "lines": [asdict(line) for line in self.lines],
            "coverage": [asdict(c) for c in self.coverage],
            "residual": list(self.residual),
            "currency": dict(self.currency),
        }

    def save(self, path: str) -> str:
        with open(path, "w", encoding="utf-8") as handle:
            yaml.safe_dump(self.to_dict(), handle, allow_unicode=True, sort_keys=False)
        return path
