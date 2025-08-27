from base.state import inventory, has_state, set_state
from locations.location import Location
from things.kitchen_cupboard_key import KitchenCupboardKey

class Library(Location):
    def visit(self):
        self.visited = True
        if has_state("library_fire_4"):
            print("The smoke and fire overwhelms you")
            set_state("died")

    def short_description(self):
        print("You are in the library.")

    def long_description(self):
        if has_state("library_fire_1") or has_state("library_fire_2") or has_state("library_fire_3"):
            print("You are in the library and the library is on fire!")
            print("Get out!")
        else:
            print("You are in a darkened library.")
            print("There is no window and the light does not work.")
            print("Every wall is shelved and there appear to be hundreds of dusty books here.")
            print("Maybe there is something here if you knew what to look for and could see it.")

    def perform_action(self, action):
        verb, noun = action

        if verb in ("find", "read"):
            if not has_state("candle_lit"):
                print("You can't see well enough to find anything.")
                return True

            if noun == "earthsea":
                print("You find the copy of Earthsea on the shelves.")
                if inventory().has_item_with_key("key"):
                    print("You open the book to find it is hollow in the middle, now empty.")
                else:
                    print("You open the book to find it is hollow in the middle, and containing a key.")
                    self.add_item(KitchenCupboardKey())
                return True

            print("There are hundreds of books here, but not that one.")
            return True

        return False

    def take_item(self, noun_key):
        if super().take_item(noun_key) and noun_key == "key":
            print("As you are trying to hold the book and candle at the same time, and trying to take the key, you accidentally drop the candle which starts some of the books burning.")
            set_state("library_fire_1")
