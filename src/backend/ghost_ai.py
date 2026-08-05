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

class Ghost:
    def __init__(self, name, initial_state):
        self.name = name
        self.state = initial_state
        self.original_state = initial_state
        self.edible_until = 0

    def update_state(self, player_powered_up=False):
        current_time = time.time()
        if player_powered_up:
            self.state = GhostState.FLEE
            self.edible_until = current_time + 10  # edible for 10 seconds
        elif self.state == GhostState.FLEE and current_time > self.edible_until:
            self.state = self.original_state

    def is_edible(self):
        return self.state == GhostState.FLEE

    def visual_identifier(self):
        return self.state.value

    def __repr__(self):
        return f"<Ghost name={self.name} state={self.state.value}>"

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
        return {name: ghost.state.value for name, ghost in self.ghosts.items()}

    def activate_power_pellet(self):
        self.power_pellet_active = True
        self.power_pellet_end_time = time.time() + 10
        for ghost in self.ghosts.values():
            ghost.state = GhostState.FLEE

    def deactivate_power_pellet(self):
        self.power_pellet_active = False

    def update(self):
        current_time = time.time()
        if self.power_pellet_active and current_time > self.power_pellet_end_time:
            self.power_pellet_active = False
            for ghost in self.ghosts.values():
                ghost.state = ghost.original_state

