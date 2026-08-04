from enum import Enum, auto
from typing import Dict

class GhostState(Enum):
    CHASE = auto()
    AMBUSH = auto()
    PATROL = auto()
    RANDOM = auto()
    FLEE = auto()
    EDIBLE = auto()

class Ghost:
    def __init__(self, name: str, state: GhostState):
        self.name = name
        self.state = state

    def set_state(self, new_state: GhostState):
        self.state = new_state

    def get_visual_identifier(self) -> str:
        # Return a visual identifier string based on the ghost's state
        if self.state == GhostState.CHASE:
            return f"{self.name}_chase"
        elif self.state == GhostState.AMBUSH:
            return f"{self.name}_ambush"
        elif self.state == GhostState.PATROL:
            return f"{self.name}_patrol"
        elif self.state == GhostState.RANDOM:
            return f"{self.name}_random"
        elif self.state == GhostState.FLEE:
            return f"{self.name}_flee"
        elif self.state == GhostState.EDIBLE:
            return f"{self.name}_edible"
        else:
            return f"{self.name}_unknown"

# Factory function to create four ghosts with distinct behaviours

def create_ghosts() -> Dict[str, Ghost]:
    return {
        "blinky": Ghost("blinky", GhostState.CHASE),
        "pinky": Ghost("pinky", GhostState.AMBUSH),
        "inky": Ghost("inky", GhostState.PATROL),
        "clyde": Ghost("clyde", GhostState.RANDOM),
    }
