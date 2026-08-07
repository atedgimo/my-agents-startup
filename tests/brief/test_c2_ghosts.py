"""C2 — four ghosts with distinct behaviours.

The brief asks for Blinky-style variety, not four copies of one chase loop.
Probed at the API: the backend must expose ghost state for four ghosts whose
declared behaviours are not all identical."""
from fastapi.testclient import TestClient

from src.backend.main import app

client = TestClient(app)


def test_four_ghosts_exist_with_distinct_behaviours():
    r = client.get("/ghost-states")
    assert r.status_code == 200, f"/ghost-states answered {r.status_code}"
    data = r.json()
    ghosts = data if isinstance(data, list) else data.get("ghosts", [])
    assert len(ghosts) >= 4, f"the brief asks for 4 ghosts; the API reports {len(ghosts)}"
    behaviours = {str(g.get("behavior") or g.get("behaviour") or g.get("mode") or
                      g.get("ai") or g.get("personality") or "") for g in ghosts}
    behaviours.discard("")
    assert len(behaviours) >= 2, (
        "four ghosts but no behavioural variety — the API reports no distinct "
        f"behaviour/mode/personality fields (saw: {behaviours or 'nothing'})")
