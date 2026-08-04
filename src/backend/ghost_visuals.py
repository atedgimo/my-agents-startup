from enum import Enum
import threading

class GhostState(str, Enum):
    CHASE = 'chase'
    FLEE = 'flee'
    EATEN = 'eaten'
    PATROL = 'patrol'
    AMBUSH = 'ambush'
    RANDOM = 'random'

class Ghost:
    def __init__(self, identity, initial_state):
        self.identity = identity
        self.state = initial_state
        self.edible = False

    def set_state(self, state):
        self.state = state
        self.edible = (state == GhostState.FLEE)

    def is_edible(self):
        return self.edible

class GhostManager:
    def __init__(self):
        self.ghosts = {
            'Blinky': Ghost('Blinky', GhostState.CHASE),
            'Pinky': Ghost('Pinky', GhostState.CHASE),
            'Inky': Ghost('Inky', GhostState.CHASE),
            'Clyde': Ghost('Clyde', GhostState.CHASE),
        }
        self.power_pellet_active = False
        self.power_pellet_timer = None

    def get_all_states(self):
        return {g.identity: g.state for g in self.ghosts.values()}

    def get_ghost_states(self):
        return {g.identity: g.state for g in self.ghosts.values()}

    def get_ghost_state(self, identity):
        return self.ghosts[identity].state

    def set_ghost_state(self, identity, state):
        self.ghosts[identity].set_state(state)

    def activate_power_pellet(self):
        self.power_pellet_active = True
        for ghost in self.ghosts.values():
            ghost.set_state(GhostState.FLEE)
        # Start timer for power pellet duration
        if self.power_pellet_timer:
            self.power_pellet_timer.cancel()
        self.power_pellet_timer = threading.Timer(10.0, self.deactivate_power_pellet)
        self.power_pellet_timer.start()

    def deactivate_power_pellet(self):
        self.power_pellet_active = False
        # Revert ghosts to original states
        self.ghosts['Blinky'].set_state(GhostState.CHASE)
        self.ghosts['Pinky'].set_state(GhostState.AMBUSH)
        self.ghosts['Inky'].set_state(GhostState.PATROL)
        self.ghosts['Clyde'].set_state(GhostState.RANDOM)

    def update(self):
        # Called periodically to update ghost states
        if self.power_pellet_active:
            # Power pellet active, ghosts remain in flee state
            pass
        else:
            # Ensure ghosts are in their normal states
            self.deactivate_power_pellet()

