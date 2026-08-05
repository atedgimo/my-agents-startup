from enum import Enum

class GhostState(Enum):
    IDLE = 1
    CHASE = 2
    FRIGHTENED = 3

class Ghost:
    def __init__(self, name):
        self.name = name
        self.state = GhostState.IDLE

    def activate(self):
        self.state = GhostState.CHASE

    def sleep(self):
        self.state = GhostState.FRIGHTENED

    def is_active(self) -> bool:
        return self.state == GhostState.CHASE

    def __repr__(self):
        return f"<Ghost name={self.name} state={self.state.name}>"
