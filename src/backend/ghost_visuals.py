from enum import Enum
import time

class GhostState(Enum):
    CHASE = 'chase'
    AMBUSH = 'ambush'
    PATROL = 'patrol'
    RANDOM = 'random'
    FLEE = 'flee'
    EATEN = 'eaten'

class Ghost:
    def __init__(self, name, initial_state):
        self.name = name
        self.state = initial_state
        self.edible_until = 0

    def visual_identifier(self):
        return self.state.value

    def is_edible(self):
        return self.state == GhostState.FLEE and time.time() < self.edible_until

class GhostManager:
    def __init__(self):
        self.ghosts = {
            'Blinky': Ghost('Blinky', GhostState.CHASE),
            'Pinky': Ghost('Pinky', GhostState.AMBUSH),
            'Inky': Ghost('Inky', GhostState.PATROL),
            'Clyde': Ghost('Clyde', GhostState.RANDOM)
        }

    def get_all_states(self):
        return {name: ghost.visual_identifier() for name, ghost in self.ghosts.items()}

    def get_ghost_state(self, identity):
        return self.ghosts[identity].state

    def set_ghost_state(self, identity, state):
        self.ghosts[identity].state = state

    def activate_power_pellet(self):
        now = time.time()
        for ghost in self.ghosts.values():
            ghost.state = GhostState.FLEE
            ghost.edible_until = now + 10

    def deactivate_power_pellet(self):
        # No immediate change, update() will revert states
        pass

    def update(self):
        now = time.time()
        for ghost in self.ghosts.values():
            if ghost.state == GhostState.FLEE and now > ghost.edible_until:
                # revert to original state
                if ghost.name == 'Blinky':
                    ghost.state = GhostState.CHASE
                elif ghost.name == 'Pinky':
                    ghost.state = GhostState.AMBUSH
                elif ghost.name == 'Inky':
                    ghost.state = GhostState.PATROL
                elif ghost.name == 'Clyde':
                    ghost.state = GhostState.RANDOM
