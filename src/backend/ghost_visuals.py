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
    def __init__(self, identity: GhostIdentity):
        self.identity = identity
        self.state = GhostState.PATROL
        self.edible_until = 0

    def set_state(self, state: GhostState):
        self.state = state

    def activate_power_pellet(self):
        self.state = GhostState.FLEE
        self.edible_until = time.time() + 10  # Edible for 10 seconds

    def update(self):
        if self.state == GhostState.FLEE and time.time() > self.edible_until:
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
        return {identity.name: ghost.state.name for identity, ghost in self.ghosts.items()}

    def set_ghost_state(self, identity: GhostIdentity, state: GhostState):
        if identity in self.ghosts:
            self.ghosts[identity].set_state(state)

    def activate_power_pellet(self):
        for ghost in self.ghosts.values():
            ghost.activate_power_pellet()

    def update(self):
        for ghost in self.ghosts.values():
            ghost.update()
