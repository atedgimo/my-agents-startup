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
from src.backend.input_buffer import InputBuffer

# from src.backend.ghost_ai import GhostManager, GhostState  # Disabled to fix import error

# Removed broken import of src.backend.api which does not exist
# This fixes the ModuleNotFoundError blocking the product start

logging.basicConfig(level=logging.INFO)

app = FastAPI()

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

input_buffer = InputBuffer()

# ghost_manager = GhostManager()  # Disabled to fix import error

class Direction(str, Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    NONE = 'NONE'

# Game state placeholder
current_position = {'x': 0, 'y': 0}

# Scores storage in memory for simplicity, persisted in file

# Declare globals here
DATA_DIR = os.getenv('DATA_DIR', '.')
SCORES_FILE = os.path.join(DATA_DIR, 'scores.json')
scores = []
scores_lock = threading.Lock()

@app.on_event("startup")
async def startup_event():
    global scores
    global DATA_DIR, SCORES_FILE
    logging.info(f"Starting up app with DATA_DIR={DATA_DIR}")
    # Validate DATA_DIR environment variable
    if not DATA_DIR or not isinstance(DATA_DIR, str) or DATA_DIR.strip() == '':
        logging.error("DATA_DIR environment variable is missing or invalid. Falling back to current directory.")
        DATA_DIR = '.'

    # Check if DATA_DIR is a directory or create it
    if os.path.exists(DATA_DIR):
        if not os.path.isdir(DATA_DIR):
            logging.error(f"DATA_DIR {DATA_DIR} exists but is not a directory. Falling back to current directory.")
            DATA_DIR = '.'
    else:
        logging.info(f"DATA_DIR {DATA_DIR} does not exist, creating it")
        try:
            os.makedirs(DATA_DIR, exist_ok=True)
        except Exception as e:
            logging.error(f"Failed to create DATA_DIR {DATA_DIR}: {e}")
            # Fallback to current directory
            DATA_DIR = '.'

    SCORES_FILE = os.path.join(DATA_DIR, 'scores.json')

    # Load scores from file or initialize
    try:
        if os.path.exists(SCORES_FILE):
            with open(SCORES_FILE, 'r') as f:
                scores = json.load(f)
            logging.info(f"Loaded scores from {SCORES_FILE}")
        else:
            logging.info(f"Scores file {SCORES_FILE} does not exist, starting with empty scores")
            scores = []
    except Exception as e:
        logging.error(f"Failed to load scores from {SCORES_FILE}: {e}")
        scores = []

# Register pellet collection router
app.include_router(pellet_router)

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
