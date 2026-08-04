"""Boundary enforcement logic to prevent player from jittering or corner cutting."""

def enforce_boundaries(current_pos, desired_pos, maze_width, maze_height):
    """
    Enforce strict grid-aligned movement constraints.
    Player must remain in center of tile during turn transitions.
    No corner cutting allowed.

    Args:
        current_pos (dict): {'x': int, 'y': int} current player position
        desired_pos (dict): {'x': int, 'y': int} desired new position
        maze_width (int): width of maze in tiles
        maze_height (int): height of maze in tiles

    Returns:
        dict: new valid position after enforcement
    """
    # Clamp desired position to maze boundaries
    x = max(0, min(desired_pos['x'], maze_width - 1))
    y = max(0, min(desired_pos['y'], maze_height - 1))

    # Enforce player remains centered on tile (integer coordinates)
    x = int(round(x))
    y = int(round(y))

    # Prevent corner cutting: only allow moves that are strictly horizontal or vertical
    dx = x - current_pos['x']
    dy = y - current_pos['y']

    if dx != 0 and dy != 0:
        # Diagonal move attempted, reject and keep current position
        return current_pos

    return {'x': x, 'y': y}


# End of boundary_enforcement.py

# Added a comment line to force commit
# End of file
