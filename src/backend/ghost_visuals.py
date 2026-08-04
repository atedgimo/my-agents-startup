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
                self.edible_timer = time.time() + 10  # Edible for 10 seconds
        else:
            if self.state == GhostState.FLEE and time.time() > self.edible_timer:
                self.state = self.behaviour

    def visual_identifier(self):
        if self.state == GhostState.FLEE:
            return f"{self.name} is fleeing"
        elif self.state == GhostState.EDIBLE:
            return f"{self.name} is edible"
        else:
            return f"{self.name} is {self.state.name.lower()}"

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
            ghost.state = GhostState.FLEE
            ghost.edible_timer = time.time() + 10

    def deactivate_power_pellet(self):
        self.power_pellet_active = False
        for ghost in self.ghosts:
            ghost.state = ghost.behaviour

    def update_ghosts(self):
        for ghost in self.ghosts:
            ghost.update_state(self.power_pellet_active)

    def get_visuals(self):
        return {ghost.name: ghost.visual_identifier() for ghost in self.ghosts}
