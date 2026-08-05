from enum import Enum, auto

class GhostIdentity(Enum):
    BLINKY = auto()
    PINKY = auto()
    INKY = auto()
    CLYDE = auto()

class GhostState(Enum):
    CHASING = auto()
    SCATTERING = auto()
    FRIGHTENED = auto()

class GhostManager:
    def __init__(self):
        self.ghosts = {identity: GhostState.CHASING for identity in GhostIdentity}

    def get_state(self, ghost_identity):
        return self.ghosts.get(ghost_identity, None)

    def set_state(self, ghost_identity, state):
        if ghost_identity in self.ghosts:
            self.ghosts[ghost_identity] = state

    def all_states(self):
        return self.ghosts.copy()
