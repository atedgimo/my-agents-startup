import pytest
from fastapi.testclient import TestClient
from src.backend.main import app, ghost_manager, GhostState

client = TestClient(app)


def test_ghost_states_endpoint():
    # Initially, all ghosts should be in the default state
    response = client.get("/ghost-states")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert all(state == "normal" for state in data.values())


def test_power_pellet_activation_and_ghost_state_change():
    # Activate power pellet
    response = client.post("/activate-power-pellet")
    assert response.status_code == 200
    data = response.json()
    assert data.get("success") is True

    # Check ghost states after activation
    response = client.get("/ghost-states")
    assert response.status_code == 200
    data = response.json()
    assert all(state == "frightened" for state in data.values())

    # Deactivate power pellet
    response = client.post("/deactivate-power-pellet")
    assert response.status_code == 200
    data = response.json()
    assert data.get("success") is True

    # Check ghost states after deactivation
    response = client.get("/ghost-states")
    assert response.status_code == 200
    data = response.json()
    assert all(state == "normal" for state in data.values())


# Additional tests for visual feedback triggers can be added here

