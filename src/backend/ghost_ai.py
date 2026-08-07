from enum import Enum, auto
import threading
import time

class GhostVisualState(Enum):
    NORMAL = "normal"
    FRIGHTENED = "frightened"
    EATEN = "eaten"
    RETURNING = "returning"

class GhostState(Enum):
    IDLE = auto()
    CHASING = auto()
    FRIGHTENED = auto()
    EATEN = auto()
    RETURNING_HOME = auto()

class Ghost:
    def __init__(self, ghost_id):
        self.ghost_id = ghost_id
        self.state = GhostState.IDLE
        self.visual_state = GhostVisualState.NORMAL
        self.position = {'x': 0, 'y': 0}
        self.lock = threading.Lock()

    def set_state(self, new_state: GhostState):
        with self.lock:
            self.state = new_state
            # Update visual state based on game logic
            if new_state == GhostState.FRIGHTENED:
                self.visual_state = GhostVisualState.FRIGHTENED
            elif new_state == GhostState.EATEN:
                self.visual_state = GhostVisualState.EATEN
            elif new_state == GhostState.RETURNING_HOME:
                self.visual_state = GhostVisualState.RETURNING
            else:
                self.visual_state = GhostVisualState.NORMAL

    def get_visual_state(self):
        with self.lock:
            return self.visual_state

    def update_position(self, x, y):
        with self.lock:
            self.position['x'] = x
            self.position['y'] = y

    def get_position(self):
        with self.lock:
            return dict(self.position)

class GhostManager:
    def __init__(self):
        self.ghosts = {}
        self.lock = threading.Lock()

    def add_ghost(self, ghost_id):
        with self.lock:
            if ghost_id not in self.ghosts:
                self.ghosts[ghost_id] = Ghost(ghost_id)

    def set_ghost_state(self, ghost_id, state: GhostState):
        with self.lock:
            if ghost_id in self.ghosts:
                self.ghosts[ghost_id].set_state(state)

    def update_ghost_position(self, ghost_id, x, y):
        with self.lock:
            if ghost_id in self.ghosts:
                self.ghosts[ghost_id].update_position(x, y)

    def get_ghost_visual_states(self):
        with self.lock:
            return {
                ghost_id: {
                    "visual_state": ghost.get_visual_state().value,
                    "position": ghost.get_position()
                }
                for ghost_id, ghost in self.ghosts.items()
            }

# Singleton instance for global use
ghost_manager = GhostManager()
