import pytest
from src.backend.ghost_visuals import GhostVisual

def test_ghost_visual_initial_state():
    ghost = GhostVisual('ghost1')
    assert ghost.get_state() == 'inactive'

def test_ghost_visual_valid_state_changes():
    ghost = GhostVisual('ghost1')
    ghost.set_state('active')
    assert ghost.get_state() == 'active'
    ghost.set_state('fading')
    assert ghost.get_state() == 'fading'
    ghost.set_state('inactive')
    assert ghost.get_state() == 'inactive'

def test_ghost_visual_invalid_state_change():
    ghost = GhostVisual('ghost1')
    with pytest.raises(ValueError):
        ghost.set_state('invalid')
