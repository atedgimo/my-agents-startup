import pytest
from src.backend.ghost_visuals import Ghost, GhostState, create_ghosts


def test_ghost_initial_states():
    ghosts = create_ghosts()
    assert ghosts["blinky"].state == GhostState.CHASE
    assert ghosts["pinky"].state == GhostState.AMBUSH
    assert ghosts["inky"].state == GhostState.PATROL
    assert ghosts["clyde"].state == GhostState.RANDOM


def test_ghost_state_transitions():
    ghost = Ghost("blinky", GhostState.CHASE)
    ghost.set_state(GhostState.FLEE)
    assert ghost.state == GhostState.FLEE
    ghost.set_state(GhostState.EDIBLE)
    assert ghost.state == GhostState.EDIBLE


def test_ghost_visual_identifiers():
    ghost = Ghost("pinky", GhostState.AMBUSH)
    assert ghost.get_visual_identifier() == "pinky_ambush"
    ghost.set_state(GhostState.FLEE)
    assert ghost.get_visual_identifier() == "pinky_flee"
    ghost.set_state(GhostState.EDIBLE)
    assert ghost.get_visual_identifier() == "pinky_edible"

    ghost.set_state(GhostState.RANDOM)
    assert ghost.get_visual_identifier() == "pinky_random"

    ghost.set_state(GhostState.PATROL)
    assert ghost.get_visual_identifier() == "pinky_patrol"

    ghost.set_state(GhostState.CHASE)
    assert ghost.get_visual_identifier() == "pinky_chase"


def test_create_ghosts_factory():
    ghosts = create_ghosts()
    assert set(ghosts.keys()) == {"blinky", "pinky", "inky", "clyde"}
    for name, ghost in ghosts.items():
        assert ghost.name == name
        assert isinstance(ghost.state, GhostState)
