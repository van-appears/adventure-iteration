from game.state import inventory
from locations.location import Location
from things.kitchen_cupboard_key import KitchenCupboardKey

class Library(Location):
    def short_description(self):
        print("You are in the library.")

    def long_description(self):
        print("You are in a dimly-lit library.")
        print("Every wall is shelved and there are hundreds of books here.")
        print("At least they look to be in alphabetical order if you knew what to look for.")

    def perform_action(self, action):
        verb, noun = action

        if verb in ("find", "read") and noun == "earthsea":
            print("You find the copy of Earthsea on the shelves.")
            if inventory().has_item_with_key("key"):
                print("You open the book to find it is hollow in the middle, now empty.")
            else:
                print("You open the book to find it is hollow in the middle, and containing a key.")
                self.add_item(KitchenCupboardKey())
            return True

        if verb in ("find", "read"):
            print("There are hundreds of books here, but not that one.")
            return True

        return False
