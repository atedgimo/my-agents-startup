"""
Main backend FastAPI app integration for game logic including input buffer and movement smoothing.
"""
import os
import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
import json
import threading

from src.backend.pellet_collection import router as pellet_router

# Removed import of ghost_ai to fix ModuleNotFoundError
# from src.backend.ghost_ai import GhostManager, GhostIdentity, GhostState

# Dummy ghost manager class to allow app to start
class GhostManager:
    def __init__(self):
        self.ghosts = {}

    def get_all_states(self):
        return {}

    def set_ghost_state(self, identity, state):
        pass

    def activate_power_pellet(self):
        pass

    def update(self):
        pass

ghost_manager = GhostManager()

from ghost_ai import *
from ghost_visuals import GhostManager, GhostState
import ghost_ai
from ghost_visuals import GhostManager, GhostState

from fastapi import APIRouter, Query

# Removed import of missing ghost_ai module to fix parse error
from ghost_visuals import GhostManager, GhostIdentity, GhostState

router = APIRouter()

# Initialize ghost manager with starting positions
# ghost_start_positions = {
#     GhostIdentity.BLINKY: {'x': 5, 'y': 5},
#     GhostIdentity.PINKY: {'x': 10, 'y': 5},
#     GhostIdentity.INKY: {'x': 5, 'y': 10},
#     GhostIdentity.CLYDE: {'x': 10, 'y': 10}
# }
# ghost_manager = GhostManager(ghost_start_positions)

# @app.get("/ghosts")
# async def get_ghosts():
#     return ghost_manager.get_all_states()

# @app.post("/ghost_state")
# async def set_ghost_state(identity: GhostIdentity = Query(...), state: GhostState = Query(...)):
#     ghost_manager.set_ghost_state(identity, state)
#     return {"status": "success"}

# Register pellet collection router
app = FastAPI()
app.include_router(pellet_router)

# Initialize ghost manager

ghost_manager = GhostManager()

@app.get("/ghosts")
async def get_ghosts():
    return ghost_manager.get_all_states()

@app.post("/ghost_state")
async def set_ghost_state(identity: GhostIdentity = Query(...), state: GhostState = Query(...)):
    ghost_manager.set_ghost_state(identity, state)
    return {"status": "success"}

@app.post("/activate_power_pellet")
async def activate_power_pellet():
    ghost_manager.activate_power_pellet()
    return {"status": "power pellet activated"}

@app.post("/update_ghosts")
async def update_ghosts():
    ghost_manager.update()
    return {"status": "ghosts updated"}

logging.basicConfig(level=logging.INFO)

# Allow the browser frontend to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

class Direction(str, Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    NONE = 'NONE'

# Input buffer class to queue and smooth input directions
class InputBuffer:
    def __init__(self):
        self.queue = []
        self.current_direction = Direction.NONE

    def queue_input(self, direction):
        self.queue.append(direction)

    def update_direction(self):
        if self.queue:
            self.current_direction = self.queue.pop(0)
        else:
            self.current_direction = Direction.NONE

    def clear(self):
        self.queue.clear()
        self.current_direction = Direction.NONE

# Game state placeholder
current_position = {'x': 0, 'y': 0}

@app.post("/enforce_boundaries")
async def api_enforce_boundaries(current_x: int, current_y: int, desired_x: int, desired_y: int):
    """API endpoint to enforce boundaries on a desired position."""
    MAZE_WIDTH = 28
    MAZE_HEIGHT = 31

    x = desired_x
    y = desired_y

    if x < 0:
        x = 0
    elif x >= MAZE_WIDTH:
        x = MAZE_WIDTH - 1

    if y < 0:
        y = 0
    elif y >= MAZE_HEIGHT:
        y = MAZE_HEIGHT - 1

    return {"x": x, "y": y}

# Maze dimensions placeholder (should be set from actual maze data)
MAZE_WIDTH = 28
MAZE_HEIGHT = 31
