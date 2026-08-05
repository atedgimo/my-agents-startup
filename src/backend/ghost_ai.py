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

class GhostIdentity:
    BLINKY = 'Blinky'
    PINKY = 'Pinky'
    INKY = 'Inky'
    CLYDE = 'Clyde'

class Ghost:
    def __init__(self, name):
        self.name = name
        self.state = GhostState.IDLE
        self.original_state = self.state

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
            GhostIdentity.BLINKY: Ghost(GhostIdentity.BLINKY),
            GhostIdentity.PINKY: Ghost(GhostIdentity.PINKY),
            GhostIdentity.INKY: Ghost(GhostIdentity.INKY),
            GhostIdentity.CLYDE: Ghost(GhostIdentity.CLYDE),
        }
        # Initialize ghosts to expected initial states
        self.ghosts[GhostIdentity.BLINKY].state = GhostState.CHASE
        self.ghosts[GhostIdentity.PINKY].state = GhostState.AMBUSH
        self.ghosts[GhostIdentity.INKY].state = GhostState.PATROL
        self.ghosts[GhostIdentity.CLYDE].state = GhostState.RANDOM
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
                # Revert to original state if stored
                if hasattr(ghost, 'original_state') and ghost.original_state:
                    ghost.state = ghost.original_state
                else:
                    ghost.state = GhostState.CHASE

    def is_edible(self, ghost_name):
        ghost = self.ghosts.get(ghost_name)
        if ghost:
            return ghost.state == GhostState.FLEE
        return False
