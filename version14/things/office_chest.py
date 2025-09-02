from base.state import has_state, set_state, get_action_method
from things.front_door_key import FrontDoorKey
from things.thing import Thing

class OfficeChest(Thing):
    def __init__(self):
        super().__init__(key="chest")

    def long_description(self):
        print("It is a heavy wooden chest, made of... let's say oak.")
        print("It has a combination lock on the outside.")

    def perform_action(self, action):
        verb, _ = action

        if verb == "open":
            if not has_state("chest_opened"):
                next_action = get_action_method()
                combination = next_action("What combination?").strip()
                if combination == "1122":
                    print("You open the chest to find a door key inside.")
                    self.add_item(FrontDoorKey())
                    set_state("chest_opened")
                else:
                    print("No, that didn't seem to work.")
            else:
                print("The chest is already opened.")
            return True

        return False
