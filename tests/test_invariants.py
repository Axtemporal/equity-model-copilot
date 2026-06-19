"""Full invariant suite on the recalculated model (requires a recalc backend)."""
import pytest

from engine.harness import verify_model


@pytest.mark.recalc
def test_synth_passes_all_invariants(require_recalc, synth_model):
    report = verify_model(synth_model)
    assert report.ok, report.summary()
    # SYNTH closes by construction: no failures and no warnings expected.
    assert not report.warnings(), [r.message for r in report.warnings()]
