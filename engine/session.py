"""Resumable session state for the assumption session (foundation item 5).

The save-game: where the analyst is (cursor), the chat transcript per line, and in-progress
working values — persisted to disk so a long line-by-line session survives a browser refresh,
a restart, or being picked up tomorrow. Decisions live in the assumptions log; this holds only
the ephemeral cursor and discussion, so the session resumes exactly where it paused.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field

import yaml


@dataclass
class SessionState:
    path: str | None = None
    current_index: int = 0
    chats: dict = field(default_factory=dict)    # line_item -> [{"role": ..., "text": ...}]
    working: dict = field(default_factory=dict)  # line_item -> {period: value} (in-progress)
    meta: dict = field(default_factory=dict)     # line_item -> {method, source, source_date, rationale}

    @classmethod
    def load(cls, path: str | None) -> "SessionState":
        if path and os.path.exists(path):
            with open(path, encoding="utf-8") as handle:
                data = yaml.safe_load(handle) or {}
            return cls(
                path=path,
                current_index=int(data.get("current_index", 0)),
                chats={k: list(v) for k, v in (data.get("chats") or {}).items()},
                working={k: {str(p): val for p, val in (vals or {}).items()}
                         for k, vals in (data.get("working") or {}).items()},
                meta={k: dict(v) for k, v in (data.get("meta") or {}).items()},
            )
        return cls(path=path)

    def save(self, path: str | None = None) -> str:
        path = path or self.path
        if not path:
            raise ValueError("no path to save the session state")
        payload = {"current_index": self.current_index, "chats": self.chats,
                   "working": self.working, "meta": self.meta}
        with open(path, "w", encoding="utf-8") as handle:
            yaml.safe_dump(payload, handle, allow_unicode=True, sort_keys=False)
        return path

    def set_meta(self, line_item: str, fields: dict) -> None:
        self.meta.setdefault(line_item, {}).update({k: v for k, v in fields.items() if v})

    def get_meta(self, line_item: str) -> dict:
        return self.meta.get(line_item, {})

    def add_message(self, line_item: str, role: str, text: str) -> None:
        self.chats.setdefault(line_item, []).append({"role": role, "text": text})

    def get_chat(self, line_item: str) -> list[dict]:
        return self.chats.get(line_item, [])

    def set_working(self, line_item: str, values: dict) -> None:
        self.working.setdefault(line_item, {}).update({str(k): v for k, v in values.items()})

    def get_working(self, line_item: str) -> dict:
        return self.working.get(line_item, {})
