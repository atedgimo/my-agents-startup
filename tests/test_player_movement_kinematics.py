import pytest

class Player:
    def __init__(self):
        self.x = 5
        self.y = 5

    def move_right(self):
        self.x += 1
        if self.x >= 19:
            self.x = 1


def test_player_moves_right_one_tile_per_update():
    player = Player()
    initial_x = player.x
    player.move_right()
    assert player.x == initial_x + 1

    # Move until just before wrap around
    for _ in range(12):
        player.move_right()
    assert player.x == 18

    # Move to boundary wrap
    player.move_right()
    assert player.x == 1

if __name__ == '__main__':
    pytest.main()
