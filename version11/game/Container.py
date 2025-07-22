class Container:
    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = items;

    def item_keys(self):
        item_keys = []
        for item in self.items:
            item_keys.append(item.key)
        return item_keys

    def find_item_with_key(self, key):
        for item in self.items:
            if item.key == key:
                return (self, item)

            found = item.find_item_with_key(key)
            if found[1] is not None:
                return found

        return (None, None)

    def has_item_with_key(self, key):
        found = self.find_item_with_key(key)
        return found[1] is not None

    def remove_item_with_key(self, key):
        for item in self.items:
            if item.key == key:
                self.items.remove(item)
                return item
        return None

    def add_item(self, item):
        self.items.append(item)

    def perform_action(self, action):
        return False