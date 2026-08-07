import time
import pytest
from src.backend.ghost_ai import Ghost, GhostManager, GhostState, GhostIdentity


def test_ghost_initial_state():
    ghost = Ghost(GhostIdentity.BLINKY)
    assert ghost.name == GhostIdentity.BLINKY
    assert ghost.state == GhostState.IDLE


def test_ghost_activate_and_sleep():
    ghost = Ghost(GhostIdentity.PINKY)
    ghost.activate()
    assert ghost.state == GhostState.CHASE
    ghost.sleep()
    assert ghost.state == GhostState.FRIGHTENED


def test_ghost_is_active():
    ghost = Ghost(GhostIdentity.INKY)
    ghost.activate()
    assert ghost.is_active() is True
    ghost.sleep()
    assert ghost.is_active() is False


def test_ghost_manager_initial_states():
    manager = GhostManager()
    states = manager.get_all_states()
    assert states[GhostIdentity.BLINKY] == GhostState.CHASE
    assert states[GhostIdentity.PINKY] == GhostState.AMBUSH
    assert states[GhostIdentity.INKY] == GhostState.PATROL
    assert states[GhostIdentity.CLYDE] == GhostState.RANDOM


def test_power_pellet_activation_and_deactivation():
    manager = GhostManager()
    manager.activate_power_pellet()
    assert manager.power_pellet_active is True
    for ghost in manager.ghosts.values():
        assert ghost.state == GhostState.FLEE
    # Simulate time passing
    manager.power_pellet_end_time = time.time() - 1
    manager.update()
    assert manager.power_pellet_active is False
    for ghost in manager.ghosts.values():
        assert ghost.state != GhostState.FLEE


def test_is_edible():
    manager = GhostManager()
    manager.activate_power_pellet()
    for ghost_name in manager.ghosts:
        assert manager.is_edible(ghost_name) is True
    manager.deactivate_power_pellet()
    for ghost_name in manager.ghosts:
        assert manager.is_edible(ghost_name) is False


if __name__ == '__main__':
    pytest.main()
