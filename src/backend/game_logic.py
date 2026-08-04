# Backend game logic for enhanced visual feedback and accessibility

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

class GameState:
    def __init__(self):
        self.pellet_consumed = False
        self.ghost_state = 'normal'  # could be 'normal', 'frightened', 'eaten'
        self.power_pellet_active = False

    def consume_pellet(self):
        self.pellet_consumed = True

    def set_ghost_state(self, state: str):
        self.ghost_state = state

    def activate_power_pellet(self):
        self.power_pellet_active = True

    def reset_states(self):
        self.pellet_consumed = False
        self.ghost_state = 'normal'
        self.power_pellet_active = False

# Simulated game state instance
game_state = GameState()

@router.get("/game/visual-feedback")
async def get_visual_feedback():
    return JSONResponse(content={
        "pellet_consumed": game_state.pellet_consumed,
        "ghost_state": game_state.ghost_state,
        "power_pellet_active": game_state.power_pellet_active
    })

@router.post("/game/consume-pellet")
async def consume_pellet():
    game_state.consume_pellet()
    return {"status": "pellet consumed"}

@router.post("/game/set-ghost-state/{state}")
async def set_ghost_state(state: str):
    if state not in ['normal', 'frightened', 'eaten']:
        return JSONResponse(status_code=400, content={"error": "Invalid ghost state"})
    game_state.set_ghost_state(state)
    return {"status": f"ghost state set to {state}"}

@router.post("/game/activate-power-pellet")
async def activate_power_pellet():
    game_state.activate_power_pellet()
    return {"status": "power pellet activated"}

@router.post("/game/reset-visual-states")
async def reset_visual_states():
    game_state.reset_states()
    return {"status": "visual states reset"}
