from enum import Enum
import time

class GhostState(str, Enum):
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

    def is_edible(self):
        return time.time() < self.edible_until

    def set_state(self, state):
        self.state = state
        if state == GhostState.FLEE:
            self.edible_until = time.time() + 10  # edible for 10 seconds
        else:
            self.edible_until = 0

class GhostManager:
    def __init__(self):
        self.ghosts = {
            'Blinky': Ghost('Blinky', GhostState.CHASE),
            'Pinky': Ghost('Pinky', GhostState.AMBUSH),
            'Inky': Ghost('Inky', GhostState.PATROL),
            'Clyde': Ghost('Clyde', GhostState.RANDOM),
        }
        self.power_pellet_active = False

    def get_ghost_state(self, name):
        return self.ghosts[name].state

    def get_all_states(self):
        return {name: ghost.state for name, ghost in self.ghosts.items()}

    def set_ghost_state(self, name, state):
        self.ghosts[name].set_state(state)

    def activate_power_pellet(self):
        self.power_pellet_active = True
        for ghost in self.ghosts.values():
            ghost.set_state(GhostState.FLEE)

    def deactivate_power_pellet(self):
        self.power_pellet_active = False

    def update(self):
        if not self.power_pellet_active:
            # revert ghosts to original states if power pellet inactive
            self.ghosts['Blinky'].set_state(GhostState.CHASE)
            self.ghosts['Pinky'].set_state(GhostState.AMBUSH)
            self.ghosts['Inky'].set_state(GhostState.PATROL)
            self.ghosts['Clyde'].set_state(GhostState.RANDOM)
        else:
            # check if edible time expired
            now = time.time()
            for ghost in self.ghosts.values():
                if ghost.state == GhostState.FLEE and now > ghost.edible_until:
                    # revert to original state
                    if ghost.name == 'Blinky':
                        ghost.set_state(GhostState.CHASE)
                    elif ghost.name == 'Pinky':
                        ghost.set_state(GhostState.AMBUSH)
                    elif ghost.name == 'Inky':
                        ghost.set_state(GhostState.PATROL)
                    elif ghost.name == 'Clyde':
                        ghost.set_state(GhostState.RANDOM)

