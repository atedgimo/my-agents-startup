"""
Main backend FastAPI app integration for game logic including input buffer and movement smoothing.
"""

import os
import logging
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from src.backend.pellet_collection import router as pellet_router

# Ghost logic implemented directly here to avoid missing ghost_ai.py module

class Ghost:
    def __init__(self, id):
        self.id = id
        self.state = 'normal'  # 'normal', 'frightened', 'eaten'

    def update_state(self, power_up_active):
        if power_up_active:
            self.state = 'frightened'
        else:
            self.state = 'normal'

    def get_visual_identifier(self):
        if self.state == 'frightened':
            return 'blue'
        elif self.state == 'eaten':
            return 'eyes'
        else:
            return 'normal'

class GhostManager:
    def __init__(self):
        self.ghosts = [Ghost(i) for i in range(4)]

    def update_ghosts(self, power_up_active):
        for ghost in self.ghosts:
            ghost.update_state(power_up_active)

    def get_ghost_visuals(self):
        return [ghost.get_visual_identifier() for ghost in self.ghosts]

ghost_manager = GhostManager()

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
    return ghost_manager.get_ghost_visuals()

@app.post("/ghost_state")
async def set_ghost_state(identity: int = Query(...), state: str = Query(...)):
    for ghost in ghost_manager.ghosts:
        if ghost.id == identity:
            ghost.state = state
            break
    return {"status": "success"}

@app.post("/activate_power_pellet")
async def activate_power_pellet():
    ghost_manager.update_ghosts(power_up_active=True)
    return {"status": "power pellet activated"}

@app.post("/update_ghosts")
async def update_ghosts():
    ghost_manager.update_ghosts(power_up_active=False)
    return {"status": "ghosts updated"}

# Other existing backend code continues here...
