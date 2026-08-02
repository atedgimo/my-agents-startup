import pytest
from fastapi.testclient import TestClient
from src.backend.main import app

client = TestClient(app)

def test_get_scores_initial():
    response = client.get("/scores")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_submit_score_and_get_scores():
    # Submit a new score
    response = client.post("/submit-score", json={"name": "Tester", "score": 123})
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Score submitted successfully"
    assert "scores" in data
    assert any(score["name"] == "Tester" and score["score"] == 123 for score in data["scores"])

    # Check scores endpoint returns the new score
    response = client.get("/scores")
    assert response.status_code == 200
    scores = response.json()
    assert any(score["name"] == "Tester" and score["score"] == 123 for score in scores)


def test_submit_score_invalid():
    response = client.post("/submit-score", json={"name": "Tester", "score": "not-an-int"})
    assert response.status_code == 400
    data = response.json()
    assert "error" in data

    response = client.post("/submit-score", json={"name": "Tester"})
    assert response.status_code == 400
    data = response.json()
    assert "error" in data


def test_receive_input_and_move():
    # Send input direction
    response = client.post("/input", json={"direction": "UP"})
    assert response.status_code == 200
    data = response.json()
    assert "Direction UP queued" in data["message"]

    # Move should update position
    response = client.get("/move")
    assert response.status_code == 200
    data = response.json()
    assert data["direction"] == "UP"
    assert "position" in data


def test_clear_input_buffer():
    response = client.post("/clear_input")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Input buffer cleared"


if __name__ == "__main__":
    import pytest
    pytest.main()
