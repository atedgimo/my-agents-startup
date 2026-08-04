import pytest
import time
from src.backend.ghost_visuals import GhostManager, GhostState

def test_initial_states():
    gm = GhostManager()
    states = gm.get_all_states()
    assert states == {
        'Blinky': 'chase',
        'Pinky': 'ambush',
        'Inky': 'patrol',
        'Clyde': 'random'
    }

def test_set_and_get_ghost_state():
    gm = GhostManager()
    gm.set_ghost_state('Blinky', GhostState.FLEE)
    assert gm.get_ghost_state('Blinky') == GhostState.FLEE
    states = gm.get_all_states()
    assert states['Blinky'] == 'flee'

    gm.set_ghost_state('Clyde', GhostState.EATEN)
    assert gm.get_ghost_state('Clyde') == GhostState.EATEN
    states = gm.get_all_states()
    assert states['Clyde'] == 'eaten'

@pytest.mark.parametrize("name,state", [
    ('Pinky', GhostState.PATROL),
    ('Inky', GhostState.AMBUSH),
])
def test_parametrized_states(name, state):
    gm = GhostManager()
    gm.set_ghost_state(name, state)
    assert gm.get_ghost_state(name) == state


def test_power_pellet_activation():
    gm = GhostManager()
    gm.activate_power_pellet()
    ghosts = gm.get_ghosts()
    for ghost in ghosts:
        assert ghost.state == GhostState.FLEE
        assert ghost.is_edible()

def test_power_pellet_deactivation_and_edible_timeout(monkeypatch):
    gm = GhostManager()
    gm.activate_power_pellet()
    gm.deactivate_power_pellet()
    ghosts = gm.get_ghosts()
    # After deactivation, ghosts should be EDIBLE
    for ghost in ghosts:
        assert ghost.state == GhostState.EDIBLE
        assert ghost.is_edible()

    # Fast forward time beyond edible_timer
    future_time = time.time() + 11
    monkeypatch.setattr("time.time", lambda: future_time)
    gm.update()
    # After edible timer expires, ghosts revert to original behaviour
    for ghost in ghosts:
        assert ghost.state == ghost.behaviour
        assert not ghost.is_edible()

