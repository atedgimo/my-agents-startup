"""
Main backend FastAPI app integration for game logic including input buffer and movement smoothing.
"""
import os
import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from enum import Enum
import json

logging.basicConfig(level=logging.INFO)

app = FastAPI()

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
DATA_DIR = os.getenv('DATA_DIR', '.')
SCORES_FILE = os.path.join(DATA_DIR, 'scores.json')
scores = []

input_buffer = InputBuffer()

@app.on_event("startup")
async def startup_event():
    global scores
    logging.info(f"Starting up app with DATA_DIR={DATA_DIR}")
    if not os.path.isdir(DATA_DIR):
        logging.warning(f"DATA_DIR {DATA_DIR} is not a directory or does not exist, creating it")
        try:
            os.makedirs(DATA_DIR, exist_ok=True)
        except Exception as e:
            logging.error(f"Failed to create DATA_DIR {DATA_DIR}: {e}")
            # We do not raise here to avoid crash, but scores persistence will fail

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

@app.post("/input")
async def receive_input(request: Request):
    """Receive player input direction and queue it."""
    data = await request.json()
    direction_str = data.get('direction', 'NONE').upper()
    try:
        direction = Direction[direction_str]
    except KeyError:
        return JSONResponse(status_code=400, content={"error": "Invalid direction"})

    input_buffer.queue_input(direction)
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

    return {
        "position": current_position,
        "direction": current_dir.name
    }

@app.post("/clear_input")
async def clear_input_buffer():
    """Clear the input buffer and reset direction."""
    input_buffer.clear()
    return {"message": "Input buffer cleared"}

@app.get("/scores")
async def get_scores():
    """Return the list of high scores as JSON."""
    return scores

@app.post("/submit-score")
async def submit_score(request: Request):
    """Accept a new score submission and persist it."""
    data = await request.json()
    name = data.get('name', 'Anonymous')
    score_value = data.get('score')
    if score_value is None or not isinstance(score_value, int):
        return JSONResponse(status_code=400, content={"error": "Score must be an integer"})

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

# Mount static files for frontend
# Changed to mount from current directory 'src/backend/static' assuming static files are here or adjust as needed
static_dir = os.path.join(os.path.dirname(__file__), 'static')
if os.path.isdir(static_dir):
    app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")
else:
    logging.warning(f"Static directory {static_dir} does not exist, static files not mounted")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
