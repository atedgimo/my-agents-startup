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
from src.backend.ghost_visuals import GhostManager, GhostIdentity, GhostState

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

from fastapi import Query
from src.backend.ghost_ai import GhostManager

# Initialize ghost manager with starting positions
ghost_start_positions = {
    'Blinky': {'x': 5, 'y': 5},
    'Pinky': {'x': 10, 'y': 5},
    'Inky': {'x': 5, 'y': 10},
    'Clyde': {'x': 10, 'y': 10}
}
ghost_manager = GhostManager(ghost_start_positions)

@app.get("/ghosts")
async def get_ghosts(player_x: int = Query(0), player_y: int = Query(0)):
    """Get current ghost states and positions based on player position."""
    player_position = {'x': player_x, 'y': player_y}
    ghost_manager.update(player_position)
    ghosts_info = ghost_manager.get_ghosts_info()
    return {"ghosts": ghosts_info}


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

    # Bound and sanitise the name before it is persisted. Nothing renders the
    # leaderboard yet, so this is not exploitable today — but the whole point
    # of the endpoint is to be displayed, and an unbounded, unescaped string
    # sitting in a JSON file is stored XSS waiting for a frontend.
    name = str(data.get('name', 'Anonymous'))[:24]
    name = ''.join(c for c in name if c.isprintable() and c not in '<>&"\'')
    name = name.strip() or 'Anonymous'
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


# Card 0021: Add endpoint to list all startups
from fastapi import HTTPException
import sqlite3

@app.get("/startups")
async def list_startups():
    data_dir = os.getenv("DATA_DIR")
    if not data_dir:
        raise HTTPException(status_code=500, detail="DATA_DIR environment variable not set")

    db_path = f"{data_dir}/startups.db"
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, description FROM startups")
        rows = cursor.fetchall()
        startups = [{"id": row[0], "name": row[1], "description": row[2]} for row in rows]
        conn.close()
        return startups
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

