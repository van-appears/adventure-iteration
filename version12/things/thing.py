from game.container import Container

class Thing(Container):
    def __init__(self, keyOrKeys, carryable=False, items=None):
        self.carryable = carryable
        if isinstance(keyOrKeys, list):
            self.keys = keyOrKeys
        else:
            self.keys = [keyOrKeys]
        super().__init__(items)

    def long_description(self):
        pass
