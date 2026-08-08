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
    return ghost_manager.get_all_states()

@app.post("/ghost_state")
async def set_ghost_state(identity: str = Query(...), state: str = Query(...)):
    try:
        state_enum = GhostState[state.upper()]
    except KeyError:
        return {"error": "Invalid ghost state"}
    ghost_manager.set_ghost_state(identity, state_enum)
    return {"status": "success"}

@app.post("/activate_power_pellet")
async def activate_power_pellet():
    ghost_manager.activate_power_pellet()
    return {"status": "power pellet activated"}

@app.post("/deactivate_power_pellet")
async def deactivate_power_pellet():
    ghost_manager.deactivate_power_pellet()
    return {"status": "power pellet deactivated"}

@app.post("/update_ghosts")
async def update_ghosts():
    ghost_manager.update()
    return {"status": "ghosts updated"}
