import pytest
import pytest_asyncio
from httpx import AsyncClient
from src.backend.main import app
from src.backend.ghost_ai import GhostIdentity, GhostState

@pytest.mark.asyncio
async def test_get_ghosts_initial_state():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/ghosts")
    assert response.status_code == 200
    ghosts = response.json()
    # Check that all expected ghosts are present with correct initial states
    expected_ghost_names = {"blinky", "pinky", "inky", "clyde"}
    assert set(ghosts.keys()) == expected_ghost_names
    for ghost_name, ghost_data in ghosts.items():
        assert "state" in ghost_data
        assert "visual_identifier" in ghost_data
        # Initial state should be 'normal' or equivalent
        assert ghost_data["state"] in {"normal", "chase", "idle", "ambush", "scatter", "frightened", "eaten"}

@pytest.mark.asyncio
async def test_post_ghost_state_and_get_reflects_change():
    ghost_name = "blinky"
    new_state = "frightened"
    async with AsyncClient(app=app, base_url="http://test") as ac:
        post_response = await ac.post(f"/ghosts/{ghost_name}/state", json={"state": new_state})
        assert post_response.status_code == 200
        get_response = await ac.get("/ghosts")
        assert get_response.status_code == 200
        ghosts = get_response.json()
        assert ghosts[ghost_name]["state"] == new_state
        assert "visual_identifier" in ghosts[ghost_name]
