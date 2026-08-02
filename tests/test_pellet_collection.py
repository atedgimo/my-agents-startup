import pytest
from fastapi.testclient import TestClient
from src.backend.main import app

client = TestClient(app)

def test_get_pellets():
    response = client.get("/pellets")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_collect_pellet():
    # Setup: add a pellet directly to the backend pellets set
    from src.backend.pellet_collection import pellets, pellets_lock
    pos = (5, 5)
    with pellets_lock:
        pellets.add(pos)

    # Collect the pellet
    response = client.post("/collect_pellet", json={"x": 5, "y": 5})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Pellet collected"
    assert data["position"] == {"x": 5, "y": 5}

    # Try to collect again, should 404
    response = client.post("/collect_pellet", json={"x": 5, "y": 5})
    assert response.status_code == 404


def test_collect_pellet_invalid_request():
    response = client.post("/collect_pellet", json={})
    assert response.status_code == 400

    response = client.post("/collect_pellet", data="not-json")
    assert response.status_code == 400


if __name__ == "__main__":
    import pytest
    pytest.main()
