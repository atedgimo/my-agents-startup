import pytest
from src.backend.ghost_visuals import GhostManager, GhostIdentity, GhostState


from src.backend.ghosts import GhostManager, GhostIdentity, GhostState

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
