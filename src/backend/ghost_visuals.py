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

    def set_state(self, new_state):
        self.state = new_state

    def is_edible(self):
        return self.state == GhostState.FLEE

    def update_state(self, current_time):
        if self.state == GhostState.FLEE and current_time > self.edible_until:
            self.state = self.original_state

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
        return self.ghosts[ghost_name].state

    def set_ghost_state(self, ghost_name, state):
        self.ghosts[ghost_name].set_state(state)

    def get_all_states(self):
        return {name: ghost.state.value for name, ghost in self.ghosts.items()}

    def activate_power_pellet(self, duration=10):
        self.power_pellet_active = True
        current_time = time.time()
        self.power_pellet_end_time = current_time + duration
        for ghost in self.ghosts.values():
            ghost.set_state(GhostState.FLEE)
            ghost.edible_until = self.power_pellet_end_time

    def deactivate_power_pellet(self):
        self.power_pellet_active = False

    def update(self):
        current_time = time.time()
        if self.power_pellet_active and current_time > self.power_pellet_end_time:
            self.deactivate_power_pellet()

        for ghost in self.ghosts.values():
            ghost.update_state(current_time)

        if not self.power_pellet_active:
            for ghost in self.ghosts.values():
                ghost.set_state(ghost.original_state)

