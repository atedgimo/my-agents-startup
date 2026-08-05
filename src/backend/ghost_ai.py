import time
from enum import Enum

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

class Ghost:
    def __init__(self, name, initial_state=GhostState.IDLE):
        self.name = name
        self.state = initial_state
        self.original_state = initial_state

    def activate(self):
        self.state = GhostState.CHASE
        self.original_state = self.state

    def sleep(self):
        self.state = GhostState.FRIGHTENED

    def is_active(self) -> bool:
        return self.state == GhostState.CHASE

    def __repr__(self):
        return f"<Ghost name={self.name} state={self.state.name}>"

class GhostManager:
    def __init__(self):
        self.ghosts = {
            GhostIdentity.BLINKY: Ghost(GhostIdentity.BLINKY, GhostState.CHASE),
            GhostIdentity.PINKY: Ghost(GhostIdentity.PINKY, GhostState.AMBUSH),
            GhostIdentity.INKY: Ghost(GhostIdentity.INKY, GhostState.PATROL),
            GhostIdentity.CLYDE: Ghost(GhostIdentity.CLYDE, GhostState.RANDOM),
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

    def update(self):
        current_time = time.time()
        if self.power_pellet_active and current_time > self.power_pellet_end_time:
            self.power_pellet_active = False
            for ghost in self.ghosts.values():
                if hasattr(ghost, 'original_state') and ghost.original_state:
                    ghost.state = ghost.original_state
                else:
                    ghost.state = GhostState.CHASE

    def is_edible(self, ghost_name):
        ghost = self.ghosts.get(ghost_name)
        if ghost:
            return ghost.state == GhostState.FLEE
        return False
