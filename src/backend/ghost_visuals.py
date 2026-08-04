from enum import Enum
from typing import Optional

class GhostState(Enum):
    NORMAL = "normal"
    FRIGHTENED = "frightened"
    EATEN = "eaten"

class GhostVisualIdentifier:
    def __init__(self, ghost_id: int):
        self.ghost_id = ghost_id
        self.state = GhostState.NORMAL

    def set_state(self, new_state: GhostState):
        if not isinstance(new_state, GhostState):
            raise ValueError("Invalid ghost state")
        self.state = new_state

    def get_visual_identifier(self) -> str:
        # Return a string identifier for the ghost visual based on its state
        if self.state == GhostState.NORMAL:
            return f"ghost_{self.ghost_id}_normal"
        elif self.state == GhostState.FRIGHTENED:
            return f"ghost_{self.ghost_id}_frightened"
        elif self.state == GhostState.EATEN:
            return f"ghost_{self.ghost_id}_eaten"
        else:
            return f"ghost_{self.ghost_id}_unknown"

# Additional logic for ghost visual state transitions could be added here
