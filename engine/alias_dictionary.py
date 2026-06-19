"""Bilingual alias dictionary — the deterministic muscle of Fase 1 matching (resolver pass 2).

Two layers, by governance:
  - GLOBAL (curated): engine/alias_dictionary.yaml — reviewed PT/EN spellings, canonical -> [raw].
  - OVERRIDE (learned): a per-session/company YAML the AI's confirmed mappings append to via
    add(). Kept separate so a wrong learned alias can be reverted without touching the muscle,
    and so a one-off company spelling never silently rewrites matching for everyone.

resolve() consults override first, then global. add() is the ONLY write path: it normalizes
both sides with canonical_schema.normalize (the same normalizer the resolver uses), rejects a
raw that already maps to a DIFFERENT canonical, and records provenance — so the model proposes a
pair but Python validates and writes it (never the LLM editing the file directly).
"""
from __future__ import annotations

from pathlib import Path

import yaml

from . import canonical_schema as cs

GLOBAL_PATH = Path(__file__).resolve().parent / "alias_dictionary.yaml"


class AliasConflictError(ValueError):
    """Raised when add() would map a raw label that already resolves to a different canonical."""


def _load_layer(path: Path) -> dict[str, str]:
    """Read a {canonical: [raw, ...]} YAML into a normalized {normalize(raw): canonical} map."""
    if not path or not path.exists():
        return {}
    with open(path, encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    out: dict[str, str] = {}
    for canonical, spellings in (data.get("aliases", {}) or {}).items():
        for raw in spellings or []:
            out[cs.normalize(raw)] = canonical
    return out


class AliasDictionary:
    """Resolve raw labels to canonical via override-then-global; learn new pairs into override."""

    def __init__(self, global_path: Path = GLOBAL_PATH, override_path: Path | None = None):
        self.global_path = Path(global_path)
        self.override_path = Path(override_path) if override_path else None
        self._global = _load_layer(self.global_path)
        self._override = _load_layer(self.override_path) if self.override_path else {}

    @classmethod
    def load(cls, override_path: Path | None = None) -> "AliasDictionary":
        return cls(GLOBAL_PATH, override_path)

    def resolve(self, raw: str) -> str | None:
        """Canonical label for a raw spelling (override wins over global), or None."""
        key = cs.normalize(raw)
        if not key:
            return None
        return self._override.get(key) or self._global.get(key)

    def add(self, raw: str, canonical: str, *, provenance: str = "", confirmed_by: str = "") -> None:
        """Append an AI-confirmed alias to the OVERRIDE layer (requires an override_path).

        Rejects a raw that already resolves to a different canonical (a silent mis-route guard).
        A re-assertion of an existing pair is a no-op.
        """
        if self.override_path is None:
            raise ValueError("add() needs an override_path (the learned layer to write to)")
        key = cs.normalize(raw)
        if not key:
            raise ValueError("cannot add an empty raw label")
        existing = self.resolve(raw)
        if existing and existing != canonical:
            raise AliasConflictError(
                f"{raw!r} already maps to {existing!r}; refusing to remap to {canonical!r}"
            )
        self._override[key] = canonical
        self._append_to_file(raw, canonical, provenance=provenance, confirmed_by=confirmed_by)

    def _append_to_file(self, raw: str, canonical: str, *, provenance: str, confirmed_by: str) -> None:
        path = self.override_path
        data = {}
        if path.exists():
            with open(path, encoding="utf-8") as handle:
                data = yaml.safe_load(handle) or {}
        aliases = data.setdefault("aliases", {})
        aliases.setdefault(canonical, [])
        if raw not in aliases[canonical]:
            aliases[canonical].append(raw)
        prov = data.setdefault("_provenance", [])
        prov.append({"raw": raw, "canonical": canonical,
                     "confirmed_by": confirmed_by, "note": provenance})
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            yaml.safe_dump(data, handle, allow_unicode=True, sort_keys=False)
