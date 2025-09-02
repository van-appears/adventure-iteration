class Container:
    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = items

    def item_keys(self):
        item_keys = []
        for item in self.items:
            item_keys.append(item.keys[0])
        return item_keys

    def find_items_with_key(self, key, all_list=None):
        if all_list is None:
            all_list = []

        for item in self.items:
            if key in item.keys:
                all_list.append((self, item))
            item.find_items_with_key(key, all_list)

        return all_list

    def has_direct_item_with_key(self, key):
        for item in self.find_items_with_key(key):
            if item[0] is self:
                return True
        return False

    def has_child_item_with_key(self, key):
        for item in self.find_items_with_key(key):
            if item[0] is not self:
                return True
        return False

    def remove_item_with_key(self, key):
        for item in self.items:
            if key in item.keys:
                self.items.remove(item)
                return item
        return None

    def add_item(self, item):
        self.items.append(item)

    def perform_action(self, action):
        return False
