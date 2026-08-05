from enum import Enum
import time

class GhostState(str, Enum):
    CHASE = 'chase'
    AMBUSH = 'ambush'
    PATROL = 'patrol'
    RANDOM = 'random'
    FLEE = 'flee'
    EATEN = 'eaten'

class Ghost:
    def __init__(self, name, initial_state):
        self.name = name
        self.initial_state = initial_state
        self.state = initial_state
        self.edible_until = 0

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def is_edible(self):
        return self.state == GhostState.FLEE and time.time() < self.edible_until

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
        return {name: ghost.get_state() for name, ghost in self.ghosts.items()}

    def get_ghost_state(self, name):
        return self.ghosts[name].get_state()

    def set_ghost_state(self, name, state):
        self.ghosts[name].set_state(state)

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
            for ghost in self.ghosts.values():
                ghost.set_state(ghost.initial_state)

        if not self.power_pellet_active:
            for ghost in self.ghosts.values():
                if ghost.get_state() == GhostState.FLEE:
                    ghost.set_state(ghost.initial_state)
