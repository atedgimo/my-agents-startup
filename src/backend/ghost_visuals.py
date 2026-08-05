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
    def __init__(self, name, initial_state):
        self.name = name
        self.state = initial_state
        self.edible = False
        self.edible_start_time = None

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def is_edible(self):
        return self.edible

    def make_edible(self):
        self.edible = True
        self.edible_start_time = time.time()
        self.state = GhostState.FLEE

    def make_normal(self):
        self.edible = False
        self.edible_start_time = None

    def update(self):
        if self.edible and self.edible_start_time:
            if time.time() - self.edible_start_time > 10:  # edible lasts 10 seconds
                self.make_normal()
                self.state = self.initial_state

class GhostManager:
    def __init__(self):
        self.ghosts = {
            'Blinky': Ghost('Blinky', GhostState.CHASE),
            'Pinky': Ghost('Pinky', GhostState.AMBUSH),
            'Inky': Ghost('Inky', GhostState.PATROL),
            'Clyde': Ghost('Clyde', GhostState.RANDOM),
        }

    def get_all_states(self):
        return {name: ghost.get_state().value for name, ghost in self.ghosts.items()}

    def set_ghost_state(self, name, state):
        if name in self.ghosts and isinstance(state, GhostState):
            self.ghosts[name].set_state(state)

    def get_ghost_state(self, name):
        if name in self.ghosts:
            return self.ghosts[name].get_state()
        return None

    def activate_power_pellet(self):
        for ghost in self.ghosts.values():
            ghost.make_edible()

    def deactivate_power_pellet(self):
        for ghost in self.ghosts.values():
            ghost.make_normal()

    def update(self):
        for ghost in self.ghosts.values():
            ghost.update()
