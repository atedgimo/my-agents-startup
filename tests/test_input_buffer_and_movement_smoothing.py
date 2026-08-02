import unittest
from src.backend.input_buffer import InputBuffer, Direction, smooth_transition

class TestInputBuffer(unittest.TestCase):
    def setUp(self):
        self.input_buffer = InputBuffer(max_buffer_size=3)

    def test_queue_and_get_next_direction(self):
        self.input_buffer.queue_input(Direction.UP)
        self.input_buffer.queue_input(Direction.LEFT)
        self.assertEqual(self.input_buffer.get_next_direction(), Direction.UP)
        self.assertEqual(self.input_buffer.get_next_direction(), Direction.LEFT)

    def test_buffer_max_size(self):
        self.input_buffer.queue_input(Direction.UP)
        self.input_buffer.queue_input(Direction.DOWN)
        self.input_buffer.queue_input(Direction.LEFT)
        self.input_buffer.queue_input(Direction.RIGHT)  # This should evict the oldest (UP)
        self.assertNotIn(Direction.UP, self.input_buffer.buffer)
        self.assertIn(Direction.RIGHT, self.input_buffer.buffer)

    def test_update_direction(self):
        self.input_buffer.queue_input(Direction.RIGHT)
        self.input_buffer.update_direction()
        self.assertEqual(self.input_buffer.current_direction, Direction.RIGHT)

    def test_clear(self):
        self.input_buffer.queue_input(Direction.UP)
        self.input_buffer.clear()
        self.assertEqual(len(self.input_buffer.buffer), 0)
        self.assertEqual(self.input_buffer.current_direction, Direction.NONE)

class TestSmoothTransition(unittest.TestCase):
    def test_same_direction(self):
        self.assertEqual(smooth_transition(Direction.UP, Direction.UP), Direction.UP)

    def test_different_direction(self):
        self.assertEqual(smooth_transition(Direction.UP, Direction.LEFT), Direction.LEFT)

if __name__ == '__main__':
    unittest.main()
