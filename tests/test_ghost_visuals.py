import time
import pytest
from src.backend.ghost_ai import GhostManager, GhostState, GhostIdentity



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
        assert state == 'flee'

    # Ghosts should be edible during power pellet
    for ghost in gm.ghosts.values():
        assert ghost.is_edible()


def test_power_pellet_deactivation_and_revert_state():
    gm = GhostManager()
    gm.activate_power_pellet()
    gm.deactivate_power_pellet()
    gm.update()
    states = gm.get_all_states()
    # After deactivation and update, ghosts revert to original behaviour
    assert states['Blinky'] == 'chase'
    assert states['Pinky'] == 'ambush'
    assert states['Inky'] == 'patrol'
    assert states['Clyde'] == 'random'


def test_edible_timeout():
    gm = GhostManager()
    gm.activate_power_pellet()
    # Simulate time passing by adjusting the power_pellet_end_time
    gm.power_pellet_end_time = time.time() - 1
    gm.update()
    states = gm.get_all_states()
    # Ghosts should revert to original behaviour after edible time
    assert states['Blinky'] == 'chase'
    assert states['Pinky'] == 'ambush'
    assert states['Inky'] == 'patrol'
    assert states['Clyde'] == 'random'

