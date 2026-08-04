import pytest
import time
from src.backend.ghost_visuals import GhostManager, GhostState

# Retain existing tests but adapt to new GhostManager interface

def test_initial_states():
    gm = GhostManager()
    ghosts = gm.get_ghosts()
    assert len(ghosts) == 4
    assert ghosts[0].state == GhostState.CHASE
    assert ghosts[1].state == GhostState.AMBUSH
    assert ghosts[2].state == GhostState.PATROL
    assert ghosts[3].state == GhostState.RANDOM

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

# Preserve original tests for compatibility
from src.backend.ghosts import GhostManager as OldGhostManager, GhostIdentity, GhostState as OldGhostState

def test_initial_ghost_states():
    gm = OldGhostManager()
    states = gm.get_all_states()
    assert states == {
        'Blinky': 'chase',
        'Pinky': 'chase',
        'Inky': 'chase',
        'Clyde': 'chase'
    }

def test_set_and_get_ghost_state():
    gm = OldGhostManager()
    gm.set_ghost_state(GhostIdentity.BLINKY, OldGhostState.FLEE)
    assert gm.get_ghost_state(GhostIdentity.BLINKY) == OldGhostState.FLEE
    states = gm.get_all_states()
    assert states['Blinky'] == 'flee'

    gm.set_ghost_state(GhostIdentity.CLYDE, OldGhostState.EATEN)
    assert gm.get_ghost_state(GhostIdentity.CLYDE) == OldGhostState.EATEN
    states = gm.get_all_states()
    assert states['Clyde'] == 'eaten'

import pytest
@pytest.mark.parametrize("identity,state", [
    (GhostIdentity.PINKY, OldGhostState.PATROL),
    (GhostIdentity.INKY, OldGhostState.AMBUSH),
])
def test_parametrized_states(identity, state):
    gm = OldGhostManager()
    gm.set_ghost_state(identity, state)
    assert gm.get_ghost_state(identity) == state

