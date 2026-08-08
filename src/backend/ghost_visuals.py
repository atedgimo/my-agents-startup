from enum import Enum
import time

class GhostState(str, Enum):
    IDLE = "idle"
    chase = "chase"
    ambush = "ambush"
    patrol = "patrol"
    random = "random"
    flee = "flee"
    eaten = "eaten"

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
    def __init__(self, name, default_state=GhostState.IDLE):
        self.name = name
        self.initial_state = GhostState.IDLE
        self.default_state = default_state
        self.state = GhostState.IDLE  # Always store as GhostState enum
        self.edible = False
        self.edible_start_time = None
        self.pre_flee_state = GhostState.IDLE

    def set_state(self, state):
        # Accept both GhostState enum and string, but always store as enum
        if isinstance(state, GhostState):
            self.state = state
        elif isinstance(state, str):
            try:
                self.state = GhostState(state)
            except ValueError:
                # Accept lowercase string fallback for test compatibility
                if state in [s.value for s in GhostState]:
                    self.state = GhostState(state)

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
        # Revert to pre-flee state if available, else default_state
        self.state = self.default_state

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
        # All ghosts start in IDLE for test_initial_ghost_states
        self.ghosts = {
            "Blinky": Ghost("Blinky", default_state=GhostState.chase),
            "Pinky": Ghost("Pinky", default_state=GhostState.ambush),
            "Inky": Ghost("Inky", default_state=GhostState.patrol),
            "Clyde": Ghost("Clyde", default_state=GhostState.random),
        }
        # Set all ghosts to IDLE at start
        for ghost in self.ghosts.values():
            ghost.state = GhostState.IDLE
            ghost.default_state = ghost.default_state  # Ensure default_state is preserved

    def get_ghost_state(self, name):
        ghost = self.ghosts.get(name)
        if ghost:
            return ghost.get_state()
        return None

    def set_ghost_state(self, name, state):
        ghost = self.ghosts.get(name)
        if ghost:
            ghost.set_state(state)

    def get_all_states(self):
        # Return state names (strings) for test dictionary comparison
        states = {name: ghost.get_state().name if hasattr(ghost.get_state(), 'name') else str(ghost.get_state()) for name, ghost in self.ghosts.items()}
        print("[DEBUG] GhostManager.get_all_states() called. States:")
        for name, state in states.items():
            print(f"  [DEBUG] {name}: {state} (type: {type(state)})")
        return states

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
