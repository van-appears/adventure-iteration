from game.state import inventory
from things.thing import Thing
from things.honey import Honey
from things.hotsauce import Hotsauce

class KitchenCupboard(Thing):
    def __init__(self):
        super().__init__(["cupboard", "cupboards"])
        self.opened = False

    def long_description(self):
        print("It is a cupboard. There's not much to say about cupboards.")
        if not self.opened:
            print("It is also locked, that's probably important to say.")
        elif len(self.items) > 0:
            print(f"Inside the cupboard is: {", ".join(self.item_keys())}")
        else:
            print("The cupboard is bare.")

    def perform_action(self, action):
        verb, _ = action

        if verb == "open":
            if self.opened:
                print("You already opened it.")
            elif inventory().has_item_with_key("key"):
                print("You unlock the cupboard with the key.")
                print("There is a bottle of hotsauce and a pot of honey inside.")
                self.items.extend([Honey(), Hotsauce()])
                self.opened = True
            else:
                print("You can't, the cupboard is locked.")
            return True

        return False
