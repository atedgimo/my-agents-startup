"""
Ghost visual identifiers and state logic for the game.

Defines four ghosts with distinct behaviours:
- chase: chases the player
- ambush: tries to ambush the player
- patrol: patrols a fixed route
- random: moves randomly

Power-pellets make ghosts flee and edible for a limited time.
"""
from enum import Enum, auto
import random
import time

class GhostState(Enum):
    CHASE = auto()
    AMBUSH = auto()
    PATROL = auto()
    RANDOM = auto()
    FLEE = auto()
    EDIBLE = auto()

class Ghost:
    def __init__(self, name, behaviour):
        self.name = name
        self.behaviour = behaviour
        self.state = behaviour
        self.edible_timer = 0

    def update_state(self, power_pellet_active):
        if power_pellet_active:
            if self.state != GhostState.EDIBLE:
                self.state = GhostState.FLEE
                self.edible_timer = time.time() + 10  # edible for 10 seconds
        else:
            if self.state == GhostState.FLEE:
                self.state = GhostState.EDIBLE
            if self.state == GhostState.EDIBLE and time.time() > self.edible_timer:
                self.state = self.behaviour

    def is_edible(self):
        return self.state == GhostState.EDIBLE or self.state == GhostState.FLEE

    def __repr__(self):
        return f"<Ghost {self.name} behaviour={self.behaviour.name} state={self.state.name}>"

class GhostManager:
    def __init__(self):
        self.ghosts = [
            Ghost("Blinky", GhostState.CHASE),
            Ghost("Pinky", GhostState.AMBUSH),
            Ghost("Inky", GhostState.PATROL),
            Ghost("Clyde", GhostState.RANDOM),
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
