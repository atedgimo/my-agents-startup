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
    def __init__(self, name, initial_state):
        self.name = name
        self.initial_state = initial_state
        self.state = initial_state
        self.edible_timer = None

    def set_state(self, state):
        self.state = state
        if state == GhostState.FLEE:
            self.edible_timer = time.time() + 10  # 10 seconds edible
        elif state != GhostState.FLEE:
            self.edible_timer = None

    def is_edible(self):
        if self.state == GhostState.FLEE:
            return True
        if self.state == GhostState.EATEN:
            return False
        if self.edible_timer and time.time() <= self.edible_timer:
            return True
        return False

    def update(self):
        if self.state == GhostState.FLEE and self.edible_timer and time.time() > self.edible_timer:
            self.state = self.initial_state
            self.edible_timer = None

class GhostManager:
    def __init__(self):
        self.ghosts = {
            'Blinky': Ghost('Blinky', GhostState.CHASE),
            'Pinky': Ghost('Pinky', GhostState.AMBUSH),
            'Inky': Ghost('Inky', GhostState.PATROL),
            'Clyde': Ghost('Clyde', GhostState.RANDOM),
        }
        self.power_pellet_active = False

    def activate_power_pellet(self):
        self.power_pellet_active = True
        for ghost in self.ghosts.values():
            ghost.set_state(GhostState.FLEE)

    def deactivate_power_pellet(self):
        self.power_pellet_active = False

    def update(self):
        for ghost in self.ghosts.values():
            ghost.update()

    def get_ghost_state(self, name):
        return self.ghosts[name].state

    def set_ghost_state(self, name, state):
        self.ghosts[name].set_state(state)

    def get_all_states(self):
        return {name: ghost.state.value for name, ghost in self.ghosts.items()}

    def get_ghost_states(self):
        return {name: ghost.state for name, ghost in self.ghosts.items()}

    @property
    def ghosts_list(self):
        return list(self.ghosts.values())

    @property
    def ghosts(self):
        return self._ghosts

    @ghosts.setter
    def ghosts(self, value):
        self._ghosts = value
