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
        self.position = (0, 0)  # Default start position
        self.edible_timer = 0

    def update_state(self, power_pellet_active):
        if power_pellet_active:
            if self.state != GhostState.FLEE and self.state != GhostState.EDIBLE:
                self.state = GhostState.FLEE
                self.edible_timer = time.time() + 10  # Edible for 10 seconds
        else:
            if self.state == GhostState.FLEE or self.state == GhostState.EDIBLE:
                if time.time() > self.edible_timer:
                    self.state = self.behaviour

    def visual_identifier(self):
        # Return a string representing the ghost's visual state
        if self.state == GhostState.FLEE:
            return f"{self.name} (Fleeing)"
        elif self.state == GhostState.EDIBLE:
            return f"{self.name} (Edible)"
        else:
            return f"{self.name} ({self.state.name})"

    def move(self):
        # Simplified move logic based on behaviour
        if self.state == GhostState.CHASE:
            return "Chasing"
        elif self.state == GhostState.AMBUSH:
            return "Ambushing"
        elif self.state == GhostState.PATROL:
            return "Patrolling"
        elif self.state == GhostState.RANDOM:
            return random.choice(["Up", "Down", "Left", "Right"])
        elif self.state == GhostState.FLEE:
            return "Fleeing"
        elif self.state == GhostState.EDIBLE:
            return "Edible"

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

    def get_ghost_states(self):
        return {ghost.name: ghost.state.name for ghost in self.ghosts}

    def get_ghost_visuals(self):
        return {ghost.name: ghost.visual_identifier() for ghost in self.ghosts}
