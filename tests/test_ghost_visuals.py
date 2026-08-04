import pytest
from src.backend.ghost_visuals import GhostManager, GhostState

def test_ghost_initial_state():
    manager = GhostManager()
    visuals = manager.get_all_ghosts_visuals()
    assert visuals["blinky"] == "blinky_patrol"
    assert visuals["pinky"] == "pinky_patrol"
    assert visuals["inky"] == "inky_patrol"
    assert visuals["clyde"] == "clyde_patrol"

def test_set_ghost_state():
    manager = GhostManager()
    manager.set_ghost_state("blinky", GhostState.CHASE)
    assert manager.get_ghost_visual("blinky") == "blinky_chase"
    manager.set_ghost_state("pinky", GhostState.FLEE)
    assert manager.get_ghost_visual("pinky") == "pinky_flee"
    manager.set_ghost_state("inky", GhostState.EDIBLE)
    assert manager.get_ghost_visual("inky") == "inky_edible"
    manager.set_ghost_state("clyde", GhostState.RANDOM)
    assert manager.get_ghost_visual("clyde") == "clyde_random"

def test_unknown_ghost():
    manager = GhostManager()
    assert manager.get_ghost_visual("unknown_ghost") == "unknown"
