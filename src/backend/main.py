"""
Main backend FastAPI app integration for game logic including input buffer and movement smoothing.
"""
import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from enum import Enum, auto
from src.backend.input_buffer import InputBuffer, Direction, smooth_transition

app = FastAPI()

# Initialize input buffer
input_buffer = InputBuffer()

# Game state placeholder
current_position = {'x': 0, 'y': 0}

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

# Note: The app reads data directory from DATA_DIR env var if needed for persistence or config


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
