"""CLI: python -m engine.harness <model.xlsx> [<model.xlsx> ...]

Recalculates each generated model and prints a pass/fail report of its invariants.
Exits non-zero if any model fails a hard invariant (CI-friendly).
"""
from __future__ import annotations

import argparse
import sys

from . import verify_model
from .recalc import RecalcError


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="engine.harness",
        description="Recalculate and verify a generated model workbook.",
    )
    parser.add_argument("models", nargs="+", help="path(s) to a generated .xlsx model")
    parser.add_argument("--backend", default="formulas", help="recalc backend (default: formulas)")
    args = parser.parse_args(argv)

    try:  # Windows consoles default to cp1252; keep output robust to any symbol
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass

    overall_ok = True
    for path in args.models:
        print(f"\n=== {path} ===")
        try:
            report = verify_model(path, backend=args.backend)
        except RecalcError as exc:
            print(f"  RECALC ERROR: {exc}")
            overall_ok = False
            continue
        print(f"  backend: {report.backend_used} | {report.summary()}")
        for result in report.results:
            mark = "ok" if result.passed else ("!!" if result.severity.value == "FAIL" else "~~")
            print(f"  [{mark}] {result.name}: {result.message}")
            if not result.passed:
                for cell in result.failing_cells[:8]:
                    print(f"          - {cell}")
                if len(result.failing_cells) > 8:
                    print(f"          ... and {len(result.failing_cells) - 8} more")
        overall_ok = overall_ok and report.ok
    return 0 if overall_ok else 1


if __name__ == "__main__":
    sys.exit(main())
