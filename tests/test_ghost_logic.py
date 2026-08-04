import pytest
import time
import src.game as game


def test_initial_ghost_state():
    game.resetGame()
    for ghost in game.ghosts:
        assert ghost.state == 'normal'


def test_power_up_activates_ghost_frightened_state():
    game.resetGame()
    # Simulate player eating a power pellet
    power_pellet_pos = None
    for p in game.pellets:
        if game.mazeData[p.y][p.x] == 2:
            power_pellet_pos = (p.x, p.y)
            p.active = True
            break
    if power_pellet_pos is None:
        pytest.skip("No power pellet in maze to test")

    game.playerPos = {'x': power_pellet_pos[0], 'y': power_pellet_pos[1]}
    game.update()

    # After update, ghosts should be frightened
    assert all(g.state == 'frightened' for g in game.ghosts)


def test_ghost_eaten_resets_state_and_increases_score():
    game.resetGame()
    # Set ghosts to frightened
    for g in game.ghosts:
        g.state = 'frightened'
        g.pos = {'x': 5, 'y': 5}
    game.playerPos = {'x': 5, 'y': 5}
    initial_score = game.score
    game.update()
    # Ghosts eaten should reset to normal and score increased
    for g in game.ghosts:
        assert g.state == 'normal'
    assert game.score > initial_score


def test_player_loses_life_on_collision_with_normal_ghost():
    game.resetGame()
    for g in game.ghosts:
        g.state = 'normal'
        g.pos = {'x': 5, 'y': 5}
    game.playerPos = {'x': 5, 'y': 5}
    initial_lives = game.lives
    game.update()
    assert game.lives == initial_lives - 1


def test_game_over_on_life_depletion():
    game.resetGame()
    game.lives = 1
    for g in game.ghosts:
        g.state = 'normal'
        g.pos = {'x': 5, 'y': 5}
    game.playerPos = {'x': 5, 'y': 5}
    game.update()
    assert game.gameState == game.STATE.LOST


