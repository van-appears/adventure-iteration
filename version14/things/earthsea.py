from base.state import inventory
from things.thing import Thing
from things.kitchen_cupboard_key import KitchenCupboardKey

class Earthsea(Thing):
    def __init__(self):
        super().__init__(key="earthsea", carryable=True, described=True)

    def long_description(self):
        print("It's a copy of Ursula K. Le Guin's classic 'Earthsea' novel.")

    def perform_action(self, action):
        verb, _ = action
        if verb in ("open", "read"):
            if inventory().has_direct_item_with_key("small key"):
                print("You open the book to find it is hollow in the middle, now empty.")
            else:
                print("You open the book to find it is hollow in the middle, and containing a key.")
                if not self.has_direct_item_with_key("small key"):
                    self.add_item(KitchenCupboardKey())
            return True

        return False
