"""Fase 1 intake orchestrator: flatten + resolve + classify + content-sufficiency end to end."""
from engine import canonical_schema as cs
from engine import fase1_intake as intake
from engine import role_classifier as rc
from engine.fase1_manifest import MAPPED


def test_analyze_synth_detects_sector_and_is_sufficient(synth_inputs):
    m = intake.analyze(synth_inputs)
    assert m.sector == cs.OIL_AND_GAS
    # every required canonical slot is satisfied by a mapped line from the real input
    assert m.content_sufficient, [c.slot for c in m.missing_required]


def test_analyze_maps_core_lines(synth_inputs):
    m = intake.analyze(synth_inputs)
    by_canonical = {line.canonical: line for line in m.lines if line.disposition == MAPPED}
    assert "(=) Net revenue" in by_canonical
    assert by_canonical["(=) Net revenue"].role == rc.STATEMENT
    # an operational driver is tagged operational-raw (deferred to Fase 2/3)
    assert any(line.canonical == "Brent average" and line.role == rc.OPERATIONAL_RAW
               for line in m.lines)


def test_every_line_has_a_terminal_disposition(synth_inputs):
    m = intake.analyze(synth_inputs)
    assert all(line.disposition != "pending" for line in m.lines)
    # unresolved lines are carried as contextual, never dropped silently
    assert all((line.canonical is not None) or (line.raw_label in m.residual) for line in m.lines)


def test_manifest_roundtrips_to_yaml(synth_inputs, tmp_path):
    m = intake.analyze(synth_inputs)
    path = m.save(str(tmp_path / "fase1_manifest.yaml"))
    import yaml
    data = yaml.safe_load(open(path, encoding="utf-8"))
    assert data["sector"] == cs.OIL_AND_GAS
    assert data["content_sufficient"] is True
