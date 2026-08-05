class GhostState:
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

    def is_edible(self):
        if self.edible_until is None:
            return False
        return time.time() < self.edible_until

    def make_edible(self, duration):
        self.edible_until = time.time() + duration
        self.state = GhostState.FLEE

    def update(self):
        if self.edible_until and time.time() > self.edible_until:
            self.edible_until = None
            if self.state == GhostState.FLEE:
                self.state = self.original_state

import time

class GhostManager:
    def __init__(self):
        self.ghosts = {
            'Blinky': Ghost('Blinky', GhostState.CHASE),
            'Pinky': Ghost('Pinky', GhostState.AMBUSH),
            'Inky': Ghost('Inky', GhostState.PATROL),
            'Clyde': Ghost('Clyde', GhostState.RANDOM),
        }

    def get_all_states(self):
        return {gid: ghost.get_state() for gid, ghost in self.ghosts.items()}

    def set_ghost_state(self, ghost_id, state):
        if ghost_id in self.ghosts:
            self.ghosts[ghost_id].set_state(state)

    def get_ghost_state(self, ghost_id):
        if ghost_id in self.ghosts:
            return self.ghosts[ghost_id].get_state()
        return None

    def activate_power_pellet(self, duration=10):
        for ghost in self.ghosts.values():
            ghost.make_edible(duration)

    def deactivate_power_pellet(self):
        for ghost in self.ghosts.values():
            ghost.edible_until = None
            ghost.set_state(ghost.original_state)

    def update(self):
        for ghost in self.ghosts.values():
            ghost.update()
