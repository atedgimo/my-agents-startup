import pytest
from src.backend.ghost_ai import GhostManager, GhostState, GhostIdentity


def test_ghost_initial_states():
    gm = GhostManager()
    states = gm.get_all_states()
    assert states[GhostIdentity.BLINKY] == GhostState.CHASE
    assert states[GhostIdentity.PINKY] == GhostState.AMBUSH
    assert states[GhostIdentity.INKY] == GhostState.PATROL
    assert states[GhostIdentity.CLYDE] == GhostState.RANDOM


def test_activate_power_pellet_sets_flee_state():
    gm = GhostManager()
    gm.activate_power_pellet()
    states = gm.get_all_states()
    for state in states.values():
        assert state == GhostState.FLEE


def test_deactivate_power_pellet_reverts_states():
    gm = GhostManager()
    gm.activate_power_pellet()
    gm.deactivate_power_pellet()
    gm.update()  # Should revert states after power pellet expires
    states = gm.get_all_states()
    assert states[GhostIdentity.BLINKY] == GhostState.CHASE
    assert states[GhostIdentity.PINKY] == GhostState.AMBUSH
    assert states[GhostIdentity.INKY] == GhostState.PATROL
    assert states[GhostIdentity.CLYDE] == GhostState.RANDOM


def test_is_edible_returns_true_during_flee():
    gm = GhostManager()
    gm.activate_power_pellet()
    assert gm.is_edible(GhostIdentity.BLINKY)
    assert gm.is_edible(GhostIdentity.PINKY)


def test_is_edible_returns_false_when_not_flee():
    gm = GhostManager()
    assert not gm.is_edible(GhostIdentity.BLINKY)


@pytest.mark.parametrize("state", [GhostState.CHASE, GhostState.AMBUSH, GhostState.PATROL, GhostState.RANDOM])
def test_drawGhost_colors_for_states(monkeypatch, state):
    # This test is a placeholder to illustrate testing drawGhost logic
    # Actual rendering tests require a canvas context mock or browser environment
    from src.game import drawGhost
    # We test that drawGhost does not throw errors for different states
    try:
        drawGhost(None, 0, 0, state.name, GhostIdentity.BLINKY)
    except Exception as e:
        pytest.fail(f"drawGhost raised an exception for state {state}: {e}")
