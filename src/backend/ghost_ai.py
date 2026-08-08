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
            'Blinky': GhostState.CHASE,
            'Pinky': GhostState.AMBUSH,
            'Inky': GhostState.PATROL,
            'Clyde': GhostState.RANDOM,
        }
        self.state = initial_state_map.get(name, GhostState.IDLE)
        self.original_state = self.state
        visual_map = {
            'Blinky': GhostVisual.BLINKY,
            'Pinky': GhostVisual.PINKY,
            'Inky': GhostVisual.INKY,
            'Clyde': GhostVisual.CLYDE,
        }
        self.visual = visual_map.get(name, None)

    def visual_identifier(self):
        # Return the correct visual identifier based on state
        if self.state == GhostState.FLEE or self.state == GhostState.FRIGHTENED:
            return GhostVisual.FRIGHTENED
        # Eyes logic (not implemented in state machine, but placeholder for extensibility)
        # if self.state == GhostState.EATEN:
        #     return GhostVisual.EYES_UP  # Example, could be direction-based
        return self.visual

    def activate(self):
        self.state = GhostState.CHASE
        self.original_state = self.state

    def sleep(self):
        self.state = GhostState.FRIGHTENED

    def is_active(self) -> bool:
        return self.state == GhostState.CHASE

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

    def get_ghost_state(self, ghost_name):
        ghost = self.ghosts.get(ghost_name)
        if ghost:
            return ghost.state
        return None

    def set_ghost_state(self, ghost_name, state):
        ghost = self.ghosts.get(ghost_name)
        if ghost:
            ghost.state = state
            ghost.original_state = state

    def get_all_states(self):
        return {name: ghost.state for name, ghost in self.ghosts.items()}

    def activate_power_pellet(self):
        self.power_pellet_active = True
        self.power_pellet_end_time = time.time() + 10
        for ghost in self.ghosts.values():
            ghost.original_state = ghost.state
            ghost.state = GhostState.FLEE

    def deactivate_power_pellet(self):
        self.power_pellet_active = False
        # Do not revert immediately; let update() handle revert after timer

    def update(self):
        current_time = time.time()
        if self.power_pellet_active and current_time > self.power_pellet_end_time:
            self.power_pellet_active = False
            for ghost in self.ghosts.values():
                # Revert to original state if stored
                if hasattr(ghost, 'original_state') and ghost.original_state is not None:
                    ghost.state = ghost.original_state
                else:
                    # Fallback: assign initial state based on ghost name
                    initial_state_map = {
                        'Blinky': GhostState.CHASE,
                        'Pinky': GhostState.AMBUSH,
                        'Inky': GhostState.PATROL,
                        'Clyde': GhostState.RANDOM,
                    }
                    ghost.state = initial_state_map.get(ghost.name, GhostState.IDLE)

    def is_edible(self, ghost_name):
        ghost = self.ghosts.get(ghost_name)
        if ghost:
            return ghost.state == GhostState.FLEE or ghost.state == GhostState.FRIGHTENED
        return False
