"""
Module for ghost visual identifiers and state logic.

Four ghosts with distinct behaviours:
- chase
- ambush
- patrol
- random

Power-pellets make ghosts flee and edible for a limited time.
"""
import random
import time

class GhostState:
    CHASE = 'chase'
    AMBUSH = 'ambush'
    PATROL = 'patrol'
    RANDOM = 'random'
    FLEE = 'flee'
    EDIBLE = 'edible'

class Ghost:
    def __init__(self, name, behaviour):
        self.name = name
        self.behaviour = behaviour
        self.state = behaviour
        self.edible_until = 0

    def update_state(self, power_pellet_active):
        now = time.time()
        if power_pellet_active:
            if self.state != GhostState.FLEE and self.state != GhostState.EDIBLE:
                self.state = GhostState.FLEE
                self.edible_until = now + 10  # Edible for 10 seconds
        if self.state == GhostState.FLEE and now > self.edible_until:
            self.state = self.behaviour

    def is_edible(self):
        return self.state == GhostState.FLEE

    def __repr__(self):
        return f"<Ghost {self.name} state={self.state}>"

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

    def get_ghost_states(self):
        return {ghost.name: ghost.state for ghost in self.ghosts}


