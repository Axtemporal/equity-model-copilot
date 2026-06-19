"""Golden regression on the synthetic model (requires a recalc backend)."""
import pytest

from engine.harness.golden import check_golden


@pytest.mark.recalc
def test_golden_snapshot_matches(require_recalc, synth_inputs, synth_golden):
    report = check_golden(synth_inputs, synth_golden)
    assert report.ok, [str(c) for c in report.results[0].failing_cells]
