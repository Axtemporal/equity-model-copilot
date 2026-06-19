"""Shared pytest fixtures.

The synthetic (non-proprietary) input is committed under tests/fixtures/. The model is built
fresh from it into a temp dir, so the tests exercise the engine end-to-end. Recalc-dependent
tests skip gracefully when no recalc backend is installed.
"""
import importlib.util
import os

import pytest

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures")


def _has_formulas() -> bool:
    return importlib.util.find_spec("formulas") is not None


@pytest.fixture(scope="session")
def synth_inputs() -> str:
    return os.path.join(FIXTURES, "SYNTH_inputs.xlsx")


@pytest.fixture(scope="session")
def synth_golden() -> str:
    return os.path.join(FIXTURES, "SYNTH_golden.json")


@pytest.fixture(scope="session")
def synth_model(synth_inputs, tmp_path_factory) -> str:
    out = str(tmp_path_factory.mktemp("models") / "SYNTH_model.xlsx")
    from engine import build_model

    build_model.main(synth_inputs, out)
    return out


@pytest.fixture
def require_recalc():
    if not _has_formulas():
        pytest.skip("no recalc backend (formulas) installed")
