from game.state import has_state, set_state
from things.thing import Thing

class OfficeChest(Thing):
    def __init__(self):
        super().__init__("chest")

    def long_description(self):
        print("It is a heavy wooden chest, made of... let's say oak.")
        if has_state("chest_open"):
            print("On the inside of the lid is the word 'Earthsea'.")

    def perform_action(self, action):
        verb, noun = action

        if verb == "open":
            if has_state("chest_open"):
                print("The chest is already open")
            else:
                print("You have opened the chest.")
                print("On the inside of the lid is the word 'Earthsea'.")
                set_state("chest_open")
            return True

        if verb == "close" and noun == "chest":
            if has_state("chest_open"):
                print("You have closed the chest")
                set_state("chest_open", False)
            else:
                print("The chest is already closed")
            return True

        return False
