"""Tile-based collision logic for Pac-Man game with boundary enforcement."""

from typing import List, Tuple

# Define tile types for clarity
WALL = 1
PELLET = 2
POWER_PELLET = 3
GHOST = 4
EMPTY = 0

class CollisionDetector:
    def __init__(self, maze_map: List[List[int]]):
        """Initialize with maze tile map.
        maze_map is a 2D list where each element represents a tile type."""
        self.maze_map = maze_map
        self.height = len(maze_map)
        self.width = len(maze_map[0]) if self.height > 0 else 0

    def is_wall(self, x: int, y: int) -> bool:
        """Check if the tile at (x, y) is a wall."""
        if 0 <= y < self.height and 0 <= x < self.width:
            return self.maze_map[y][x] == WALL
        return True  # Out of bounds treated as wall

    def is_pellet(self, x: int, y: int) -> bool:
        if 0 <= y < self.height and 0 <= x < self.width:
            return self.maze_map[y][x] == PELLET
        return False

    def is_power_pellet(self, x: int, y: int) -> bool:
        if 0 <= y < self.height and 0 <= x < self.width:
            return self.maze_map[y][x] == POWER_PELLET
        return False

    def is_ghost(self, x: int, y: int) -> bool:
        if 0 <= y < self.height and 0 <= x < self.width:
            return self.maze_map[y][x] == GHOST
        return False

    def can_move_to(self, x: int, y: int) -> bool:
        """Check if player can move to tile (x, y). Cannot move into walls or out of bounds."""
        if 0 <= y < self.height and 0 <= x < self.width:
            return self.maze_map[y][x] != WALL
        return False

    def detect_collision(self, x: int, y: int) -> Tuple[bool, str]:
        """Detect collision at tile (x, y).
        Returns tuple (collision: bool, collision_type: str) where collision_type is one of:
        'wall', 'pellet', 'power_pellet', 'ghost', or '' if no collision."""
        if not (0 <= y < self.height and 0 <= x < self.width):
            return True, 'wall'  # Treat out of bounds as wall collision
        tile = self.maze_map[y][x]
        if tile == WALL:
            return True, 'wall'
        elif tile == PELLET:
            return True, 'pellet'
        elif tile == POWER_PELLET:
            return True, 'power_pellet'
        elif tile == GHOST:
            return True, 'ghost'
        else:
            return False, ''


# End of collision.py

# Added a comment line to force commit
# End of file
