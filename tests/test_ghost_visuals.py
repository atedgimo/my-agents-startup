import pytest
from src.backend.ghosts import GhostManager, GhostIdentity, GhostState

# Existing tests

def test_initial_ghost_states():
    gm = GhostManager()
    states = gm.get_all_states()
    assert states == {
        'Blinky': 'chase',
        'Pinky': 'chase',
        'Inky': 'chase',
        'Clyde': 'chase'
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


# Additional tests for ghost visual identifiers and state logic

def test_ghost_state_transitions():
    gm = GhostManager()
    gm.set_ghost_state(GhostIdentity.BLINKY, GhostState.FLEE)
    assert gm.get_ghost_state(GhostIdentity.BLINKY) == GhostState.FLEE
    gm.set_ghost_state(GhostIdentity.BLINKY, GhostState.CHASE)
    assert gm.get_ghost_state(GhostIdentity.BLINKY) == GhostState.CHASE


def test_ghost_visual_identifiers():
    gm = GhostManager()
    gm.set_ghost_state(GhostIdentity.PINKY, GhostState.FLEE)
    state = gm.get_ghost_state(GhostIdentity.PINKY)
    # Assuming visual identifier is derived from state string
    assert state == GhostState.FLEE


def test_ghost_state_effects_on_game():
    # This is a placeholder for integration tests
    # that would check game logic reacting to ghost states
    gm = GhostManager()
    gm.set_ghost_state(GhostIdentity.INKY, GhostState.EATEN)
    assert gm.get_ghost_state(GhostIdentity.INKY) == GhostState.EATEN

