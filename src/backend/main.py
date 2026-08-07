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
# # from src.backend.ghost_visuals import GhostManager, GhostIdentity, GhostState  # Disabled import to fix ModuleNotFoundError
# from src.backend.ghost_ai import GhostManager, GhostState, G  # Disabled import to fix ModuleNotFoundError  # Disabled import to fix ModuleNotFoundError

router = APIRouter()

# Initialize ghost manager with starting positions
# ghost_start_positions = {
#     GhostIdentity.BLINKY: {'x': 5, 'y': 5},
#     GhostIdentity.PINKY: {'x': 10, 'y': 5},
#     GhostIdentity.INKY: {'x': 5, 'y': 10},
#     GhostIdentity.CLYDE: {'x': 10, 'y': 10}
# }
# ghost_manager = GhostManager(ghost_start_positions)

input_buffer = InputBuffer()

ghost_manager = GhostManager()

app = FastAPI()

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

# Game state placeholder
current_position = {'x': 0, 'y': 0}

from src.backend.input_buffer import InputBuffer

input_buffer = InputBuffer()

def api_enforce_boundaries(current_x: int, current_y: int, desired_x: int, desired_y: int):
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


@app.post("/enforce_boundaries")
async def enforce_boundaries_endpoint(current_x: int, current_y: int, desired_x: int, desired_y: int):
    return api_enforce_boundaries(current_x, current_y, desired_x, desired_y)


MAZE_WIDTH = 28
MAZE_HEIGHT = 31

@app.post("/move_player")
async def move_player(new_x: int, new_y: int):
    global current_position

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
scores = []
scores_lock = threading.Lock()

# Load scores from file if exists
def load_scores():
    global scores
    try:
        with open(SCORES_FILE, 'r') as f:
            scores = json.load(f)
    except FileNotFoundError:
        scores = []

load_scores()

@app.get("/high_scores")
async def get_high_scores():
    return {"scores": scores}

@app.post("/submit_score")
async def submit_score(player_name: str, score: int):
    global scores
    with scores_lock:
        scores.append({'player': player_name, 'score': score})
        scores.sort(key=lambda x: x['score'], reverse=True)
        scores = scores[:10]  # Keep top 10 scores
        with open(SCORES_FILE, 'w') as f:
            json.dump(scores, f)
    return {"status": "success"}

# Mount static files for frontend
app.mount("/static", StaticFiles(directory="src/frontend/static"), name="static")
