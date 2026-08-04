from enum import Enum

class GhostIdentity(Enum):
    BLINKY = 'blinky'
    PINKY = 'pinky'
    INKY = 'inky'
    CLYDE = 'clyde'

class GhostState(Enum):
    SCATTER = 'scatter'
    CHASE = 'chase'
    FRIGHTENED = 'frightened'
    EATEN = 'eaten'

class Ghost:
    def __init__(self, identity: GhostIdentity, position: dict):
        self.identity = identity
        self.position = position
        self.state = GhostState.SCATTER

    def set_state(self, state: GhostState):
        self.state = state

    def get_state(self):
        return self.state

    def move(self, new_position: dict):
        self.position = new_position

class GhostManager:
    def __init__(self):
        self.ghosts = {
            GhostIdentity.BLINKY: Ghost(GhostIdentity.BLINKY, {'x': 5, 'y': 5}),
            GhostIdentity.PINKY: Ghost(GhostIdentity.PINKY, {'x': 10, 'y': 5}),
            GhostIdentity.INKY: Ghost(GhostIdentity.INKY, {'x': 5, 'y': 10}),
            GhostIdentity.CLYDE: Ghost(GhostIdentity.CLYDE, {'x': 10, 'y': 10}),
        }

    def get_all_states(self):
        return {identity.value: {'position': ghost.position, 'state': ghost.state.value} for identity, ghost in self.ghosts.items()}

    def set_ghost_state(self, identity: GhostIdentity, state: GhostState):
        if identity in self.ghosts:
            self.ghosts[identity].set_state(state)

    def activate_power_pellet(self):
        for ghost in self.ghosts.values():
            ghost.set_state(GhostState.FRIGHTENED)

    def update(self):
        # Placeholder for ghost AI update logic
        pass
