class Container:
    def __init__(self, items=None):
        if items is None:
            self.items = dict()
        else:
            self.items = items;

    def item_keys(self):
        item_keys = []
        for key in self.items:
            item_keys.append(key)
        return item_keys

    def remove_item(self, key):
        if key in self.items:
            return self.items.pop(key)
        return None

    def add_item(self, key):
        self.items[key] = True

    def has_item(self, key):
        return key in self.items