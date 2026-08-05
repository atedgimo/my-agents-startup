import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/backend')))

from ghost_ai import GhostVisual, GhostManager, GhostState


def test_ghost_visual_identifiers():
    expected_members = [
        'BLINKY', 'PINKY', 'INKY', 'CLYDE',
        'FRIGHTENED', 'EYES_UP', 'EYES_DOWN', 'EYES_LEFT', 'EYES_RIGHT'
    ]
    for member in expected_members:
        assert hasattr(GhostVisual, member), f"GhostVisual missing member {member}"


def test_ghost_visual_state_logic():
    assert GhostVisual.FRIGHTENED.name == 'FRIGHTENED'
    assert GhostVisual.FRIGHTENED.value is not None

    assert GhostVisual.EYES_UP.name == 'EYES_UP'
    assert GhostVisual.EYES_DOWN.name == 'EYES_DOWN'
    assert GhostVisual.EYES_LEFT.name == 'EYES_LEFT'
    assert GhostVisual.EYES_RIGHT.name == 'EYES_RIGHT'

    normal_ghosts = {GhostVisual.BLINKY, GhostVisual.PINKY, GhostVisual.INKY, GhostVisual.CLYDE}
    special_states = {GhostVisual.FRIGHTENED, GhostVisual.EYES_UP, GhostVisual.EYES_DOWN, GhostVisual.EYES_LEFT, GhostVisual.EYES_RIGHT}
    assert normal_ghosts.isdisjoint(special_states)


def test_initial_ghost_states():
    gm = GhostManager()
    states = gm.get_all_states()
    assert states == {
        'Blinky': GhostState.CHASE,
        'Pinky': GhostState.AMBUSH,
        'Inky': GhostState.PATROL,
        'Clyde': GhostState.RANDOM
    }


def test_set_and_get_ghost_state():
    gm = GhostManager()
    gm.set_ghost_state('Blinky', GhostState.FLEE)
    assert gm.get_ghost_state('Blinky') == GhostState.FLEE
    states = gm.get_all_states()
    assert states['Blinky'] == GhostState.FLEE

    gm.set_ghost_state('Clyde', GhostState.EATEN)
    assert gm.get_ghost_state('Clyde') == GhostState.EATEN
    states = gm.get_all_states()
    assert states['Clyde'] == GhostState.EATEN


@pytest.mark.parametrize("identity,state", [
    ('Pinky', GhostState.PATROL),
    ('Inky', GhostState.AMBUSH),
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

    for ghost_name in gm.ghosts.keys():
        assert gm.is_edible(ghost_name)


def test_power_pellet_deactivation_and_revert_state():
    gm = GhostManager()
    gm.activate_power_pellet()
    import time
    time.sleep(0.1)  # short wait to simulate time passing
    gm.deactivate_power_pellet()
    gm.update()
    states = gm.get_all_states()
    assert states['Blinky'] == GhostState.CHASE
    assert states['Pinky'] == GhostState.AMBUSH
    assert states['Inky'] == GhostState.PATROL
    assert states['Clyde'] == GhostState.RANDOM


def test_edible_timeout():
    gm = GhostManager()
    gm.activate_power_pellet()
    import time
    time.sleep(10.1)
    gm.update()
    states = gm.get_all_states()
    assert states['Blinky'] == GhostState.CHASE
    assert states['Pinky'] == GhostState.AMBUSH
    assert states['Inky'] == GhostState.PATROL
    assert states['Clyde'] == GhostState.RANDOM

    gm = GhostManager()
    gm.activate_power_pellet()
