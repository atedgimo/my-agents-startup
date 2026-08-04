from enum import Enum

class GhostState(Enum):
    CHASE = 1
    SCATTER = 2
    FRIGHTENED = 3

class GhostManager:
    def __init__(self):
        self.ghosts = []

    def add_ghost(self, ghost):
        self.ghosts.append(ghost)

    def update_states(self):
        # Placeholder for updating ghost states logic
        pass
