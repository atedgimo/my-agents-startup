"""
Pellet collection backend logic for Chomp game.
Handles API endpoints and data management for pellets in the maze.
"""
import os
import json
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from threading import Lock

router = APIRouter()

DATA_DIR = os.getenv('DATA_DIR', '.')
PELLETS_FILE = os.path.join(DATA_DIR, 'pellets.json')

pellets_lock = Lock()

# Pellets data structure: set of tuples (x, y) for pellet positions
pellets = set()

# Load pellets from file

def load_pellets():
    global pellets
    try:
        if os.path.exists(PELLETS_FILE):
            with open(PELLETS_FILE, 'r') as f:
                data = json.load(f)
                # Expecting list of positions [{"x": int, "y": int}, ...]
                pellets = set((p['x'], p['y']) for p in data)
        else:
            pellets = set()
    except Exception as e:
        pellets = set()

# Save pellets to file

def save_pellets():
    with pellets_lock:
        data = [{'x': x, 'y': y} for (x, y) in pellets]
        with open(PELLETS_FILE, 'w') as f:
            json.dump(data, f)

# Initialize pellets on startup
load_pellets()

@router.get("/pellets")
async def get_pellets():
    """Return current pellets positions."""
    with pellets_lock:
        return [{'x': x, 'y': y} for (x, y) in pellets]

@router.post("/collect_pellet")
async def collect_pellet(request: Request):
    """Handle pellet collection by Pac-Man at a given position."""
    try:
        data = await request.json()
        x = data.get('x')
        y = data.get('y')
        if x is None or y is None:
            raise ValueError("Missing x or y in request")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid request data: {str(e)}")

    pos = (x, y)
    is_power_pellet = False
    with pellets_lock:
        if pos in pellets:
            pellets.remove(pos)
            # Detect if this was a power pellet (mazeData not available here, so use a convention: power pellets at corners)
            if (x, y) in [(1,1), (1,18), (18,1), (18,18)]:
                is_power_pellet = True
            save_pellets()
            return {"message": "Pellet collected", "position": {"x": x, "y": y}, "power_pellet": is_power_pellet}
        else:
            raise HTTPException(status_code=404, detail="Pellet not found at given position")

# Trivial whitespace change to force commit

