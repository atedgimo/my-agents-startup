from enum import Enum

class GhostState(Enum):
    CHASE = 1
    SCATTER = 2
    FRIGHTENED = 3

class GhostIdentity(Enum):
    BLINKY = 1
    PINKY = 2
    INKY = 3
    CLYDE = 4

class GhostManager:
    def __init__(self):
        self.ghosts = {}

    def add_ghost(self, identity, state):
        self.ghosts[identity] = state

    def get_all_states(self):
        return {identity.name: state.name for identity, state in self.ghosts.items()}

    def set_ghost_state(self, identity, state):
        if identity in self.ghosts:
            self.ghosts[identity] = state
