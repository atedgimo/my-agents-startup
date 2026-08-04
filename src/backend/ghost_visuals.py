from enum import Enum, auto
import time

class GhostIdentity(Enum):
    BLINKY = auto()
    PINKY = auto()
    INKY = auto()
    CLYDE = auto()

class GhostState(Enum):
    CHASE = auto()
    AMBUSH = auto()
    PATROL = auto()
    RANDOM = auto()
    FLEE = auto()
    EDIBLE = auto()

class Ghost:
    def __init__(self, identity):
        self.identity = identity
        self.state = GhostState.PATROL
        self.edible_until = 0

    def set_state(self, state):
        self.state = state
        if state == GhostState.EDIBLE:
            self.edible_until = time.time() + 10  # edible for 10 seconds

    def update(self):
        if self.state == GhostState.EDIBLE and time.time() > self.edible_until:
            self.state = GhostState.PATROL

class GhostManager:
    def __init__(self):
        self.ghosts = {
            GhostIdentity.BLINKY: Ghost(GhostIdentity.BLINKY),
            GhostIdentity.PINKY: Ghost(GhostIdentity.PINKY),
            GhostIdentity.INKY: Ghost(GhostIdentity.INKY),
            GhostIdentity.CLYDE: Ghost(GhostIdentity.CLYDE),
        }

    def get_all_states(self):
        return {ghost_id.name: ghost.state.name for ghost_id, ghost in self.ghosts.items()}

    def set_ghost_state(self, identity, state):
        if identity in self.ghosts:
            self.ghosts[identity].set_state(state)

    def update_all(self):
        for ghost in self.ghosts.values():
            ghost.update()

# Singleton instance
ghost_manager = GhostManager()
