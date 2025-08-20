from game.state import has_state, set_state
from things.thing import Thing

class Hotsauce(Thing):
    def __init__(self):
        super().__init__(["hotsauce", "hot sauce"], True)

    def long_description(self):
        print("It is a small bottle of hotsauce with the label showing a chicken wearing a luchador mask.")
        if has_state("eaten_hotsauce"):
            print("It is empty.")

    def perform_action(self, action):
        verb, _ = action

        if verb == "consume":
            if has_state("eaten_hotsauce"):
                print("You have already eaten the hotsauce. You regret it.")
            else:
                print("You start drinking the whole bottle of hotsauce.")
                print("Aarrgh... so hot... so painful... your stomach hurts.")
                print("You want to be sick.")
                print("This was a bad idea.")
                set_state("eaten_hotsauce")
            return True

        return False
