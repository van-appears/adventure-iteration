from base.state import has_state, set_state
from things.thing import Thing

class OfficeChest(Thing):
    def __init__(self):
        super().__init__(key="chest")

    def long_description(self):
        print("It is a heavy wooden chest, made of... let's say oak.")

    def perform_action(self, action):
        verb, _ = action

        if verb == "open":
            if has_state("fridge_opened"):
                print("You open the chest to find... nothing, it's just as empty as the fridge.")
            else:
                print("You open the chest to find... nothing, not even a paperclip.")
            set_state("chest_opened")
            return True

        return False
