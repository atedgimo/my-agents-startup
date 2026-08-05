from enum import Enum

class GhostState(Enum):
    CHASE = 'chase'
    SCATTER = 'scatter'
    FRIGHTENED = 'frightened'

class GhostIdentity(Enum):
    BLINKY = 'blinky'
    PINKY = 'pinky'
    INKY = 'inky'
    CLYDE = 'clyde'

class GhostManager:
    def __init__(self):
        self.ghosts = {identity: GhostState.SCATTER for identity in GhostIdentity}

    def get_all_states(self):
        return {ghost.value: state.value for ghost, state in self.ghosts.items()}

    def set_ghost_state(self, identity, state):
        if identity in self.ghosts:
            self.ghosts[identity] = state

    def activate_power_pellet(self):
        for ghost in self.ghosts:
            self.ghosts[ghost] = GhostState.FRIGHTENED

    def update(self):
        # Placeholder for ghost state update logic
        pass

