class GhostVisual:
    def __init__(self, identifier):
        self.identifier = identifier
        self.state = 'inactive'

    def set_state(self, new_state):
        valid_states = ['inactive', 'active', 'fading']
        if new_state in valid_states:
            self.state = new_state
        else:
            raise ValueError(f'Invalid state: {new_state}')

    def get_state(self):
        return self.state
