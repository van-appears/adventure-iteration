from base.state import has_state, set_state
from things.thing import Thing

class Honey(Thing):
    def __init__(self):
        super().__init__(key="honey", carryable=True)

    def long_description(self):
        if has_state("eaten_honey"):
            print("It is an empty jar of local honey.")
        else:
            print("It is a mostly full jar of local honey.")

    def perform_action(self, action):
        verb, _ = action

        if verb == "consume":
            if has_state("eaten_honey"):
                print("You have already eaten the honey. It was delicious.")
            else:
                print("You start eating the honey.")
                print("It is delicious, but you are a terribly messy eater and it gets everywhere, all down your front.")
                set_state("eaten_honey")
            return True

        return False
