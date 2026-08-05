# Ghost AI logic for visual identifiers and state management

class Ghost:
    def __init__(self, id):
        self.id = id
        self.state = 'normal'  # could be 'normal', 'frightened', 'eaten'

    def update_state(self, power_up_active):
        if power_up_active:
            self.state = 'frightened'
        else:
            self.state = 'normal'

    def get_visual_identifier(self):
        if self.state == 'frightened':
            return 'blue'
        elif self.state == 'eaten':
            return 'eyes'
        else:
            return 'normal'


class GhostManager:
    def __init__(self):
        self.ghosts = [Ghost(i) for i in range(4)]

    def update_ghosts(self, power_up_active):
        for ghost in self.ghosts:
            ghost.update_state(power_up_active)

    def get_ghost_visuals(self):
        return [ghost.get_visual_identifier() for ghost in self.ghosts]
