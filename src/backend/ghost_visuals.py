"""
Ghost visual identifiers and state logic for four ghosts with distinct behaviours:
- chase
- ambush
- patrol
- random

Power-pellets make ghosts flee and edible for a limited time.
"""
from enum import Enum, auto
import time

class GhostState(Enum):
    CHASE = 'chase'
    AMBUSH = 'ambush'
    PATROL = 'patrol'
    RANDOM = 'random'
    FLEE = 'flee'
    EDIBLE = 'edible'
    EATEN = 'eaten'

class Ghost:
    def __init__(self, name, behaviour):
        self.name = name
        self.behaviour = behaviour
        self.state = behaviour
        self.edible_timer = 0

    def update_state(self, power_pellet_active):
        now = time.time()
        if power_pellet_active:
            if self.state not in (GhostState.FLEE, GhostState.EDIBLE):
                self.state = GhostState.FLEE
                self.edible_timer = now + 10  # edible for 10 seconds
        else:
            if self.state == GhostState.FLEE:
                self.state = GhostState.EDIBLE
            if self.state == GhostState.EDIBLE and now > self.edible_timer:
                self.state = self.behaviour

    def is_edible(self):
        return self.state in (GhostState.FLEE, GhostState.EDIBLE)

class GhostManager:
    def __init__(self):
        self.ghosts = [
            Ghost('Blinky', GhostState.CHASE),
            Ghost('Pinky', GhostState.AMBUSH),
            Ghost('Inky', GhostState.PATROL),
            Ghost('Clyde', GhostState.RANDOM),
        ]
        self.power_pellet_active = False

    def activate_power_pellet(self):
        self.power_pellet_active = True
        for ghost in self.ghosts:
            ghost.update_state(True)

    def deactivate_power_pellet(self):
        self.power_pellet_active = False
        for ghost in self.ghosts:
            ghost.update_state(False)

    def update(self):
        for ghost in self.ghosts:
            ghost.update_state(self.power_pellet_active)

    def get_ghosts(self):
        return self.ghosts

    def get_all_states(self):
        return {ghost.name: ghost.state.value for ghost in self.ghosts}

    def get_ghost_state(self, name):
        for ghost in self.ghosts:
            if ghost.name == name:
                return ghost.state
        return None

    def set_ghost_state(self, name, state):
        for ghost in self.ghosts:
            if ghost.name == name:
                ghost.state = state
                return

