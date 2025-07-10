from game.state import has_state, set_state, inventory
from locations.Location import Location

class Library(Location):
    def short_description(self):
        print("You are in the library.")

    def long_description(self):
        print("You are in a dimly-lit library.")
        print("Every wall is shelved and there are hundreds of books here.")
        print("At least they look to be in alphabetical order if you knew what to look for.")

    def perform_action(self, action):
        verb, noun = action

        if verb == "take":
            self.take_item(noun)

        elif (verb == "find" or verb == "read") and noun == "earthsea":
            print("You find the copy of Earthsea on the shelves.")
            if inventory().has_item("key"):
                print("You open the book to find it is hollow in the middle, now empty.")
            else:
                print("You open the book to find it is hollow in the middle, and containing a key.")
                self.add_item("key");
            set_state("book_found")

        elif verb == "find" or verb == "read":
            print("There are hundreds of books here, but not that one.")

        else:
            print("I don't think that will help")
