"""End-to-end pipeline: validate input -> build model -> verify model.

The single entry point the CLI and the future MCP / Phase-B bridge call. Keeps the cheap
fail-fast input validation in front of the build, and the heavy recalc verification after.
"""
from __future__ import annotations

import importlib
import importlib.util

import openpyxl

from . import verify_model
from .report import Report
from .validator import assert_valid_input, detect_sector


def _select_builder(sector: str | None):
    """Pick the build engine for a sector WITHOUT hardcoding any sector.

    A sector with a dedicated engine module (engine/build_model_<slug>.py) uses it; every other
    sector uses the default engine, which builds bottom-up when per-asset data is present and a
    generic top-down layer otherwise. Adding a dedicated build for a new sector = drop a
    build_model_<slug>.py file; no change here.
    """
    if sector:
        module = f"engine.build_model_{sector}"
        if importlib.util.find_spec(module):
            return importlib.import_module(module)
    from engine import build_model
    return build_model


def build_and_verify(
    input_path: str,
    output_path: str,
    *,
    sector: str | None = None,
    backend: str = "formulas",
    verify: bool = True,
    assumptions_log=None,
) -> tuple[str, Report | None]:
    """Validate the input, build the model for its sector, apply approved assumptions, verify.

    `assumptions_log` may be a path to a YAML log or an AssumptionsLog; its Approved entries
    override the seeded Premises cells (merge by line + period) and render the Assumptions tab.
    Returns (output_path, verification Report or None). Raises InputValidationError if the
    input is malformed (before wasting a build).
    """
    assert_valid_input(input_path, sector)
    sector = sector or detect_sector(openpyxl.load_workbook(input_path))
    builder = _select_builder(sector)
    builder.main(input_path, output_path)
    if assumptions_log is not None:
        from ..assumptions import AssumptionsLog, apply_to_model

        log = (assumptions_log if isinstance(assumptions_log, AssumptionsLog)
               else AssumptionsLog.load(assumptions_log))
        apply_to_model(output_path, log)
    report = verify_model(output_path, backend=backend) if verify else None
    return output_path, report


if __name__ == "__main__":
    import argparse
    import sys

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass

    from .recalc import RecalcError
    from .validator import InputValidationError

    parser = argparse.ArgumentParser(
        prog="engine.harness.pipeline",
        description="Validate an input, build its sector model, and verify it.",
    )
    parser.add_argument("input", help="filled input .xlsx")
    parser.add_argument("output", help="path to write the model .xlsx")
    parser.add_argument("--sector", default=None,
                        help="optional sector slug; auto-detected from the input when omitted")
    parser.add_argument("--backend", default="formulas")
    parser.add_argument("--no-verify", action="store_true")
    args = parser.parse_args()

    try:
        out_path, report = build_and_verify(
            args.input, args.output, sector=args.sector,
            backend=args.backend, verify=not args.no_verify,
        )
    except InputValidationError as exc:
        print("INPUT INVALID:")
        for problem in exc.problems:
            print("  -", problem)
        sys.exit(2)
    except RecalcError as exc:
        print("RECALC FAILED:")
        print("  -", exc)
        print("  → rode `python -m engine.check_env` para diagnosticar o ambiente de recálculo")
        sys.exit(3)

    print(f"built: {out_path}")
    if report is not None:
        print(report.summary())
        for result in report.results:
            mark = "ok" if result.passed else ("!!" if result.severity.value == "FAIL" else "~~")
            print(f"  [{mark}] {result.name}: {result.message}")
        sys.exit(0 if report.ok else 1)
