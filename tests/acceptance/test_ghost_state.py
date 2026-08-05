import time
import pytest
from src.backend.ghost_ai import Ghost, GhostState


def test_ghost_initial_state():
    ghost = Ghost('Blinky')
    assert ghost.state == GhostState.CHASE


def test_ghost_update_state_player_powered_up():
    ghost = Ghost('Pinky')
    ghost.update_state(player_powered_up=True)
    assert ghost.state == GhostState.FLEE
    assert ghost.is_edible() is True


def test_ghost_update_state_edible_timeout():
    ghost = Ghost('Inky')
    ghost.update_state(player_powered_up=True)
    assert ghost.state == GhostState.FLEE
    # Fast-forward time by manipulating edible_until
    ghost.edible_until = time.time() - 1
    ghost.update_state(player_powered_up=False)
    assert ghost.state == ghost.original_state


def test_ghost_visual_identifier():
    ghost = Ghost('Clyde')
    assert ghost.visual_identifier() == 'Clyde is chase'
    ghost.update_state(player_powered_up=True)
    assert ghost.visual_identifier() == 'Clyde is flee'
