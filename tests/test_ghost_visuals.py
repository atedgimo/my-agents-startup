import pytest
import sys
import os

# Adjust the path to import src.backend
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/backend')))

# Try to import from ghosts.py for this test suite
try:
    from ghosts import GhostManager, GhostState
    GHOSTS_IMPORTED = True
except ImportError:
    from ghost_ai import GhostManager, GhostState
    GHOSTS_IMPORTED = False

from ghost_ai import GhostVisual


def test_ghost_visual_identifiers():
    # Test that the GhostVisual enum has the expected members
    expected_members = [
        'BLINKY', 'PINKY', 'INKY', 'CLYDE',
        'FRIGHTENED', 'EYES_UP', 'EYES_DOWN', 'EYES_LEFT', 'EYES_RIGHT'
    ]
    for member in expected_members:
        assert hasattr(GhostVisual, member), f"GhostVisual missing member {member}"

def test_ghost_visual_identifier_method():
    gm = GhostManager()
    for ghost_name in gm.ghosts:
        ghost = gm.ghosts[ghost_name]
        visual = ghost.visual_identifier()
        assert visual in GhostVisual, f"Visual {visual} for ghost {ghost_name} not in GhostVisual enum"
        # Check that visual matches expected mapping
        expected_visual = getattr(GhostVisual, ghost_name.upper())
        assert visual == expected_visual, f"Ghost {ghost_name} visual {visual} does not match expected {expected_visual}"


def test_ghost_visual_state_logic():
    # Test the state logic of GhostVisual
    # For example, check if FRIGHTENED is a special state
    assert GhostVisual.FRIGHTENED.name == 'FRIGHTENED'
    assert GhostVisual.FRIGHTENED.value is not None

    # Check that eyes directions are correctly named
    assert GhostVisual.EYES_UP.name == 'EYES_UP'
    assert GhostVisual.EYES_DOWN.name == 'EYES_DOWN'
    assert GhostVisual.EYES_LEFT.name == 'EYES_LEFT'
    assert GhostVisual.EYES_RIGHT.name == 'EYES_RIGHT'

    # Check that the normal ghost visuals are distinct from special states
    normal_ghosts = {GhostVisual.BLINKY, GhostVisual.PINKY, GhostVisual.INKY, GhostVisual.CLYDE}
    special_states = {GhostVisual.FRIGHTENED, GhostVisual.EYES_UP, GhostVisual.EYES_DOWN, GhostVisual.EYES_LEFT, GhostVisual.EYES_RIGHT}
    assert normal_ghosts.isdisjoint(special_states)


# Retain existing tests below
from ghost_ai import GhostManager, GhostState

class GhostIdentity:
    BLINKY = 'Blinky'
    PINKY = 'Pinky'
    INKY = 'Inky'
    CLYDE = 'Clyde'


def test_initial_ghost_states():
    gm = GhostManager()
    states = gm.get_all_states()
    print("[DEBUG] test_initial_ghost_states: Actual states returned:")
    for ghost in ['Blinky', 'Pinky', 'Inky', 'Clyde']:
        state = states[ghost]
        print(f"  [DEBUG] {ghost}: {state} (type: {type(state)})")
        # Debug: print expected vs actual
        print(f"  [DEBUG] Expected: IDLE, Actual: {state}")
        assert state == "IDLE"


def test_set_and_get_ghost_state():
    gm = GhostManager()
    gm.set_ghost_state(GhostIdentity.BLINKY, GhostState.FLEE)
    state = gm.get_ghost_state(GhostIdentity.BLINKY)
    if hasattr(state, 'name'):
        assert state.name == 'FLEE'
    else:
        assert state == 'FLEE'
    states = gm.get_all_states()
    state = states['Blinky']
    if hasattr(state, 'name'):
        assert state.name == 'FLEE'
    else:
        assert state == 'FLEE'

    # The new GhostState does have EATEN, so test it
    if hasattr(GhostState, 'EATEN'):
        gm.set_ghost_state(GhostIdentity.CLYDE, GhostState.EATEN)
        state = gm.get_ghost_state(GhostIdentity.CLYDE)
        if hasattr(state, 'name'):
            assert state.name == 'EATEN'
        else:
            assert state == 'EATEN'
        states = gm.get_all_states()
        state = states['Clyde']
        if hasattr(state, 'name'):
            assert state.name == 'EATEN'
        else:
            assert state == 'EATEN'


@pytest.mark.parametrize("identity,state", [
    (GhostIdentity.PINKY, GhostState.PATROL),
    (GhostIdentity.INKY, GhostState.AMBUSH),
])
def test_parametrized_states(identity, state):
    gm = GhostManager()
    gm.set_ghost_state(identity, state)
    ghost_state = gm.get_ghost_state(identity)
    if hasattr(ghost_state, 'name'):
        assert ghost_state.name == state.name
    else:
        assert ghost_state == state.name or ghost_state == state


def test_power_pellet_activation_and_edible_state():
    gm = GhostManager()
    gm.activate_power_pellet()
    states = gm.get_all_states()
    for state in states.values():
        if hasattr(state, 'name'):
            assert state.name == 'FLEE'
        else:
            assert state == 'FLEE'
    # Ghosts should be edible during power pellet
    # Only run if is_edible exists
    if hasattr(gm, 'is_edible'):
        for ghost_name in getattr(gm, 'ghosts', []):
            assert gm.is_edible(ghost_name)


def test_power_pellet_deactivation_and_revert_state():
    gm = GhostManager()
    gm.activate_power_pellet()
    import time
    time.sleep(10.1)  # Wait for edible timer to expire
    gm.update()
    states = gm.get_all_states()
    # After deactivation and update, ghosts revert to original behaviour
    expected = {
        'Blinky': 'CHASE',
        'Pinky': 'AMBUSH',
        'Inky': 'PATROL',
        'Clyde': 'RANDOM'
    }
    for ghost, state in states.items():
        if hasattr(state, 'name'):
            assert state.name == expected[ghost]
        else:
            assert state == expected[ghost]


def test_edible_timeout():
    gm = GhostManager()
    gm.activate_power_pellet()
    import time
    # Wait for edible time to expire
    time.sleep(10.1)
    gm.update()
    states = gm.get_all_states()
    # Ghosts should revert to original behaviour after edible time
    expected = {
        'Blinky': 'CHASE',
        'Pinky': 'AMBUSH',
        'Inky': 'PATROL',
        'Clyde': 'RANDOM'
    }
    for ghost, state in states.items():
        if hasattr(state, 'name'):
            assert state.name == expected[ghost]
        else:
            assert state == expected[ghost]
