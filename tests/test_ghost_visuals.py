import pytest
from src.backend.ghost_visuals import GhostManager, GhostState


class GhostIdentity:
    BLINKY = 'Blinky'
    PINKY = 'Pinky'
    INKY = 'Inky'
    CLYDE = 'Clyde'


def test_initial_ghost_states():
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
    gm.set_ghost_state(GhostIdentity.BLINKY, GhostState.FLEE)
    assert gm.get_ghost_state(GhostIdentity.BLINKY) == GhostState.FLEE
    states = gm.get_all_states()
    assert states['Blinky'] == 'flee'

    gm.set_ghost_state(GhostIdentity.CLYDE, GhostState.EATEN)
    assert gm.get_ghost_state(GhostIdentity.CLYDE) == GhostState.EATEN
    states = gm.get_all_states()
    assert states['Clyde'] == 'eaten'


@pytest.mark.parametrize("identity,state", [
    (GhostIdentity.PINKY, GhostState.PATROL),
    (GhostIdentity.INKY, GhostState.AMBUSH),
])
def test_parametrized_states(identity, state):
    gm = GhostManager()
    gm.set_ghost_state(identity, state)
    assert gm.get_ghost_state(identity) == state


def test_power_pellet_activation_and_edible_state():
    gm = GhostManager()
    gm.activate_power_pellet()
    states = gm.get_all_states()
    for state in states.values():
        assert state == GhostState.FLEE

    # Ghosts should be edible during power pellet
    for ghost in gm.ghosts.values():
        assert ghost.is_edible()


def test_power_pellet_deactivation_and_revert_state():
    gm = GhostManager()
    gm.activate_power_pellet()
    import time
    time.sleep(0.1)  # short wait to simulate time passing
    gm.deactivate_power_pellet()
    gm.update()
    states = gm.get_all_states()
    # After deactivation and update, ghosts revert to original behaviour
    assert states['Blinky'] == GhostState.CHASE
    assert states['Pinky'] == GhostState.AMBUSH
    assert states['Inky'] == GhostState.PATROL
    assert states['Clyde'] == GhostState.RANDOM


def test_edible_timeout():
    gm = GhostManager()
    gm.activate_power_pellet()
    import time
    # Wait for edible time to expire
    time.sleep(10.1)
    gm.update()
    states = gm.get_all_states()
    # Ghosts should revert to original behaviour after edible time
    assert states['Blinky'] == GhostState.CHASE
    assert states['Pinky'] == GhostState.AMBUSH
    assert states['Inky'] == GhostState.PATROL
    assert states['Clyde'] == GhostState.RANDOM
