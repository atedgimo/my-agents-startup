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
    def __init__(self, identity, initial_state):
        self.identity = identity
        self.original_state = initial_state
        self.state = initial_state
        self.edible_until = 0

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def activate_edible(self, duration):
        self.set_state(GhostState.FLEE)
        self.edible_until = time.time() + duration

    def is_edible(self):
        return self.state == GhostState.FLEE and time.time() < self.edible_until

    def update(self):
        if self.state == GhostState.FLEE and time.time() >= self.edible_until:
            self.state = self.original_state


class GhostManager:
    EDIBLE_DURATION = 10  # seconds

    def __init__(self):
        self.ghosts = {
            'Blinky': Ghost('Blinky', GhostState.CHASE),
            'Pinky': Ghost('Pinky', GhostState.AMBUSH),
            'Inky': Ghost('Inky', GhostState.PATROL),
            'Clyde': Ghost('Clyde', GhostState.RANDOM),
        }
        self.power_pellet_active = False

    def get_ghost_state(self, identity):
        return self.ghosts[identity].get_state()

    def set_ghost_state(self, identity, state):
        self.ghosts[identity].set_state(state)

    def get_all_states(self):
        return {identity: ghost.get_state() for identity, ghost in self.ghosts.items()}

    def activate_power_pellet(self):
        self.power_pellet_active = True
        for ghost in self.ghosts.values():
            ghost.activate_edible(self.EDIBLE_DURATION)

    def deactivate_power_pellet(self):
        self.power_pellet_active = False

    def update(self):
        for ghost in self.ghosts.values():
            ghost.update()

        if not self.power_pellet_active:
            # Revert ghosts to their original states if power pellet not active
            for ghost in self.ghosts.values():
                if ghost.get_state() == GhostState.FLEE:
                    ghost.set_state(ghost.original_state)
