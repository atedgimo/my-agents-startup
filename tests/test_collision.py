import unittest
from src.backend.collision import CollisionDetector, WALL, PELLET, POWER_PELLET, GHOST, EMPTY

class TestCollisionDetector(unittest.TestCase):
    def setUp(self):
        # Simple 5x5 maze for testing
        # 1 = wall, 2 = pellet, 3 = power pellet, 4 = ghost, 0 = empty
        self.maze_map = [
            [WALL, WALL, WALL, WALL, WALL],
            [WALL, PELLET, EMPTY, POWER_PELLET, WALL],
            [WALL, EMPTY, GHOST, EMPTY, WALL],
            [WALL, PELLET, EMPTY, EMPTY, WALL],
            [WALL, WALL, WALL, WALL, WALL],
        ]
        self.detector = CollisionDetector(self.maze_map)

    def test_is_wall(self):
        self.assertTrue(self.detector.is_wall(0, 0))
        self.assertTrue(self.detector.is_wall(4, 4))
        self.assertFalse(self.detector.is_wall(2, 2))
        self.assertTrue(self.detector.is_wall(-1, 0))  # out of bounds
        self.assertTrue(self.detector.is_wall(0, 5))   # out of bounds

    def test_is_pellet(self):
        self.assertTrue(self.detector.is_pellet(1, 1))
        self.assertFalse(self.detector.is_pellet(2, 2))

    def test_is_power_pellet(self):
        self.assertTrue(self.detector.is_power_pellet(3, 1))
        self.assertFalse(self.detector.is_power_pellet(1, 1))

    def test_is_ghost(self):
        self.assertTrue(self.detector.is_ghost(2, 2))
        self.assertFalse(self.detector.is_ghost(1, 1))

    def test_can_move_to(self):
        self.assertFalse(self.detector.can_move_to(0, 0))  # wall
        self.assertTrue(self.detector.can_move_to(2, 2))   # ghost tile but not wall
        self.assertFalse(self.detector.can_move_to(-1, 0)) # out of bounds

    def test_detect_collision(self):
        self.assertEqual(self.detector.detect_collision(0, 0), (True, 'wall'))
        self.assertEqual(self.detector.detect_collision(1, 1), (True, 'pellet'))
        self.assertEqual(self.detector.detect_collision(3, 1), (True, 'power_pellet'))
        self.assertEqual(self.detector.detect_collision(2, 2), (True, 'ghost'))
        self.assertEqual(self.detector.detect_collision(2, 3), (False, ''))
        self.assertEqual(self.detector.detect_collision(-1, 0), (True, 'wall'))

if __name__ == '__main__':
    unittest.main()
