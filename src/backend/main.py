"""
Main backend FastAPI app integration for game logic including input buffer and movement smoothing.
"""
import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from enum import Enum
import json

app = FastAPI()

# Initialize input buffer
input_buffer = InputBuffer()

# Game state placeholder
current_position = {'x': 0, 'y': 0}

# Scores storage in memory for simplicity, persisted in file
DATA_DIR = os.getenv('DATA_DIR', '.')
SCORES_FILE = os.path.join(DATA_DIR, 'scores.json')

# Load scores from file or initialize
if os.path.exists(SCORES_FILE):
    with open(SCORES_FILE, 'r') as f:
        try:
            scores = json.load(f)
        except Exception:
            scores = []
else:
    scores = []

class MoveDirection(str, Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    NONE = 'NONE'

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
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Failed to save scores: {str(e)}"})

    return {"message": "Score submitted successfully", "scores": scores}

# Mount static files for frontend
app.mount("/", StaticFiles(directory="src", html=True), name="static")

# Note: The app reads data directory from DATA_DIR env var if needed for persistence or config


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
