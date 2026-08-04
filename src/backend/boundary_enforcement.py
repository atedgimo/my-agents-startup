from typing import Dict


def enforce_boundaries(current_pos: Dict[str, int], desired_pos: Dict[str, int], maze_width: int, maze_height: int) -> Dict[str, int]:
    """Clamp the desired position within the maze boundaries."""
    x = desired_pos.get('x', 0)
    y = desired_pos.get('y', 0)

    # Clamp x and y to maze boundaries
    if x < 0:
        x = 0
    elif x >= maze_width:
        x = maze_width - 1

    if y < 0:
        y = 0
    elif y >= maze_height:
        y = maze_height - 1

    return {'x': x, 'y': y}
