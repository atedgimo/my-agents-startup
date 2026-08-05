from enum import Enum

class GhostState(Enum):
    CHASE = 'chase'
    SCATTER = 'scatter'
    FRIGHTENED = 'frightened'

class GhostManager:
    def __init__(self):
        self.ghosts = {}

    def add_ghost(self, ghost_id, state=GhostState.SCATTER):
        self.ghosts[ghost_id] = state

    def get_state(self, ghost_id):
        return self.ghosts.get(ghost_id, None)

    def set_state(self, ghost_id, state):
        if ghost_id in self.ghosts:
            self.ghosts[ghost_id] = state

    def all_ghosts(self):
        return self.ghosts.items()

