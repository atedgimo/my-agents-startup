import pytest
from fastapi.testclient import TestClient
from src.backend.api import app

client = TestClient(app)

def test_get_visual_feedback_initial():
    response = client.get("/game/visual-feedback")
    assert response.status_code == 200
    data = response.json()
    assert data["pellet_consumed"] is False
    assert data["ghost_state"] == "normal"
    assert data["power_pellet_active"] is False

def test_consume_pellet_and_feedback():
    response = client.post("/game/consume-pellet")
    assert response.status_code == 200
    response = client.get("/game/visual-feedback")
    data = response.json()
    assert data["pellet_consumed"] is True

def test_set_ghost_state():
    for state in ["normal", "frightened", "eaten"]:
        response = client.post(f"/game/set-ghost-state/{state}")
        assert response.status_code == 200
        response = client.get("/game/visual-feedback")
        data = response.json()
        assert data["ghost_state"] == state

    response = client.post("/game/set-ghost-state/invalid")
    assert response.status_code == 400

def test_activate_power_pellet():
    response = client.post("/game/activate-power-pellet")
    assert response.status_code == 200
    response = client.get("/game/visual-feedback")
    data = response.json()
    assert data["power_pellet_active"] is True

def test_reset_visual_states():
    response = client.post("/game/reset-visual-states")
    assert response.status_code == 200
    response = client.get("/game/visual-feedback")
    data = response.json()
    assert data["pellet_consumed"] is False
    assert data["ghost_state"] == "normal"
    assert data["power_pellet_active"] is False
