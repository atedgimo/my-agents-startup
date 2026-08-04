from enum import Enum, auto
import time

class GhostState(Enum):
    CHASE = auto()
    AMBUSH = auto()
    PATROL = auto()
    RANDOM = auto()
    FLEE = auto()
    EDIBLE = auto()
    EATEN = auto()

class Ghost:
    def __init__(self, name, behaviour):
        self.name = name
        self.behaviour = behaviour
        self.state = behaviour
        self.edible_timer = 0

    def update_state(self, power_pellet_active):
        if power_pellet_active:
            if self.state != GhostState.EDIBLE and self.state != GhostState.EATEN:
                self.state = GhostState.FLEE
                self.edible_timer = time.time() + 10  # Edible for 10 seconds
        else:
            if self.state == GhostState.FLEE and time.time() > self.edible_timer:
                self.state = self.behaviour

    def visual_identifier(self):
        if self.state == GhostState.FLEE:
            return f"{self.name} is fleeing"
        elif self.state == GhostState.EDIBLE:
            return f"{self.name} is edible"
        elif self.state == GhostState.EATEN:
            return f"{self.name} is eaten"
        else:
            return f"{self.name} is {self.state.name.lower()}"

    def is_edible(self):
        return self.state == GhostState.FLEE

class GhostManager:
    def __init__(self):
        self.ghosts = [
            Ghost("Blinky", GhostState.CHASE),
            Ghost("Pinky", GhostState.AMBUSH),
            Ghost("Inky", GhostState.PATROL),
            Ghost("Clyde", GhostState.RANDOM),
        ]
        self.power_pellet_active = False

    def activate_power_pellet(self):
        self.power_pellet_active = True
        for ghost in self.ghosts:
            ghost.state = GhostState.FLEE
            ghost.edible_timer = time.time() + 10

    def deactivate_power_pellet(self):
        self.power_pellet_active = False

    def update(self):
        for ghost in self.ghosts:
            ghost.update_state(self.power_pellet_active)

    def get_all_states(self):
        return {ghost.name: ghost.state.name.lower() for ghost in self.ghosts}

    def get_ghost_states(self):
        return {ghost.name: ghost.state for ghost in self.ghosts}

    def set_ghost_state(self, name, state):
        for ghost in self.ghosts:
            if ghost.name == name:
                ghost.state = state
                break

    def get_ghost_state(self, name):
        for ghost in self.ghosts:
            if ghost.name == name:
                return ghost.state
        return None

