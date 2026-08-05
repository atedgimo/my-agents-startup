import time
import pytest
from src.backend.ghost_ai import Ghost, GhostState


def test_ghost_initial_state():
    ghost = Ghost('Blinky')
    assert ghost.state == GhostState.CHASE


def test_ghost_update_state_powered_up():
    ghost = Ghost('Blinky')
    ghost.update_state(player_powered_up=True)
    assert ghost.state == GhostState.FLEE
    assert ghost.is_edible()


def test_ghost_update_state_edible_timeout():
    ghost = Ghost('Blinky')
    ghost.update_state(player_powered_up=True)
    # Simulate time passing beyond edible duration
    ghost.edible_until = time.time() - 1
    ghost.update_state(player_powered_up=False)
    assert ghost.state == ghost.original_state


def test_visual_identifier():
    ghost = Ghost('Blinky')
    assert ghost.visual_identifier() == ghost.state.value


def test_repr():
    ghost = Ghost('Blinky')
    rep = repr(ghost)
    assert 'Blinky' in rep and ghost.state.value in rep


@pytest.mark.parametrize("state", [
    GhostState.IDLE,
    GhostState.CHASE,
    GhostState.FRIGHTENED,
    GhostState.FLEE,
    GhostState.EATEN,
    GhostState.AMBUSH,
    GhostState.PATROL,
    GhostState.RANDOM
])
def test_set_state(state):
    ghost = Ghost('Blinky')
    ghost.state = state
    assert ghost.state == state
