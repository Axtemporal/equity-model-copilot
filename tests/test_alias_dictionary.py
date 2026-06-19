"""Alias dictionary: global resolve, governed override write-back, conflict guard."""
import pytest

from engine.alias_dictionary import AliasConflictError, AliasDictionary


def test_global_resolves_bilingual_spellings():
    ad = AliasDictionary.load()
    assert ad.resolve("Receita líquida") == "(=) Net revenue"
    assert ad.resolve("Lucro líquido") == "(=) Net income"
    assert ad.resolve("Imobilizado") == "PP&E"


def test_unknown_raw_resolves_to_none():
    assert AliasDictionary.load().resolve("não existe essa linha") is None


def test_add_writes_to_override_and_resolves(tmp_path):
    override = tmp_path / "override.yaml"
    ad = AliasDictionary(override_path=override)
    ad.add("Receita de serviços", "(=) Net revenue",
           provenance="confirmed in TIM intake", confirmed_by="analyst")
    # resolvable in this instance...
    assert ad.resolve("Receita de serviços") == "(=) Net revenue"
    # ...and persisted for a fresh load of the same override layer
    assert AliasDictionary(override_path=override).resolve("Receita de serviços") == "(=) Net revenue"


def test_add_rejects_conflicting_remap(tmp_path):
    ad = AliasDictionary(override_path=tmp_path / "o.yaml")
    ad.add("Outras receitas", "(=) Net revenue")
    with pytest.raises(AliasConflictError):
        ad.add("Outras receitas", "(=) EBIT")  # already mapped elsewhere


def test_add_requires_override_path():
    with pytest.raises(ValueError):
        AliasDictionary.load().add("x", "(=) Net revenue")  # no override layer to write to
