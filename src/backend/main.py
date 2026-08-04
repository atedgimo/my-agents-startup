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
from fastapi import APIRouter, Query

# Commented out ghost imports to fix missing module errors
# from src.backend.ghost_ai import GhostAI
# from src.backend.ghost_visuals import GhostManager, GhostIdentity, GhostState

router = APIRouter()

# Register pellet collection router
app = FastAPI()
app.include_router(pellet_router)

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

