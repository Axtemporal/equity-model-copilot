"""Session state: round-trip of cursor / chat / working values."""
from engine.session import SessionState


def test_session_roundtrip(tmp_path):
    path = str(tmp_path / "session.yaml")
    state = SessionState(path=path)
    state.current_index = 3
    state.add_message("Brent average", "user", "2029 para 70")
    state.add_message("Brent average", "claude", "Atualizei: 2029 = 70")
    state.set_working("Brent average", {"2029": 70})
    state.save()

    reloaded = SessionState.load(path)
    assert reloaded.current_index == 3
    assert reloaded.get_working("Brent average") == {"2029": 70}
    chat = reloaded.get_chat("Brent average")
    assert len(chat) == 2
    assert chat[0]["text"] == "2029 para 70"


def test_load_missing_returns_fresh(tmp_path):
    state = SessionState.load(str(tmp_path / "nope.yaml"))
    assert state.current_index == 0
    assert state.chats == {}
    assert state.working == {}
