import pytest
from src.backend.game_logic import Ghost, GhostState

def test_ghost_visual_identifier_normal():
    ghost = Ghost("Blinky")
    assert ghost.visual_identifier() == "Blinky"

def test_ghost_visual_identifier_frightened():
    ghost = Ghost("Pinky")
    ghost.state = GhostState.FRIGHTENED
    assert ghost.visual_identifier() == "Pinky_frightened"

def test_ghost_visual_identifier_eaten():
    ghost = Ghost("Inky")
    ghost.state = GhostState.EATEN
    assert ghost.visual_identifier() == "Inky_eaten"

def test_ghost_state_update_with_powerup():
    ghost = Ghost("Clyde")
    ghost.state = GhostState.NORMAL
    ghost.update_state(player_powered_up=True)
    assert ghost.state == GhostState.FRIGHTENED

def test_ghost_state_update_without_powerup():
    ghost = Ghost("Clyde")
    ghost.state = GhostState.FRIGHTENED
    ghost.update_state(player_powered_up=False)
    assert ghost.state == GhostState.NORMAL

def test_ghost_eaten_state():
    ghost = Ghost("Blinky")
    ghost.eaten()
    assert ghost.state == GhostState.EATEN

def test_ghost_reset():
    ghost = Ghost("Blinky")
    ghost.state = GhostState.EATEN
    ghost.reset()
    assert ghost.state == GhostState.NORMAL
