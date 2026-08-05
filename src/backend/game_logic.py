from enum import Enum, auto

class GhostState(Enum):
    NORMAL = auto()
    FRIGHTENED = auto()
    EATEN = auto()

class Ghost:
    def __init__(self, name):
        self.name = name
        self.state = GhostState.NORMAL

    def visual_identifier(self):
        # Return visual identifier based on ghost state
        if self.state == GhostState.NORMAL:
            return self.name
        elif self.state == GhostState.FRIGHTENED:
            return f"{self.name}_frightened"
        elif self.state == GhostState.EATEN:
            return f"{self.name}_eaten"

    def update_state(self, player_powered_up):
        # Update ghost state based on player power-up state
        if player_powered_up:
            if self.state == GhostState.NORMAL:
                self.state = GhostState.FRIGHTENED
        else:
            if self.state == GhostState.FRIGHTENED:
                self.state = GhostState.NORMAL

    def eaten(self):
        # When ghost is eaten by player
        self.state = GhostState.EATEN

    def reset(self):
        # Reset ghost to normal state
        self.state = GhostState.NORMAL
