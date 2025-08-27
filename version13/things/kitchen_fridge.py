from base.state import has_state, set_state
from things.thing import Thing

class KitchenFridge(Thing):
    def __init__(self):
        super().__init__(key="fridge")

    def long_description(self):
        print("It is a fridge. It seems to be working.")

    def perform_action(self, action):
        verb, _ = action

        if verb == "open":
            if has_state("chest_opened"):
                print("You open the fridge to find... nothing, it's just as empty as the chesty.")
            else:
                print("You open the fridge to find... nothing, not even a nubbin of cheese.")
            set_state("fridge_opened")
            return True

        return False
