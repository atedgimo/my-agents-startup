from enum import Enum, auto

class GhostState(Enum):
    CHASE = auto()
    SCATTER = auto()
    FRIGHTENED = auto()

class GhostManager:
    def __init__(self):
        self.ghosts = {}

    def add_ghost(self, name):
        if name not in self.ghosts:
            self.ghosts[name] = GhostState.SCATTER

    def set_state(self, name, state):
        if name in self.ghosts and isinstance(state, GhostState):
            self.ghosts[name] = state

    def get_state(self, name):
        return self.ghosts.get(name, None)

    def get_all_ghosts(self):
        return self.ghosts.copy()
