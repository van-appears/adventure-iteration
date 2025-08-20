from game.state import has_state, set_state, inventory
from things.thing import Thing
from things.matches import Matches

class KitchenBottle(Thing):
    def __init__(self):
        super().__init__("bottle")

    def long_description(self):
        if has_state("bottle_smashed"):
            print("There is the smashed remains of a large glass bottle")
            if not inventory().has_item_with_key("matches"):
                print("Amidst the wreckage is a small box of matches.")
        else:
            print("It is a large glass bottle. Very large.")
            print("One of those champagne bottles with the weird names probably.")
            print("There seems to be something at the bottom of it.")

    def perform_action(self, action):
        verb, _ = action

        if verb == "break":
            if has_state("bottle_smashed"):
                print("It's already smashed. Nothing to be gained from making it smasheder.")
            elif inventory().has_item_with_key("hammer"):
                print("You smash the bottom to smithereens with the hammer.")
                print("You keep going until there are only tiny little pieces left.")
                print("It was quite satisfying.")
                print("Amidst the wreckage is a small box of matches.")
                self.items.extend([Matches()])
                set_state("bottle_smashed")
            else:
                print("You try breaking the bottle on the ground, but it is quite resilient and remains intact.")
            return True

        return False
