"""C4 — high scores persist via the backend API.

The full round trip, on the app itself: submit a score, read it back. A
scoreboard that forgets is a screenshot."""
from fastapi.testclient import TestClient

from src.backend.main import app

client = TestClient(app)


def test_a_submitted_score_can_be_read_back():
    r = client.post("/submit-score", json={"player": "brief-probe", "score": 4321})
    assert r.status_code in (200, 201), f"submit answered {r.status_code}: {r.text[:200]}"
    r = client.get("/scores")
    assert r.status_code == 200, (
        f"/scores answered {r.status_code} — submitted scores cannot be read back")
    body = r.text
    assert "4321" in body or "brief-probe" in body, (
        "the submitted score is not in the scoreboard — persistence is not real")
