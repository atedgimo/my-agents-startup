from enum import Enum

from enum import Enum
import time

class GhostState(Enum):
    IDLE = 'idle'
    CHASE = 'chase'
    FRIGHTENED = 'frightened'
    FLEE = 'flee'
    EATEN = 'eaten'
    AMBUSH = 'ambush'
    PATROL = 'patrol'
    RANDOM = 'random'

class GhostIdentity:
    BLINKY = 'Blinky'
    PINKY = 'Pinky'
    INKY = 'Inky'
    CLYDE = 'Clyde'

class Ghost:
    def __init__(self, name):
        self.name = name
        self.state = GhostState.CHASE
        self.original_state = self.state
        self.edible_until = 0

    def update_state(self, player_powered_up=False):
        current_time = time.time()
        if player_powered_up:
            self.state = GhostState.FLEE
            self.edible_until = current_time + 10  # edible for 10 seconds
        elif self.state == GhostState.FLEE and current_time > self.edible_until:
            self.state = self.original_state

    def is_edible(self):
        return self.state == GhostState.FLEE

    def visual_identifier(self):
        return self.state.value

    def __repr__(self):
        return f"<Ghost name={self.name} state={self.state.value}>"
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
