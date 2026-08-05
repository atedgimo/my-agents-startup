import pytest
from fastapi.testclient import TestClient
from src.backend.main import app

client = TestClient(app)

def test_ghosts_endpoint():
    response = client.get("/ghosts")
    assert response.status_code == 200
    data = response.json()
    assert 'Blinky' in data
    assert 'Pinky' in data
    assert 'Inky' in data
    assert 'Clyde' in data
