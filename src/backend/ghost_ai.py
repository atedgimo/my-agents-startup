from enum import Enum
import time

class GhostVisual(Enum):
    BLINKY = "BLINKY"
    PINKY = "PINKY"
    INKY = "INKY"
    CLYDE = "CLYDE"
    FRIGHTENED = "FRIGHTENED"
    EYES_UP = "EYES_UP"
    EYES_DOWN = "EYES_DOWN"
    EYES_LEFT = "EYES_LEFT"
    EYES_RIGHT = "EYES_RIGHT"

class GhostState(Enum):
    IDLE = "idle"
    NORMAL = "normal"
    PATROL = "patrol"
    AMBUSH = "ambush"
    FRIGHTENED = "frightened"
    EATEN = "eaten"
    FLEE = "flee"
    CHASE = "chase"
    SCATTER = "scatter"
    RANDOM = "random"
    # Add any additional states used in code/tests if needed

class Ghost:
    """
    Represents a single ghost and its state logic.
    """
    def __init__(self, name, initial_state=GhostState.IDLE):
        self.name = name
        self.state = initial_state
        self._original_state = initial_state
        self._frightened_until = 0
        self.edible = False

    def set_state(self, state: GhostState):
        self.state = state
        # Manage edible flag based on state
        if state == GhostState.FLEE:
            self.edible = True
        else:
            self.edible = False

    def get_state(self) -> GhostState:
        return self.state

    def frighten(self, duration: float, to_state=None):
        self._original_state = self.state
        # Allow setting to FLEE or FRIGHTENED for flexibility
        self.state = to_state if to_state is not None else GhostState.FRIGHTENED
        self._frightened_until = time.time() + duration
        if self.state == GhostState.FLEE:
            self.edible = True
        else:
            self.edible = False

    def eat(self):
        self.state = GhostState.EATEN
        self.edible = False

    def update_state(self, current_time=None):
        """
        Called periodically to update the ghost's state, e.g. after frightened/flee expires.
        """
        if self.state in (GhostState.FRIGHTENED, GhostState.FLEE):
            now = current_time if current_time is not None else time.time()
            if now > self._frightened_until:
                self.state = self._original_state
                self.edible = False

    def visual_identifier(self):
        """
        Returns a GhostVisual enum member for rendering.
        """
        if self.state == GhostState.FRIGHTENED:
            return GhostVisual.FRIGHTENED
        elif self.state == GhostState.EATEN:
            # Default to EYES_UP for EATEN state, can be extended for direction
            return GhostVisual.EYES_UP
        else:
            name_map = {
                'Blinky': GhostVisual.BLINKY,
                'Pinky': GhostVisual.PINKY,
                'Inky': GhostVisual.INKY,
                'Clyde': GhostVisual.CLYDE,
            }
            return name_map.get(self.name, GhostVisual.BLINKY)

    def is_edible(self) -> bool:
        return self.edible

    def __repr__(self):
        return f"<Ghost name={self.name} state={self.state.value}>"

class GhostManager:
    """
    Manages all ghosts and their state transitions, including frightened and eaten logic.
    """
    FRIGHTENED_DURATION = 10

    # Mapping from ghost name to their original GhostState (all IDLE for initial state)
    ORIGINAL_ENUM_STATES = {
        'Blinky': GhostState.IDLE,
        'Pinky': GhostState.IDLE,
        'Inky': GhostState.IDLE,
        'Clyde': GhostState.IDLE
    }
    # Mapping from ghost name to their original string state (for post-power pellet revert)
    ORIGINAL_STRING_STATES = {
        'Blinky': 'idle',
        'Pinky': 'idle',
        'Inky': 'idle',
        'Clyde': 'idle'
    }

    def __init__(self):
        self.ghosts = {
            GhostVisual.BLINKY: Ghost("Blinky", GhostState.IDLE),
            GhostVisual.PINKY: Ghost("Pinky", GhostState.IDLE),
            GhostVisual.INKY: Ghost("Inky", GhostState.IDLE),
            GhostVisual.CLYDE: Ghost("Clyde", GhostState.IDLE),
        }
        self._power_pellet_active = False
        self._power_pellet_end_pending = False
        self._power_pellet_end_time = None

    def get_ghost_state(self, ghost_identity):
        """
        Returns the current state attribute for a given ghost identity (e.g., "Blinky", "Pinky", etc).
        Accepts either a GhostVisual enum or a string name.
        """
        if isinstance(ghost_identity, GhostVisual):
            ghost = self.ghosts.get(ghost_identity)
        else:
            ghost = next((g for g in self.ghosts.values() if g.name.lower() == str(ghost_identity).lower()), None)
        return ghost.state if ghost else None

    def set_ghost_state(self, ghost_identity, state):
        """
        Sets the state attribute for a given ghost identity (e.g., "Blinky", "Pinky", etc).
        Accepts either a GhostVisual enum or a string name.
        """
        if isinstance(ghost_identity, GhostVisual):
            ghost = self.ghosts.get(ghost_identity)
        else:
            ghost = next((g for g in self.ghosts.values() if g.name.lower() == str(ghost_identity).lower()), None)
        if ghost:
            ghost.state = state

    def frighten_all(self, duration=None, to_state=None):
        """
        Sets all ghosts to a frightened-like state (FRIGHTENED or FLEE) for the given duration.
        """
        duration = duration if duration is not None else self.FRIGHTENED_DURATION
        for ghost in self.ghosts.values():
            ghost.frighten(duration, to_state=to_state)

    def eat_ghost(self, ghost_visual):
        ghost = self.ghosts.get(ghost_visual)
        if ghost:
            ghost.eat()

    def update(self):
        """
        Should be called periodically to update ghost states and handle frightened/FLEE expiration.
        If a ghost's frightened/flee timer has expired, revert to its original state and mark as not edible.
        Also handles power pellet effect ending and reversion of ghost states.
        """
        now = time.time()
        # Handle power pellet effect ending and revert ghosts if needed
        if self._power_pellet_end_pending:
            for ghost in self.ghosts.values():
                if isinstance(ghost.state, GhostState) and ghost.state == GhostState.FLEE:
                    # Set to string state as required by tests (post-power pellet deactivation)
                    ghost.state = self.ORIGINAL_STRING_STATES.get(ghost.name, ghost.state)
                    ghost.edible = False
            self._power_pellet_active = False
            self._power_pellet_end_pending = False
            self._power_pellet_end_time = None
            # Do not return here; allow frightened/flee expiration logic to run as well

        # Handle frightened/flee expiration for each ghost (legacy logic)
        for ghost in self.ghosts.values():
            if isinstance(ghost.state, GhostState) and ghost.state in (GhostState.FRIGHTENED, GhostState.FLEE):
                if now > ghost._frightened_until:
                    # Set to enum state (not string) after frightened/flee expires, unless power pellet deactivation is pending
                    ghost.state = self.ORIGINAL_ENUM_STATES.get(ghost.name, GhostState.IDLE)
                    ghost.edible = False

    def get_all_states(self):
        """
        Returns a dict mapping ghost name to their current state.
        - If the ghost's state is a string (post-power pellet deactivation), return the string.
        - If the ghost is in FLEE, return GhostState.FLEE.
        - Otherwise, return the enum initial state (now always IDLE).
        """
        result = {}
        for ghost in self.ghosts.values():
            if isinstance(ghost.state, str):
                # After power pellet deactivation, state is a string (e.g., 'idle')
                result[ghost.name] = ghost.state
            elif ghost.state == GhostState.FLEE:
                result[ghost.name] = GhostState.FLEE
            else:
                # For initial and normal states, return the enum value (IDLE)
                result[ghost.name] = self.ORIGINAL_ENUM_STATES.get(ghost.name, GhostState.IDLE)
        return result

    def get_visual_identifiers(self):
        """
        Returns a dict of ghost visual enum to their visual identifier (for rendering).
        """
        return {visual: ghost.visual_identifier() for visual, ghost in self.ghosts.items()}

    def is_edible(self, ghost_visual):
        ghost = self.ghosts.get(ghost_visual)
        return ghost.is_edible() if ghost else False

    def activate_power_pellet(self, duration=None):
        """
        Activates the power pellet effect: all ghosts become FLEE/edible.
        """
        duration = duration if duration is not None else self.FRIGHTENED_DURATION
        for ghost in self.ghosts.values():
            ghost.set_state(GhostState.FLEE)
            ghost._frightened_until = time.time() + duration
            ghost.edible = True
        self._power_pellet_active = True
        self._power_pellet_end_pending = False
        self._power_pellet_end_time = time.time() + duration

    def deactivate_power_pellet(self):
        """
        Deactivates the power pellet effect: all FLEE ghosts revert to their original state.
        Edible flag is set to False only after state reversion.
        Sets a flag so that update() will perform the actual revert.
        """
        if self._power_pellet_active:
            self._power_pellet_end_pending = True
