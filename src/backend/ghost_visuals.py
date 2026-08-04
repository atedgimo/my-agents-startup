from enum import Enum
from datetime import datetime, timedelta

class GhostState(Enum):
    CHASE = "chase"
    AMBUSH = "ambush"
    PATROL = "patrol"
    RANDOM = "random"
    FLEE = "flee"
    EDIBLE = "edible"

class Ghost:
    def __init__(self, id, state: GhostState):
        self.id = id
        self.state = state
        self.edible_until = None

    def set_state(self, state: GhostState):
        self.state = state

    def get_state(self):
        if self.edible_until and datetime.now() < self.edible_until:
            return GhostState.EDIBLE
        return self.state

    def make_edible(self, duration_seconds: int):
        self.edible_until = datetime.now() + timedelta(seconds=duration_seconds)

    def is_edible(self):
        return self.get_state() == GhostState.EDIBLE

class GhostManager:
    def __init__(self):
        self.ghosts = [
            Ghost(1, GhostState.CHASE),
            Ghost(2, GhostState.AMBUSH),
            Ghost(3, GhostState.PATROL),
            Ghost(4, GhostState.RANDOM),
        ]
        self.power_pellet_active = False
        self.power_pellet_end_time = None

    def activate_power_pellet(self, duration_seconds: int):
        self.power_pellet_active = True
        self.power_pellet_end_time = datetime.now() + timedelta(seconds=duration_seconds)
        for ghost in self.ghosts:
            ghost.make_edible(duration_seconds)

    def update(self):
        if self.power_pellet_active and datetime.now() > self.power_pellet_end_time:
            self.power_pellet_active = False
            for ghost in self.ghosts:
                ghost.edible_until = None

    def get_ghost_states(self):
        self.update()
        return {ghost.id: ghost.get_state().value for ghost in self.ghosts}
