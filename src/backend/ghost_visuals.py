from enum import Enum
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
        self.edible_until = 0

    def is_edible(self):
        return time.time() < self.edible_until

class GhostManager:
    def __init__(self):
        self.ghosts = {
            'Blinky': Ghost('Blinky', GhostState.CHASE),
            'Pinky': Ghost('Pinky', GhostState.AMBUSH),
            'Inky': Ghost('Inky', GhostState.PATROL),
            'Clyde': Ghost('Clyde', GhostState.RANDOM),
        }
        self.power_pellet_active = False
        self.power_pellet_end_time = 0

    def get_all_states(self):
        return {gid: ghost.state.value for gid, ghost in self.ghosts.items()}

    def set_ghost_state(self, ghost_id, state):
        if ghost_id in self.ghosts:
            self.ghosts[ghost_id].state = state

    def get_ghost_state(self, ghost_id):
        if ghost_id in self.ghosts:
            return self.ghosts[ghost_id].state
        return None

    def activate_power_pellet(self, duration=10):
        self.power_pellet_active = True
        self.power_pellet_end_time = time.time() + duration
        for ghost in self.ghosts.values():
            ghost.state = GhostState.FLEE
            ghost.edible_until = self.power_pellet_end_time

    def deactivate_power_pellet(self):
        self.power_pellet_active = False

    def update(self):
        if self.power_pellet_active and time.time() > self.power_pellet_end_time:
            self.power_pellet_active = False
            # revert ghosts to original states
            self.ghosts['Blinky'].state = GhostState.CHASE
            self.ghosts['Pinky'].state = GhostState.AMBUSH
            self.ghosts['Inky'].state = GhostState.PATROL
            self.ghosts['Clyde'].state = GhostState.RANDOM
            for ghost in self.ghosts.values():
                ghost.edible_until = 0
