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

logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Allow the browser frontend to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

@app.post("/input")
async def receive_input(request: Request):
    """Receive player input direction and queue it."""
    try:
        data = await request.json()
    except Exception as e:
        logging.error(f"Invalid JSON input in /input: {e}")
        return JSONResponse(status_code=400, content={"error": "Invalid JSON input"})

    direction_str = data.get('direction', 'NONE').upper()
    try:
        direction = Direction[direction_str]
    except KeyError:
        logging.error(f"Invalid direction received: {direction_str}")
        return JSONResponse(status_code=400, content={"error": "Invalid direction"})

    input_buffer.queue_input(direction)
    logging.info(f"Direction {direction_str} queued")
    return {"message": f"Direction {direction_str} queued"}

@app.get("/move")
async def get_movement():
    """Update movement direction smoothly and return new position."""
    input_buffer.update_direction()
    current_dir = input_buffer.current_direction

    # For demonstration, move one unit per call in the direction
    if current_dir == Direction.UP:
        current_position['y'] += 1
    elif current_dir == Direction.DOWN:
        current_position['y'] -= 1
    elif current_dir == Direction.LEFT:
        current_position['x'] -= 1
    elif current_dir == Direction.RIGHT:
        current_position['x'] += 1

    logging.info(f"Moved {current_dir.name} to position {current_position}")
    return {
        "position": current_position,
        "direction": current_dir.name
    }

@app.post("/clear_input")
async def clear_input_buffer():
    """Clear the input buffer and reset direction."""
    input_buffer.clear()
    logging.info("Input buffer cleared")
    return {"message": "Input buffer cleared"}

@app.get("/scores")
async def get_scores():
    """Return the list of high scores as JSON."""
    with scores_lock:
        return scores

@app.post("/submit-score")
async def submit_score(request: Request):
    """Accept a new score submission and persist it."""
    try:
        data = await request.json()
    except Exception as e:
        logging.error(f"Invalid JSON input in /submit-score: {e}")
        return JSONResponse(status_code=400, content={"error": "Invalid JSON input"})

    name = data.get('name', 'Anonymous')
    score_value = data.get('score')
    if score_value is None or not isinstance(score_value, int):
        logging.error("Score must be an integer")
        return JSONResponse(status_code=400, content={"error": "Score must be an integer"})

    with scores_lock:
        # Append and save
        scores.append({"name": name, "score": score_value})
        # Sort descending
        scores.sort(key=lambda x: x['score'], reverse=True)
        # Keep top 10
        scores[:] = scores[:10]

        # Persist
        try:
            with open(SCORES_FILE, 'w') as f:
                json.dump(scores, f)
            logging.info(f"Scores saved to {SCORES_FILE}")
        except Exception as e:
            logging.error(f"Failed to save scores to {SCORES_FILE}: {e}")
            return JSONResponse(status_code=500, content={"error": f"Failed to save scores: {str(e)}"})

    return {"message": "Score submitted successfully", "scores": scores}

# Mount static files for frontend.
# index.html and game.js live in src/, one level above this file. Resolve from
# __file__ rather than the working directory: the app is started with
# `cd src/backend`, so a relative "src" pointed at src/backend/src and
# StaticFiles raised at import, crash-looping the pod. The isdir guard keeps a
# wrong path from taking the whole API down with it.
static_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if os.path.isdir(static_dir):
    try:
        app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")
        logging.info(f"Static files mounted from {static_dir}")
    except Exception as e:
        logging.error(f"Failed to mount static files from {static_dir}: {e}")
else:
    logging.warning(f"Static directory {static_dir} does not exist, static files not mounted")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
