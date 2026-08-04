"""
Boundary enforcement module for player movement within maze limits.
"""

from typing import Dict


def enforce_boundaries(current_pos: Dict[str, int], desired_pos: Dict[str, int], maze_width: int, maze_height: int) -> Dict[str, int]:
    """
    Enforce the boundaries of the maze so the player cannot move outside.

    Args:
        current_pos: Current position dictionary with 'x' and 'y' keys.
        desired_pos: Desired position dictionary with 'x' and 'y' keys.
        maze_width: Width of the maze (max x coordinate).
        maze_height: Height of the maze (max y coordinate).

    Returns:
        New position dictionary with 'x' and 'y' keys, adjusted to stay within boundaries.
    """
    new_x = max(0, min(desired_pos['x'], maze_width - 1))
    new_y = max(0, min(desired_pos['y'], maze_height - 1))
    return {'x': new_x, 'y': new_y}
