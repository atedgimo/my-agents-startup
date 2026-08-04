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
    def __init__(self, name: str):
        self.name = name
        self.state = GhostState.PATROL

    def set_state(self, state: GhostState):
        self.state = state

    def get_visual_identifier(self) -> str:
        # Return a string identifier for the ghost's visual state
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

class GhostManager:
    def __init__(self):
        self.ghosts: Dict[str, Ghost] = {
            "blinky": Ghost("blinky"),
            "pinky": Ghost("pinky"),
            "inky": Ghost("inky"),
            "clyde": Ghost("clyde")
        }

    def set_ghost_state(self, ghost_name: str, state: GhostState):
        if ghost_name in self.ghosts:
            self.ghosts[ghost_name].set_state(state)

    def get_ghost_visual(self, ghost_name: str) -> str:
        if ghost_name in self.ghosts:
            return self.ghosts[ghost_name].get_visual_identifier()
        return "unknown"

    def get_all_ghosts_visuals(self) -> Dict[str, str]:
        return {name: ghost.get_visual_identifier() for name, ghost in self.ghosts.items()}
