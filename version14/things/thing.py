from base.container import Container

class Thing(Container):
    def __init__(self, key=None, keys=None, carryable=False, described=False, items=None):
        self.carryable = carryable
        self.described = described
        if keys is not None:
            self.keys = keys
        else:
            self.keys = [key]
        super().__init__(items)

    def long_description(self):
        pass
