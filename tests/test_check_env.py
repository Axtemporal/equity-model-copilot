"""Environment preflight (`engine.check_env`).

The recalc smoke genuinely runs the 'formulas' backend, so the tests that exercise the
full check are marked `recalc` and skip gracefully when no backend is installed — same
convention as the rest of the suite.
"""
import pytest

from engine.check_env import (
    _ASCII_MAP,
    Check,
    _check_libreoffice,
    _supports_glyphs,
    main,
    run_checks,
)


def test_check_namedtuple_defaults():
    """Pure structural check — no env dependency."""
    c = Check("x", True, False, "detail")
    assert c.ok and not c.optional and c.hint == ""


def test_ascii_fallback_covers_every_report_glyph():
    """A non-UTF console (Windows cp1252) must not crash the diagnostic.

    `main` falls back to ASCII when stdout can't encode the glyphs; guard that the
    detector spots a cp1252 stream and that every glyph the report emits has a mapping.
    """
    class _Cp1252:
        encoding = "cp1252"

    class _Utf8:
        encoding = "utf-8"

    assert _supports_glyphs(_Cp1252()) is False
    assert _supports_glyphs(_Utf8()) is True
    assert set("✓○✗≥→—") <= set(_ASCII_MAP)


@pytest.mark.recalc
def test_all_critical_checks_pass_in_dev_env(require_recalc):
    failing = [c.label for c in run_checks() if not c.ok and not c.optional]
    assert not failing, f"critical env checks failed: {failing}"


@pytest.mark.recalc
def test_recalc_smoke_actually_computes(require_recalc):
    recalc_check = next(c for c in run_checks() if c.label.startswith("recálculo"))
    assert recalc_check.ok, recalc_check.detail
    assert "42" in recalc_check.detail


@pytest.mark.recalc
def test_main_returns_zero_and_prints_report(require_recalc, capsys):
    rc = main()
    out = capsys.readouterr().out
    assert rc == 0
    assert "verificação de ambiente" in out
    assert "Ambiente pronto para build" in out


def test_libreoffice_is_optional_never_critical():
    """LibreOffice absence must never fail the env (it is a cross-check).

    Calls _check_libreoffice() directly rather than run_checks(), so it asserts the
    optional flag without paying for the recalc smoke or needing a backend.
    """
    lo = _check_libreoffice()
    assert lo.label.startswith("LibreOffice")
    assert lo.optional is True
