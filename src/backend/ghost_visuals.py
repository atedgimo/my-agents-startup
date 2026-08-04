from enum import Enum
import time

class GhostState(Enum):
    CHASE = 'chase'
    AMBUSH = 'ambush'
    PATROL = 'patrol'
    RANDOM = 'random'
    FLEE = 'flee'
    EATEN = 'eaten'

class GhostIdentity:
    BLINKY = 'Blinky'
    PINKY = 'Pinky'
    INKY = 'Inky'
    CLYDE = 'Clyde'

class Ghost:
    def __init__(self, identity, state):
        self.identity = identity
        self.state = state
        self.edible_until = 0

    def is_edible(self):
        return time.time() < self.edible_until

    def set_state(self, state):
        self.state = state

class GhostManager:
    def __init__(self):
        self.ghosts = {
            GhostIdentity.BLINKY: Ghost(GhostIdentity.BLINKY, GhostState.CHASE),
            GhostIdentity.PINKY: Ghost(GhostIdentity.PINKY, GhostState.CHASE),
            GhostIdentity.INKY: Ghost(GhostIdentity.INKY, GhostState.CHASE),
            GhostIdentity.CLYDE: Ghost(GhostIdentity.CLYDE, GhostState.CHASE),
        }
        self.power_pellet_active = False
        self.power_pellet_end_time = 0

    def get_all_states(self):
        return {ghost.identity: ghost.state.value for ghost in self.ghosts.values()}

    def get_ghost_state(self, identity):
        return self.ghosts[identity].state

    def set_ghost_state(self, identity, state):
        self.ghosts[identity].set_state(state)

    def activate_power_pellet(self, duration=10):
        self.power_pellet_active = True
        self.power_pellet_end_time = time.time() + duration
        for ghost in self.ghosts.values():
            ghost.set_state(GhostState.FLEE)
            ghost.edible_until = self.power_pellet_end_time

    def deactivate_power_pellet(self):
        self.power_pellet_active = False

    def update(self):
        if self.power_pellet_active and time.time() > self.power_pellet_end_time:
            self.power_pellet_active = False
            # revert to original states
            self.ghosts[GhostIdentity.BLINKY].set_state(GhostState.CHASE)
            self.ghosts[GhostIdentity.PINKY].set_state(GhostState.AMBUSH)
            self.ghosts[GhostIdentity.INKY].set_state(GhostState.PATROL)
            self.ghosts[GhostIdentity.CLYDE].set_state(GhostState.RANDOM)
