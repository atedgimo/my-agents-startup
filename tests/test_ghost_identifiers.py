import unittest
from src.backend.ghost_identifiers import GhostVisualIdentifier, GhostStateManager

class TestGhostVisualIdentifier(unittest.TestCase):
    def test_initial_state(self):
        ghost = GhostVisualIdentifier(id=1, state='inactive')
        self.assertEqual(ghost.state, 'inactive')

    def test_update_state(self):
        ghost = GhostVisualIdentifier(id=1, state='inactive')
        ghost.update_state('active')
        self.assertEqual(ghost.state, 'active')

class TestGhostStateManager(unittest.TestCase):
    def test_add_and_get_ghost(self):
        manager = GhostStateManager()
        ghost = GhostVisualIdentifier(id=1, state='inactive')
        manager.add_ghost(ghost)
        self.assertEqual(manager.get_ghost_state(1), 'inactive')

    def test_update_ghost_state(self):
        manager = GhostStateManager()
        ghost = GhostVisualIdentifier(id=1, state='inactive')
        manager.add_ghost(ghost)
        manager.update_ghost_state(1, 'active')
        self.assertEqual(manager.get_ghost_state(1), 'active')

if __name__ == '__main__':
    unittest.main()
