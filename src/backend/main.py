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

app = FastAPI()

from src.backend.pellet_collection import router as pellet_router
# Removed import of non-existent ghost_ai module to fix import errors
from src.backend.ghost_visuals import GhostManager, GhostIdentity, GhostState


# Temporarily comment out ghost_ai import to fix startup crash
# from src.backend.ghost_ai import GhostAI

from fastapi import APIRouter, Query
# from src.backend.ghosts import GhostManager, GhostIdentity, GhostState  # Removed to fix missing module error

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
app.include_router(pellet_router)

logging.basicConfig(level=logging.INFO)

# Allow the browser frontend to call this API
# allow_credentials=True together with allow_origins=["*"] is the classic CORS
# mistake: Starlette then echoes the caller's own origin back, so ANY site can
# make credentialed requests to this API. This app has no cookies or auth, so
# credentials are simply switched off rather than pretended to be safe.
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

# from src.backend.boundary_enforcement import enforce_boundaries  # Temporarily commented out to avoid import error

# from src.backend.boundary_enforcement import enforce_boundaries


@app.post("/enforce_boundaries")
async def api_enforce_boundaries(current_x: int, current_y: int, desired_x: int, desired_y: int):
    """API endpoint to enforce boundaries on a desired position."""
    # Implement boundary enforcement here directly
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

@app.post("/move_player")
async def move_player(new_x: int, new_y: int):
    global current_position
    # Enforce boundary rules
    x = new_x
    y = new_y

    if x < 0:
        x = 0
    elif x >= MAZE_WIDTH:
        x = MAZE_WIDTH - 1

    if y < 0:
        y = 0
    elif y >= MAZE_HEIGHT:
        y = MAZE_HEIGHT - 1

    new_pos = {'x': x, 'y': y}
    current_position = new_pos
    return {"position": current_position}


# Scores storage in memory for simplicity, persisted in file

# Declare globals here
DATA_DIR = os.getenv('DATA_DIR', '.')
SCORES_FILE = os.path.join(DATA_DIR, 'scores.json')


[... truncated ...]
