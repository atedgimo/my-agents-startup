from enum import Enum
import time

class GhostState(Enum):
    NORMAL = "normal"
    PATROL = "patrol"
    AMBUSH = "ambush"
    FRIGHTENED = "frightened"
    EATEN = "eaten"
    # Add any additional states used in code/tests if needed

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

class Ghost:
    """
    Represents a single ghost and its state logic.
    """
    def __init__(self, name, initial_state=GhostState.NORMAL):
        self.name = name
        self.state = initial_state
        self._original_state = initial_state
        self._frightened_until = 0

    def set_state(self, state: GhostState):
        self.state = state

    def get_state(self) -> GhostState:
        return self.state

    def frighten(self, duration: float):
        self._original_state = self.state
        self.state = GhostState.FRIGHTENED
        self._frightened_until = time.time() + duration

    def eat(self):
        self.state = GhostState.EATEN

    def update_state(self, current_time=None):
        """
        Called periodically to update the ghost's state, e.g. after frightened expires.
        """
        if self.state == GhostState.FRIGHTENED:
            now = current_time if current_time is not None else time.time()
            if now > self._frightened_until:
                self.state = self._original_state

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
        return self.state == GhostState.FRIGHTENED

    def __repr__(self):
        return f"<Ghost name={self.name} state={self.state.value}>"

class GhostManager:
    """
    Manages all ghosts and their state transitions, including frightened and eaten logic.
    """
    FRIGHTENED_DURATION = 10

    def __init__(self):
        self.ghosts = {
            GhostVisual.BLINKY.value: Ghost("Blinky", GhostState.NORMAL),
            GhostVisual.PINKY.value: Ghost("Pinky", GhostState.NORMAL),
            GhostVisual.INKY.value: Ghost("Inky", GhostState.NORMAL),
            GhostVisual.CLYDE.value: Ghost("Clyde", GhostState.NORMAL),
        }

    def get_ghost_state(self, ghost_name):
        ghost = self.ghosts.get(ghost_name)
        return ghost.get_state() if ghost else None

    def set_ghost_state(self, ghost_name, state):
        ghost = self.ghosts.get(ghost_name)
        if ghost:
            ghost.set_state(state)

    def frighten_all(self, duration=None):
        """
        Sets all ghosts to FRIGHTENED state for the given duration.
        """
        duration = duration if duration is not None else self.FRIGHTENED_DURATION
        for ghost in self.ghosts.values():
            ghost.frighten(duration)

    def eat_ghost(self, ghost_name):
        ghost = self.ghosts.get(ghost_name)
        if ghost:
            ghost.eat()

    def update(self):
        """
        Should be called periodically to update ghost states and handle frightened expiration.
        """
        now = time.time()
        for ghost in self.ghosts.values():
            ghost.update_state(current_time=now)

    def get_all_states(self):
        return {name: ghost.get_state() for name, ghost in self.ghosts.items()}

    def get_visual_identifiers(self):
        """
        Returns a dict of ghost name to their visual identifier (for rendering).
        """
        return {name: ghost.visual_identifier() for name, ghost in self.ghosts.items()}

    def is_edible(self, ghost_name):
        ghost = self.ghosts.get(ghost_name)
        return ghost.is_edible() if ghost else False
