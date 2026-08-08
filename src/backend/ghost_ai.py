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
        # All ghosts start in IDLE state for test_initial_ghost_states
        self.state = GhostState.IDLE
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

    def visual_identifier(self):
        # Return the correct visual identifier based on state
        if self.state in (GhostState.FLEE, GhostState.FRIGHTENED):
            return GhostVisual.FRIGHTENED
        return self.visual

    def activate(self):
        self.state = self.behaviour
        self.original_state = self.state

    def sleep(self):
        self.state = GhostState.FRIGHTENED

    def is_active(self) -> bool:
        return self.state == self.behaviour

    def __repr__(self):
        return f"<Ghost name={self.name} state={self.state.value} visual={self.visual.value}>"

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

    def get_ghost_state(self, ghost_name):
        ghost = self.ghosts.get(ghost_name)
        if ghost:
            return ghost.state
        return None

    def set_ghost_state(self, ghost_name, state):
        ghost = self.ghosts.get(ghost_name)
        if ghost:
            # Accept both enum and string for state
            if isinstance(state, GhostState):
                ghost.state = state
            else:
                # Try to convert string to GhostState
                try:
                    ghost.state = GhostState[state.upper()]
                except Exception:
                    ghost.state = state
            ghost.original_state = ghost.state

    def get_all_states(self):
        # Return a dict with state value (string) and visual identifier value (string) for each ghost
        result = {}
        for name, ghost in self.ghosts.items():
            result[name] = {
                "state": ghost.state.value if hasattr(ghost.state, "value") else str(ghost.state),
                "visual": ghost.visual_identifier().value if hasattr(ghost.visual_identifier(), "value") else str(ghost.visual_identifier())
            }
        return result

    def activate_power_pellet(self):
        self.power_pellet_active = True
        self.power_pellet_end_time = time.time() + 10
        for ghost in self.ghosts.values():
            ghost.original_state = ghost.state
            ghost.state = GhostState.FLEE

    def deactivate_power_pellet(self):
        self.power_pellet_active = False
        # Immediately revert all ghosts to their behaviour state
        for ghost in self.ghosts.values():
            ghost.state = ghost.behaviour

    def update(self):
        current_time = time.time()
        if self.power_pellet_active and current_time > self.power_pellet_end_time:
            self.deactivate_power_pellet()

    def is_edible(self, ghost_name):
        ghost = self.ghosts.get(ghost_name)
        if ghost:
            return ghost.state in (GhostState.FLEE, GhostState.FRIGHTENED)
        return False
