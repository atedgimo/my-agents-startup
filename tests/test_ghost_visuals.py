import pytest
from src.backend.ghost_visuals import GhostVisualIdentifier, GhostState


def test_initial_state():
    ghost = GhostVisualIdentifier(1)
    assert ghost.state == GhostState.NORMAL
    assert ghost.get_visual_identifier() == "ghost_1_normal"


def test_set_state_valid():
    ghost = GhostVisualIdentifier(2)
    ghost.set_state(GhostState.FRIGHTENED)
    assert ghost.state == GhostState.FRIGHTENED
    assert ghost.get_visual_identifier() == "ghost_2_frightened"

    ghost.set_state(GhostState.EATEN)
    assert ghost.state == GhostState.EATEN
    assert ghost.get_visual_identifier() == "ghost_2_eaten"


def test_set_state_invalid():
    ghost = GhostVisualIdentifier(3)
    with pytest.raises(ValueError):
        ghost.set_state("invalid_state")


def test_get_visual_identifier_unknown_state(monkeypatch):
    ghost = GhostVisualIdentifier(4)
    # Force an invalid state to test fallback
    ghost.state = "invalid"
    assert ghost.get_visual_identifier() == "ghost_4_unknown"
