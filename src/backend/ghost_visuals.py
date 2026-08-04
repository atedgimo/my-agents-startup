from enum import Enum, auto
import time

class GhostState(Enum):
    CHASE = 'chase'
    AMBUSH = 'ambush'
    PATROL = 'patrol'
    RANDOM = 'random'
    FLEE = 'flee'
    EATEN = 'eaten'

class Ghost:
    def __init__(self, identity, initial_state):
        self.identity = identity
        self.state = initial_state
        self.edible = False

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def is_edible(self):
        return self.edible

    def set_edible(self, edible):
        self.edible = edible

class GhostManager:
    POWER_PELLET_DURATION = 10  # seconds

    def __init__(self):
        self.ghosts = {
            'Blinky': Ghost('Blinky', GhostState.CHASE),
            'Pinky': Ghost('Pinky', GhostState.AMBUSH),
            'Inky': Ghost('Inky', GhostState.PATROL),
            'Clyde': Ghost('Clyde', GhostState.RANDOM),
        }
        self.power_pellet_active = False
        self.power_pellet_activated_at = None

    def get_all_states(self):
        return {gid: ghost.get_state().value for gid, ghost in self.ghosts.items()}

    def get_ghost_states(self):
        return {gid: ghost.get_state() for gid, ghost in self.ghosts.items()}

    def set_ghost_state(self, ghost_id, state):
        if ghost_id in self.ghosts:
            self.ghosts[ghost_id].set_state(state)

    def get_ghost_state(self, ghost_id):
        if ghost_id in self.ghosts:
            return self.ghosts[ghost_id].get_state()
        return None

    def activate_power_pellet(self):
        self.power_pellet_active = True
        self.power_pellet_activated_at = time.time()
        for ghost in self.ghosts.values():
            ghost.set_state(GhostState.FLEE)
            ghost.set_edible(True)

    def deactivate_power_pellet(self):
        self.power_pellet_active = False
        self.power_pellet_activated_at = None
        for ghost in self.ghosts.values():
            ghost.set_edible(False)

    def update(self):
        if self.power_pellet_active:
            elapsed = time.time() - self.power_pellet_activated_at
            if elapsed > self.POWER_PELLET_DURATION:
                self.deactivate_power_pellet()
                # Revert ghosts to original states
                self.ghosts['Blinky'].set_state(GhostState.CHASE)
                self.ghosts['Pinky'].set_state(GhostState.AMBUSH)
                self.ghosts['Inky'].set_state(GhostState.PATROL)
                self.ghosts['Clyde'].set_state(GhostState.RANDOM)

