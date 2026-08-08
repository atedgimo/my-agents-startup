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
    IDLE = 'idle'
    CHASE = 'chase'
    FRIGHTENED = 'frightened'
    FLEE = 'flee'
    EATEN = 'eaten'
    AMBUSH = 'ambush'
    PATROL = 'patrol'
    RANDOM = 'random'

class GhostIdentity:
    BLINKY = 'Blinky'
    PINKY = 'Pinky'
    INKY = 'Inky'
    CLYDE = 'Clyde'

class Ghost:
    """
    Represents a single ghost and its state logic.
    """
    def __init__(self, name, initial_state=GhostState.IDLE):
        self.name = name
        self.state = initial_state
        self._original_state = initial_state
        self._edible_until = 0

    def set_state(self, state: GhostState):
        self.state = state

    def get_state(self) -> GhostState:
        return self.state

    def update_for_power_pellet(self, duration: float):
        self._original_state = self.state
        self.state = GhostState.FLEE
        self._edible_until = time.time() + duration

    def update_state(self, current_time=None):
        """
        Called periodically to update the ghost's state, e.g. after power pellet expires.
        """
        if self.state == GhostState.FLEE:
            now = current_time if current_time is not None else time.time()
            if now > self._edible_until:
                self.state = self._original_state

    def visual_identifier(self):
        """
        Returns a GhostVisual enum member for rendering.
        """
        if self.state == GhostState.FLEE:
            return GhostVisual.FRIGHTENED
        elif self.state == GhostState.EATEN:
            # For simplicity, default to EYES_UP when eaten; could be directional
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
        return self.state == GhostState.FLEE

    def __repr__(self):
        return f"<Ghost name={self.name} state={self.state.value}>"

class GhostManager:
    """
    Manages all ghosts and their state transitions, including power pellet logic.
    """
    POWER_PELLET_DURATION = 10

    def __init__(self):
        self.ghosts = {
            GhostIdentity.BLINKY: Ghost(GhostIdentity.BLINKY, GhostState.CHASE),
            GhostIdentity.PINKY: Ghost(GhostIdentity.PINKY, GhostState.AMBUSH),
            GhostIdentity.INKY: Ghost(GhostIdentity.INKY, GhostState.PATROL),
            GhostIdentity.CLYDE: Ghost(GhostIdentity.CLYDE, GhostState.RANDOM),
        }
        self._power_pellet_active = False
        self._power_pellet_end_time = 0

    def get_ghost_state(self, ghost_name):
        ghost = self.ghosts.get(ghost_name)
        return ghost.get_state() if ghost else None

    def set_ghost_state(self, ghost_name, state):
        ghost = self.ghosts.get(ghost_name)
        if ghost:
            ghost.set_state(state)

    def get_all_states(self):
        return {name: ghost.get_state() for name, ghost in self.ghosts.items()}

    def activate_power_pellet(self, duration=None):
        """
        Activates power pellet mode for all ghosts.
        """
        duration = duration if duration is not None else self.POWER_PELLET_DURATION
        self._power_pellet_active = True
        self._power_pellet_end_time = time.time() + duration
        for ghost in self.ghosts.values():
            ghost.update_for_power_pellet(duration)

    def deactivate_power_pellet(self):
        """
        Deactivates power pellet mode (ghosts revert to original states).
        """
        self._power_pellet_active = False
        # Force all ghosts out of FLEE state, back to their original state
        for ghost in self.ghosts.values():
            if ghost.state == GhostState.FLEE:
                ghost.state = ghost._original_state
            # Also clear edible timer
            ghost._edible_until = 0

    def update(self):
        """
        Should be called periodically to update ghost states and handle power pellet expiration.
        """
        now = time.time()
        if self._power_pellet_active and now > self._power_pellet_end_time:
            self.deactivate_power_pellet()
        elif self._power_pellet_active:
            for ghost in self.ghosts.values():
                ghost.update_state(current_time=now)

    def is_edible(self, ghost_name):
        ghost = self.ghosts.get(ghost_name)
        return ghost.is_edible() if ghost else False

    def get_visual_identifiers(self):
        """
        Returns a dict of ghost name to their visual identifier (for rendering).
        """
        return {name: ghost.visual_identifier() for name, ghost in self.ghosts.items()}
