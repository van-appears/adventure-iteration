from things.thing import Thing

class KitchenFridge(Thing):
    def __init__(self):
        super().__init__("fridge")

    def long_description(self):
        print("It is a fridge. It seems to be working.")

    def perform_action(self, action):
        verb, _ = action

        if verb == "open":
            print("You open the fridge to find... nothing, not even a nubbin of cheese.")
            return True

        return False
