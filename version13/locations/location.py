from base.container import Container
from base.state import inventory

class Location(Container):
    def __init__(self, items=None):
        super().__init__(items)
        self.visited = False

    def visit(self):
        self.visited = True

    def was_visited(self):
        return self.visited

    def short_description(self):
        pass

    def long_description(self):
        self.short_description()

    def perform_action(self, action):
        pass

    def print_items(self):
        carryable_keys = []
        for item in self.items:
            if item.carryable and not item.described:
                carryable_keys.append(item.keys[0])
        if len(carryable_keys) > 0:
            print(f"Here there is: {", ".join(carryable_keys)}")

    def take_item(self, noun_key):
        if inventory().has_item_with_key(noun_key):
            print(f"You already have: {noun_key}!")
            return False

        container, item = self.find_item_with_key(noun_key)
        if item is None:
            print("There isn't one of these here.")
            self.print_items()
            return False

        if not item.carryable:
            print("You can't carry that.")
            return False

        inventory().add_item(item)
        container.remove_item_with_key(noun_key)
        print(f"You have taken: {noun_key}")
        return True
