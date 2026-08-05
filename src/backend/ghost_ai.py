from enum import Enum

class GhostState(Enum):
    IDLE = 1
    CHASE = 2
    FRIGHTENED = 3

class Ghost:
    def __init__(self, name):
        self.name = name
        self.state = GhostState.IDLE

    def visual_identifier(self):
        return f"{self.name}-{self.state.name}"

    def update_state(self, player_powered_up=False):
        if player_powered_up:
            self.state = GhostState.FRIGHTENED
        else:
            self.state = GhostState.CHASE
