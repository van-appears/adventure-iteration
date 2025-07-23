from game.container import Container

class Thing(Container):
    def __init__(self, key, carryable=False, items=None):
        self.carryable = carryable
        self.key = key
        super().__init__(items)

    def long_description(self):
        pass
