from game.state import has_state, set_state, has_item, add_item
from game.action_parser import is_synonym_of
from locations.Location import Location

class Office(Location):
    def short_description(self):
        print("You are in the office.")

    def long_description(self):
        print("You are in a lovely wood-panelled office.")
        print("There is a large wooden chest in the corner.")

    def perform_action(self, action):
        if is_synonym_of(action, "take", "chest"):
            print("The chest is far too heavy")

        elif is_synonym_of(action, "open", "chest"):
            if has_state("chest_open"):
                print("The chest is already open")
            else:
                print("You have opened the chest.")
                print("On the inside of the lid is the word 'Earthsea'.")
                set_state("chest_open")

        elif is_synonym_of(action, "close", "chest"):
            if has_state("chest_open"):
                print("You have closed the chest")
                set_state("chest_open", False)
            else:
                print("The chest is already closed")

        else:
            print("I don't think that will help")
