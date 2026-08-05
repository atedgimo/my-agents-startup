"""
Main backend FastAPI app integration for game logic including input buffer and movement smoothing.
"""

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from src.backend.ghost_ai import Ghost, GhostState
from src.backend.pellet_collection import router as pellet_router

class GhostManager:
    def __init__(self):
        self.ghosts = {
            'Blinky': Ghost('Blinky'),
            'Pinky': Ghost('Pinky'),
            'Inky': Ghost('Inky'),
            'Clyde': Ghost('Clyde')
        }

    def get_all_states(self):
        return {name: ghost.visual_identifier() for name, ghost in self.ghosts.items()}

    def set_ghost_state(self, identity, state):
        if identity in self.ghosts:
            self.ghosts[identity].state = state
            self.ghosts[identity].original_state = state

    def activate_power_pellet(self):
        for ghost in self.ghosts.values():
            ghost.update_state(player_powered_up=True)

    def deactivate_power_pellet(self):
        # Reset ghosts to their original states
        for ghost in self.ghosts.values():
            ghost.state = ghost.original_state

    def update(self):
        for ghost in self.ghosts.values():
            ghost.update_state(player_powered_up=False)

# Initialize ghost manager
ghost_manager = GhostManager()

# Register pellet collection router
app = FastAPI()
app.include_router(pellet_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

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

# Other existing backend code continues here...
