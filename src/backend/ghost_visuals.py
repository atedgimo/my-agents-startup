from enum import Enum

class GhostState(Enum):
    NORMAL = 'normal'
    FRIGHTENED = 'frightened'
    EATEN = 'eaten'

class GhostIdentity(Enum):
    BLINKY = 'blinky'
    PINKY = 'pinky'
    INKY = 'inky'
    CLYDE = 'clyde'

class Ghost:
    def __init__(self, identity, start_pos):
        self.identity = identity
        self.pos = start_pos
        self.state = GhostState.NORMAL
        self.respawn_timer = 0

    def set_state(self, state):
        self.state = state
        if state == GhostState.EATEN:
            self.respawn_timer = 180  # frames or ticks until respawn

    def update(self):
        if self.state == GhostState.EATEN:
            if self.respawn_timer > 0:
                self.respawn_timer -= 1
            else:
                self.state = GhostState.NORMAL

    def to_dict(self):
        return {
            'identity': self.identity.value,
            'pos': self.pos,
            'state': self.state.value
        }

class GhostManager:
    def __init__(self):
        self.ghosts = {
            GhostIdentity.BLINKY: Ghost(GhostIdentity.BLINKY, {'x': 5, 'y': 5}),
            GhostIdentity.PINKY: Ghost(GhostIdentity.PINKY, {'x': 10, 'y': 5}),
            GhostIdentity.INKY: Ghost(GhostIdentity.INKY, {'x': 5, 'y': 10}),
            GhostIdentity.CLYDE: Ghost(GhostIdentity.CLYDE, {'x': 10, 'y': 10}),
        }
        self.power_pellet_active = False
        self.power_pellet_timer = 0

    def get_all_states(self):
        return {identity.value: ghost.to_dict() for identity, ghost in self.ghosts.items()}

    def set_ghost_state(self, identity, state):
        if identity in self.ghosts:
            self.ghosts[identity].set_state(state)

    def activate_power_pellet(self):
        self.power_pellet_active = True
        self.power_pellet_timer = 600  # duration in frames
        for ghost in self.ghosts.values():
            if ghost.state == GhostState.NORMAL:
                ghost.set_state(GhostState.FRIGHTENED)

    def update(self):
        if self.power_pellet_active:
            self.power_pellet_timer -= 1
            if self.power_pellet_timer <= 0:
                self.power_pellet_active = False
                for ghost in self.ghosts.values():
                    if ghost.state == GhostState.FRIGHTENED:
                        ghost.set_state(GhostState.NORMAL)

        for ghost in self.ghosts.values():
            ghost.update()

        # TODO: Add ghost movement AI and collision logic here

