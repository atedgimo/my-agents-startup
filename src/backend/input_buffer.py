"""
Module for handling input buffering and smooth movement transitions in the game.

This module provides a class InputBuffer that queues player inputs and manages smooth
movement transitions between directions.
"""
from collections import deque
from enum import Enum, auto
from typing import Optional

class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    NONE = auto()  # No movement

class InputBuffer:
    def __init__(self, max_buffer_size: int = 5):
        """Initialize the input buffer with a maximum buffer size."""
        self.buffer = deque(maxlen=max_buffer_size)
        self.current_direction: Direction = Direction.NONE
        self.next_direction: Optional[Direction] = None

    def queue_input(self, direction: Direction):
        """Queue a new input direction into the buffer."""
        if direction != Direction.NONE:
            self.buffer.append(direction)

    def get_next_direction(self) -> Direction:
        """Get the next direction from the buffer if available, else return current."""
        if self.buffer:
            self.next_direction = self.buffer.popleft()
        else:
            self.next_direction = self.current_direction
        return self.next_direction

    def update_direction(self):
        """Update the current direction to the next direction smoothly."""
        # For simplicity, we directly update current direction here.
        # Movement smoothing logic can be enhanced here.
        self.current_direction = self.get_next_direction()

    def clear(self):
        """Clear the input buffer."""
        self.buffer.clear()
        self.current_direction = Direction.NONE
        self.next_direction = None

# Movement smoothing helper function

def smooth_transition(current: Direction, target: Direction) -> Direction:
    """Return a direction that smoothly transitions from current to target.
    This is a placeholder for more complex interpolation logic.
    """
    if current == target:
        return current
    # For now, just return target to simulate smooth transition
    return target
