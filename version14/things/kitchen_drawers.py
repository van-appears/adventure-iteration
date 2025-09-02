from base.state import inventory
from things.thing import Thing
from things.hammer import Hammer

class KitchenDrawers(Thing):
    def __init__(self):
        super().__init__(keys=["drawer", "drawers"])
        self.drawers_opened = False

    def long_description(self):
        print("It is a set of drawers.")
        if self.drawers_opened:
            print("The third drawer contains a hammer.")

    def perform_action(self, action):
        verb, _ = action

        if verb == "open":
            print("There are a few drawers, you check them one by one.")
            print("The first looks like it should have cutlery in it, but is completely empty.")
            print("The second drawer is also empty.")
            if inventory().has_direct_item_with_key("hammer"):
                print("The third drawer is empty.")
            else:
                print("The third drawer contains a hammer.")

            if not self.drawers_opened:
                self.items.extend([Hammer()])
                self.drawers_opened = True

            return True

        return False
