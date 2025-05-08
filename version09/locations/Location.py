class Location:
    def __init__(self):
        self.visited = False

    def visit(self):
        self.visited = True

    def was_visited(self):
        return self.visited

    def short_description(self):
        pass

    def long_description(self):
        short_description(self)

    def perform_action(self, action):
        pass
