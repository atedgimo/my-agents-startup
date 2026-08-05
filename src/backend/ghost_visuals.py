from enum import Enum, auto

class GhostState(Enum):
    CHASE = auto()
    SCATTER = auto()
    FRIGHTENED = auto()

class GhostManager:
    def __init__(self):
        self.ghosts = {}

    def add_ghost(self, ghost_id, initial_state=GhostState.SCATTER):
        self.ghosts[ghost_id] = initial_state

    def set_state(self, ghost_id, state):
        if ghost_id in self.ghosts:
            self.ghosts[ghost_id] = state

    def get_state(self, ghost_id):
        return self.ghosts.get(ghost_id, None)

    def get_all_states(self):
        return self.ghosts.copy()
