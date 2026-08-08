from enum import Enum
import time

class GhostState(str, Enum):
    IDLE = "idle"
    CHASE = "chase"
    AMBUSH = "ambush"
    PATROL = "patrol"
    RANDOM = "random"
    FLEE = "flee"
    EATEN = "eaten"

class GhostVisual(str, Enum):
    BLINKY = "red"
    PINKY = "pink"
    INKY = "cyan"
    CLYDE = "orange"
    FRIGHTENED = "blue"
    EATEN = "white"
    UNKNOWN = "unknown"

GHOST_VISUAL_MAP = {
    "Blinky": GhostVisual.BLINKY,
    "Pinky": GhostVisual.PINKY,
    "Inky": GhostVisual.INKY,
    "Clyde": GhostVisual.CLYDE,
}

class Ghost:
    def __init__(self, name):
        self.name = name
        self.initial_state = GhostState.IDLE
        self.state = GhostState.IDLE
        self.edible = False
        self.edible_start_time = None
        self.pre_flee_state = GhostState.IDLE

    def set_state(self, state):
        if isinstance(state, GhostState):
            self.state = state

    def get_state(self):
        return self.state

    def is_edible(self):
        return self.edible

    def make_edible(self):
        if not self.edible:
            self.pre_flee_state = self.state
        self.edible = True
        self.edible_start_time = time.time()
        self.state = GhostState.FLEE

    def make_normal(self):
        self.edible = False
        self.edible_start_time = None
        # Revert to pre-flee state if available, else initial
        self.state = self.pre_flee_state if self.pre_flee_state else self.initial_state

    def update(self):
        if self.edible and self.edible_start_time:
            if time.time() - self.edible_start_time > 10:
                self.make_normal()

    def visual_identifier(self):
        if self.state == GhostState.FLEE or self.edible:
            return GhostVisual.FRIGHTENED.value
        elif self.state == GhostState.EATEN:
            return GhostVisual.EATEN.value
        else:
            return GHOST_VISUAL_MAP.get(self.name, GhostVisual.UNKNOWN).value

class GhostManager:
    def __init__(self):
        self.ghosts = {
            "Blinky": Ghost("Blinky"),
            "Pinky": Ghost("Pinky"),
            "Inky": Ghost("Inky"),
            "Clyde": Ghost("Clyde"),
        }

    def get_ghost_state(self, name):
        ghost = self.ghosts.get(name)
        if ghost:
            return ghost.get_state()
        return None

    def set_ghost_state(self, name, state):
        ghost = self.ghosts.get(name)
        if ghost and isinstance(state, GhostState):
            ghost.set_state(state)

    def get_all_states(self):
        return {name: ghost.get_state() for name, ghost in self.ghosts.items()}

    def activate_power_pellet(self):
        for ghost in self.ghosts.values():
            ghost.make_edible()

    def deactivate_power_pellet(self):
        for ghost in self.ghosts.values():
            if ghost.edible:
                ghost.make_normal()

    def update(self):
        for ghost in self.ghosts.values():
            ghost.update()

    def is_edible(self, name):
        ghost = self.ghosts.get(name)
        if ghost:
            return ghost.is_edible()
        return False

    def get_visual_identifier(self, name):
        ghost = self.ghosts.get(name)
        if ghost:
            return ghost.visual_identifier()
        return GhostVisual.UNKNOWN.value
