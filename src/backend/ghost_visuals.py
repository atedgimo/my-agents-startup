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
    def __init__(self, identity):
        self.identity = identity
        self.state = GhostState.CHASE
        self.original_state = self.state
        self.edible_until = 0

    def visual_identifier(self):
        if self.state == GhostState.FLEE:
            return 'flee'
        elif self.state == GhostState.EATEN:
            return 'eaten'
        else:
            return self.state.value

    def update_state(self, player_powered_up=False):
        current_time = time.time()
        if player_powered_up:
            self.state = GhostState.FLEE
            self.edible_until = current_time + 10
        else:
            if self.state == GhostState.FLEE and current_time > self.edible_until:
                self.state = self.original_state

    def is_edible(self):
        return self.state == GhostState.FLEE

class GhostManager:
    def __init__(self):
        self.ghosts = {
            'Blinky': Ghost('Blinky'),
            'Pinky': Ghost('Pinky'),
            'Inky': Ghost('Inky'),
            'Clyde': Ghost('Clyde')
        }

        self.ghosts['Blinky'].state = GhostState.CHASE
        self.ghosts['Blinky'].original_state = GhostState.CHASE
        self.ghosts['Pinky'].state = GhostState.AMBUSH
        self.ghosts['Pinky'].original_state = GhostState.AMBUSH
        self.ghosts['Inky'].state = GhostState.PATROL
        self.ghosts['Inky'].original_state = GhostState.PATROL
        self.ghosts['Clyde'].state = GhostState.RANDOM
        self.ghosts['Clyde'].original_state = GhostState.RANDOM

    def get_all_states(self):
        return {name: ghost.visual_identifier() for name, ghost in self.ghosts.items()}

    def get_ghost_state(self, identity):
        if identity in self.ghosts:
            return self.ghosts[identity].state
        return None

    def set_ghost_state(self, identity, state):
        if identity in self.ghosts:
            self.ghosts[identity].state = state

    def activate_power_pellet(self):
        for ghost in self.ghosts.values():
            ghost.update_state(player_powered_up=True)

    def deactivate_power_pellet(self):
        for ghost in self.ghosts.values():
            ghost.update_state(player_powered_up=False)

    def update(self):
        for ghost in self.ghosts.values():
            ghost.update_state(player_powered_up=False)
