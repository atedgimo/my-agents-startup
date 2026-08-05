import time
from enum import Enum

class GhostState(Enum):
    CHASE = 'chase'
    AMBUSH = 'ambush'
    PATROL = 'patrol'
    RANDOM = 'random'
    FLEE = 'flee'
    EATEN = 'eaten'

class Ghost:
    def __init__(self, name, initial_state):
        self.name = name
        self.state = initial_state
        self.original_state = initial_state
        self.edible_until = 0

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def is_edible(self):
        return self.state == GhostState.FLEE

    def update(self):
        current_time = time.time()
        if self.state == GhostState.FLEE and current_time > self.edible_until:
            self.state = self.original_state

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

    def get_ghost_state(self, name):
        return self.ghosts[name].get_state()

    def set_ghost_state(self, name, state):
        self.ghosts[name].set_state(state)

    def get_all_states(self):
        return {name: ghost.get_state().value for name, ghost in self.ghosts.items()}

    def activate_power_pellet(self):
        self.power_pellet_active = True
        self.power_pellet_end_time = time.time() + 10
        for ghost in self.ghosts.values():
            ghost.set_state(GhostState.FLEE)
            ghost.edible_until = self.power_pellet_end_time

    def deactivate_power_pellet(self):
        self.power_pellet_active = False

    def update(self):
        current_time = time.time()
        if self.power_pellet_active and current_time > self.power_pellet_end_time:
            self.power_pellet_active = False
            for ghost in self.ghosts.values():
                ghost.update()

        if not self.power_pellet_active:
            for ghost in self.ghosts.values():
                ghost.update()
