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
        self.state = initial_state
        self.original_state = initial_state
        self.edible_until = None

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def make_edible(self, duration):
        self.set_state(GhostState.FLEE)
        self.edible_until = time.time() + duration

    def is_edible(self):
        if self.edible_until is None:
            return False
        return time.time() < self.edible_until

    def update(self):
        if self.edible_until and time.time() > self.edible_until:
            self.edible_until = None
            self.set_state(self.original_state)

class GhostManager:
    POWER_PELLET_DURATION = 10  # seconds

    def __init__(self):
        self.ghosts = {
            'Blinky': Ghost('Blinky', GhostState.CHASE),
            'Pinky': Ghost('Pinky', GhostState.CHASE),
            'Inky': Ghost('Inky', GhostState.CHASE),
            'Clyde': Ghost('Clyde', GhostState.CHASE),
        }
        # Set distinct original states for demonstration
        self.ghosts['Pinky'].original_state = GhostState.AMBUSH
        self.ghosts['Inky'].original_state = GhostState.PATROL
        self.ghosts['Clyde'].original_state = GhostState.RANDOM
        for ghost in self.ghosts.values():
            ghost.set_state(ghost.original_state)

        self.power_pellet_active = False
        self.power_pellet_activated_at = None

    def get_ghost_state(self, identity):
        return self.ghosts[identity].get_state()

    def get_all_states(self):
        return {identity: ghost.get_state() for identity, ghost in self.ghosts.items()}

    def set_ghost_state(self, identity, state):
        self.ghosts[identity].set_state(state)

    def activate_power_pellet(self):
        self.power_pellet_active = True
        self.power_pellet_activated_at = time.time()
        for ghost in self.ghosts.values():
            ghost.make_edible(self.POWER_PELLET_DURATION)

    def deactivate_power_pellet(self):
        self.power_pellet_active = False

    def update(self):
        if self.power_pellet_active:
            elapsed = time.time() - self.power_pellet_activated_at
            if elapsed > self.POWER_PELLET_DURATION:
                self.deactivate_power_pellet()

        for ghost in self.ghosts.values():
            ghost.update()

    def get_ghost_states(self):
        return {identity: ghost.get_state() for identity, ghost in self.ghosts.items()}


