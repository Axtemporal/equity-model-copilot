"""Recalc backends.

openpyxl writes formulas as *text* and never computes them, so a generated model
carries no values until a real calculator runs over it. `recalc()` produces a
computed copy; `recalc_workbook()` returns it loaded with `data_only=True` so the
invariants can read the numbers.

Backends are pluggable. `formulas` (pure Python, pip-only) is the working default
and has been verified to reproduce the balance check to ~5e-12 on the fixtures.
LibreOffice headless (forced UNO `calculateAll`) is the intended high-fidelity
cross-check and slots in here as a second backend without touching callers.
"""
from __future__ import annotations

import glob
import os
import shutil
import subprocess
import tempfile
import warnings

import openpyxl


class RecalcError(RuntimeError):
    """A recalc backend failed (distinct from a model invariant violation)."""


def _formulas_backend(in_path: str, out_path: str) -> str:
    try:
        import formulas
    except ImportError as exc:  # pragma: no cover - environment guard
        raise RecalcError(
            "the 'formulas' library is not installed (pip install formulas)"
        ) from exc

    warnings.filterwarnings("ignore")
    try:
        model = formulas.ExcelModel().loads(in_path).finish()
        model.calculate()
        # write() ignores any filename, writes one file per workbook into dirpath
        # named as the UPPERCASED source basename, and returns a dict. So we write
        # into a throwaway dir and move the single produced file to out_path.
        tmpdir = tempfile.mkdtemp(prefix="emc_recalc_")
        try:
            model.write(dirpath=tmpdir)
            produced = list(
                {*glob.glob(os.path.join(tmpdir, "*.xlsx")),
                 *glob.glob(os.path.join(tmpdir, "*.XLSX"))}
            )
            if not produced:
                raise RecalcError("formulas.write() produced no .xlsx file")
            if os.path.exists(out_path):
                os.remove(out_path)
            shutil.move(produced[0], out_path)
        finally:
            shutil.rmtree(tmpdir, ignore_errors=True)
        return out_path
    except RecalcError:
        raise
    except Exception as exc:  # noqa: BLE001 - surface any backend failure uniformly
        raise RecalcError(f"formulas backend failed: {exc!r}") from exc


_SOFFICE_CANDIDATES = [
    r"C:\Program Files\LibreOffice\program\soffice.exe",
    r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
    "soffice",
    "soffice.bin",
]

# Forces "Always recalculate on load" for OOXML and ODF, so the convert recomputes the
# formula-only workbook instead of preserving its (empty) cache.
_RECALC_XCU = """<?xml version="1.0" encoding="UTF-8"?>
<oor:items xmlns:oor="http://openoffice.org/2001/registry">
 <item oor:path="/org.openoffice.Office.Calc/Formula/Load"><prop oor:name="OOXMLRecalcMode" oor:op="fuse"><value>0</value></prop></item>
 <item oor:path="/org.openoffice.Office.Calc/Formula/Load"><prop oor:name="ODFRecalcMode" oor:op="fuse"><value>0</value></prop></item>
</oor:items>
"""


def _find_soffice():
    for candidate in _SOFFICE_CANDIDATES:
        if os.path.isabs(candidate):
            if os.path.exists(candidate):
                return candidate
        else:
            found = shutil.which(candidate)
            if found:
                return found
    return None


def _libreoffice_backend(in_path: str, out_path: str) -> str:
    """Authoritative recalc via LibreOffice headless (Excel-compatible calc engine).

    NOT yet verified on this machine (LibreOffice is not installed). Slots in as a
    high-fidelity cross-check; the `formulas` backend remains the default.
    """
    soffice = _find_soffice()
    if soffice is None:
        raise RecalcError(
            "LibreOffice (soffice) not found. Install it with: "
            "winget install -e --id TheDocumentFoundation.LibreOffice"
        )
    profile = tempfile.mkdtemp(prefix="emc_lo_profile_")
    outdir = tempfile.mkdtemp(prefix="emc_lo_out_")
    try:
        user_dir = os.path.join(profile, "user")
        os.makedirs(user_dir, exist_ok=True)
        with open(os.path.join(user_dir, "registrymodifications.xcu"), "w", encoding="utf-8") as handle:
            handle.write(_RECALC_XCU)
        profile_url = "file:///" + profile.replace("\\", "/")
        cmd = [
            soffice, f"-env:UserInstallation={profile_url}",
            "--headless", "--norestore", "--nolockcheck",
            "--convert-to", "xlsx:Calc MS Excel 2007 XML",
            "--outdir", outdir, in_path,
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        produced = glob.glob(os.path.join(outdir, "*.xlsx"))
        if not produced:
            detail = (proc.stderr or proc.stdout or "").strip()[:300]
            raise RecalcError(
                f"LibreOffice convert produced no file (exit {proc.returncode}): {detail}"
            )
        if os.path.exists(out_path):
            os.remove(out_path)
        shutil.move(produced[0], out_path)
        return out_path
    except subprocess.TimeoutExpired as exc:
        raise RecalcError("LibreOffice recalc timed out") from exc
    finally:
        shutil.rmtree(profile, ignore_errors=True)
        shutil.rmtree(outdir, ignore_errors=True)


BACKENDS = {"formulas": _formulas_backend, "libreoffice": _libreoffice_backend}


def recalc(in_path: str, *, backend: str = "formulas", out_path: str | None = None) -> str:
    """Write a recalculated copy of `in_path` and return its path. Never mutates the input."""
    if backend not in BACKENDS:
        raise RecalcError(f"unknown backend {backend!r}; available: {sorted(BACKENDS)}")
    if out_path is None:
        fd, out_path = tempfile.mkstemp(prefix="emc_recalc_", suffix=".xlsx")
        os.close(fd)
    return BACKENDS[backend](in_path, out_path)


def recalc_workbook(in_path: str, *, backend: str = "formulas"):
    """Return (workbook, out_path) for the recalculated model, loaded data_only."""
    out_path = recalc(in_path, backend=backend)
    return openpyxl.load_workbook(out_path, data_only=True), out_path
