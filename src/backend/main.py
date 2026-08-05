"""
Main backend FastAPI app integration for game logic including input buffer and movement smoothing.
"""

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from src.backend.ghost_visuals import GhostIdentity, GhostState
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

class GhostManager:
    def __init__(self):
        self.ghosts = {identity: GhostState.CHASING for identity in GhostIdentity}

    def get_all_states(self):
        return {ghost.name: state.name for ghost, state in self.ghosts.items()}

    def set_ghost_state(self, identity, state):
        if identity in self.ghosts:
            self.ghosts[identity] = state

    def activate_power_pellet(self):
        for ghost in self.ghosts:
            self.ghosts[ghost] = GhostState.FRIGHTENED

    def deactivate_power_pellet(self):
        for ghost in self.ghosts:
            self.ghosts[ghost] = GhostState.CHASING

    def update(self):
        # Placeholder for ghost state update logic
        pass

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

# Other existing backend code continues here...

import os
import logging
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from enum import Enum
import json
import threading

from fastapi import APIRouter

# Additional backend code can be added below as needed
