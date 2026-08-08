from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from src.backend.ghost_ai import GhostManager, GhostState, GhostIdentity
from src.backend.pellet_collection import router as pellet_router

app = FastAPI()
app.include_router(pellet_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

ghost_manager = GhostManager()

@app.get("/ghosts")
async def get_ghosts():
    states = ghost_manager.get_all_states()
    visuals = ghost_manager.get_all_visuals()
    print("[DEBUG] /ghosts endpoint returning:")
    for k, v in states.items():
        print(f"  [DEBUG] {k}: {v} (visual: {visuals[k]})")
    # Return both state and visual for each ghost
    return {k: {"state": states[k], "visual": visuals[k]} for k in states}

@app.get("/ghost-states")
async def get_ghost_states():
    # Alias for /ghosts for test compatibility
    return ghost_manager.get_all_states()

@app.get("/ghost-visuals")
async def get_ghost_visuals():
    # API endpoint to get all ghost visuals
    return ghost_manager.get_all_visuals()

@app.post("/ghost_state")
async def set_ghost_state(identity: str = Query(...), state: str = Query(...)):
    try:
        state_enum = GhostState[state.upper()]
    except KeyError:
        return {"error": "Invalid ghost state"}
    ghost_manager.set_ghost_state(identity, state_enum)
    print(f"[DEBUG] /ghost_state set {identity} to {state_enum}")
    return {"status": "success"}

@app.post("/activate_power_pellet")
async def activate_power_pellet():
    ghost_manager.activate_power_pellet()
    print("[DEBUG] /activate_power_pellet called")
    return {"status": "power pellet activated"}

@app.post("/activate-power-pellet")
async def activate_power_pellet_alias():
    # Alias for test compatibility
    ghost_manager.activate_power_pellet()
    print("[DEBUG] /activate-power-pellet called")
    return {"status": "power pellet activated"}

@app.post("/deactivate_power_pellet")
async def deactivate_power_pellet():
    ghost_manager.deactivate_power_pellet()
    print("[DEBUG] /deactivate_power_pellet called")
    return {"status": "power pellet deactivated"}

@app.post("/deactivate-power-pellet")
async def deactivate_power_pellet_alias():
    # Alias for test compatibility
    ghost_manager.deactivate_power_pellet()
    print("[DEBUG] /deactivate-power-pellet called")
    return {"status": "power pellet deactivated"}

@app.post("/update_ghosts")
async def update_ghosts():
    ghost_manager.update()
    print("[DEBUG] /update_ghosts called")
    return {"status": "ghosts updated"}
