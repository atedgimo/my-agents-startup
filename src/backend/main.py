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
from src.backend.ghost_ai import GhostManager, GhostState, GhostIdentity

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

# Scores storage in memory for simplicity, persisted in file

# Declare globals here
DATA_DIR = os.getenv('DATA_DIR', '.')
SCORES_FILE = os.path.join(DATA_DIR, 'scores.json')
scores = []
scores_lock = threading.Lock()

input_buffer = InputBuffer()
ghost_manager = GhostManager()

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

@app.post("/submit-score")
async def submit_score(request: Request):
    """Submit a new score to be saved."""
    global scores
    try:
        data = await request.json()
        score_value = data.get('score')
        if not isinstance(score_value, int) or score_value < 0:
            return JSONResponse(status_code=400, content={"error": "Invalid score value"})
        with scores_lock:
            scores.append(score_value)
            # Keep only top 10 scores descending
            scores.sort(reverse=True)
            scores = scores[:10]
            # Save scores to file
            try:
                with open(SCORES_FILE, 'w') as f:
                    json.dump(scores, f)
            except Exception as e:
                logging.error(f"Failed to save scores to {SCORES_FILE}: {e}")
        return JSONResponse(status_code=200, content={"message": "Score submitted successfully"})
    except Exception as e:
        logging.error(f"Error in submit_score: {e}")
        return JSONResponse(status_code=500, content={"error": "Internal server error"})

@app.get("/scores")
async def get_scores():
    """Return the top scores."""
    with scores_lock:
        return JSONResponse(content={"scores": scores})

# Mount static files for frontend
app.mount("/static", StaticFiles(directory="src/frontend"), name="static")

# TODO: Implement /ghost-states, /activate-power-pellet, /deactivate-power-pellet endpoints

