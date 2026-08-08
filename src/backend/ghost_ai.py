from enum import Enum
import time

class GhostState(Enum):
    IDLE = 'idle'
    CHASE = 'chase'
    FRIGHTENED = 'frightened'
    FLEE = 'flee'
    EATEN = 'eaten'
    AMBUSH = 'ambush'
    PATROL = 'patrol'
    RANDOM = 'random'

class GhostVisual(Enum):
    BLINKY = 'blinky'
    PINKY = 'pinky'
    INKY = 'inky'
    CLYDE = 'clyde'
    FRIGHTENED = 'frightened'
    EYES_UP = 'eyes_up'
    EYES_DOWN = 'eyes_down'
    EYES_LEFT = 'eyes_left'
    EYES_RIGHT = 'eyes_right'

class GhostIdentity:
    BLINKY = 'Blinky'
    PINKY = 'Pinky'
    INKY = 'Inky'
    CLYDE = 'Clyde'

class Ghost:
    def __init__(self, name):
        self.name = name
        # Set initial state based on ghost name
        initial_state_map = {
            'Blinky': GhostState.IDLE,
            'Pinky': GhostState.IDLE,
            'Inky': GhostState.IDLE,
            'Clyde': GhostState.IDLE,
        }
        self.state = initial_state_map.get(name, GhostState.IDLE)
        self.behaviour_map = {
            'Blinky': GhostState.CHASE,
            'Pinky': GhostState.AMBUSH,
            'Inky': GhostState.PATROL,
            'Clyde': GhostState.RANDOM,
        }
        self.behaviour = self.behaviour_map.get(name, GhostState.CHASE)
        self.visual_map = {
            'Blinky': GhostVisual.BLINKY,
            'Pinky': GhostVisual.PINKY,
            'Inky': GhostVisual.INKY,
            'Clyde': GhostVisual.CLYDE,
        }
        self.visual = self.visual_map.get(name, None)
        self.original_state = self.state
        self._debug("Initialized")

    def visual_identifier(self):
        # Return the correct visual identifier based on state
        if self.state in (GhostState.FLEE, GhostState.FRIGHTENED):
            return GhostVisual.FRIGHTENED
        # Eyes logic (not implemented in state machine, but placeholder for extensibility)
        # if self.state == GhostState.EATEN:
        #     return GhostVisual.EYES_UP  # Example, could be direction-based
        return self.visual

    def activate(self):
        self.state = self.behaviour
        self.original_state = self.state
        self._debug("Activated")

    def sleep(self):
        self.state = GhostState.FRIGHTENED
        self._debug("Slept (frightened)")

    def is_active(self) -> bool:
        return self.state == self.behaviour

    def _debug(self, msg):
        print(f"[DEBUG] Ghost {self.name}: {msg} | state={self.state} behaviour={self.behaviour}")

    def __repr__(self):
        return f"<Ghost name={self.name} state={self.state.name} visual={self.visual.value}>"

class GhostManager:
    def __init__(self):
        self.ghosts = {
            GhostIdentity.BLINKY: Ghost(GhostIdentity.BLINKY),
            GhostIdentity.PINKY: Ghost(GhostIdentity.PINKY),
            GhostIdentity.INKY: Ghost(GhostIdentity.INKY),
            GhostIdentity.CLYDE: Ghost(GhostIdentity.CLYDE),
        }
        self.power_pellet_active = False
        self.power_pellet_end_time = 0
        self._debug("Initialized GhostManager")

    def get_ghost_state(self, ghost_name):
        ghost = self.ghosts.get(ghost_name)
        if ghost:
            self._debug(f"get_ghost_state({ghost_name}) = {ghost.state}")
            return ghost.state
        return None

    def set_ghost_state(self, ghost_name, state):
        ghost = self.ghosts.get(ghost_name)
        if ghost:
            ghost.state = state
            ghost.original_state = state
            self._debug(f"set_ghost_state({ghost_name}, {state})")

    def get_all_states(self):
        # Return a dict with state name and visual identifier for each ghost
        result = {}
        for name, ghost in self.ghosts.items():
            result[name] = {
                "state": ghost.state.name if hasattr(ghost.state, "name") else str(ghost.state),
                "visual": ghost.visual_identifier().name if hasattr(ghost.visual_identifier(), "name") else str(ghost.visual_identifier())
            }
            self._debug(f"get_all_states: {name} -> {result[name]}")
        return result

    def activate_power_pellet(self):
        self.power_pellet_active = True
        self.power_pellet_end_time = time.time() + 10
        for ghost in self.ghosts.values():
            ghost.original_state = ghost.state
            ghost.state = GhostState.FLEE
            ghost._debug("Power pellet activated (FLEE)")

    def deactivate_power_pellet(self):
        self.power_pellet_active = False
        self._debug("Power pellet deactivated")
        # Do not revert immediately; let update() handle revert after timer

    def update(self):
        current_time = time.time()
        if self.power_pellet_active and current_time > self.power_pellet_end_time:
            self.power_pellet_active = False
            for ghost in self.ghosts.values():
                # Revert to behaviour state
                ghost.state = ghost.behaviour
                ghost._debug("Power pellet expired, reverting to behaviour")

    def is_edible(self, ghost_name):
        ghost = self.ghosts.get(ghost_name)
        if ghost:
            edible = ghost.state in (GhostState.FLEE, GhostState.FRIGHTENED)
            self._debug(f"is_edible({ghost_name}) = {edible}")
            return edible
        return False

    def _debug(self, msg):
        print(f"[DEBUG] GhostManager: {msg}")
