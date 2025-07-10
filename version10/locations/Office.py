from game.state import has_state, set_state
from locations.Location import Location

class Office(Location):
    def short_description(self):
        print("You are in the office.")

    def long_description(self):
        print("You are in a lovely wood-panelled office.")
        print("There is a large wooden chest in the corner.")

    def perform_action(self, action):
        verb, noun = action

        if verb == "take" and noun == "chest":
            print("The chest is far too heavy")

        elif verb == "take":
            self.take_item(noun)

        elif verb == "open" and noun == "chest":
            if has_state("chest_open"):
                print("The chest is already open")
            else:
                print("You have opened the chest.")
                print("On the inside of the lid is the word 'Earthsea'.")
                set_state("chest_open")

        elif verb == "close" and noun == "chest":
            if has_state("chest_open"):
                print("You have closed the chest")
                set_state("chest_open", False)
            else:
                print("The chest is already closed")

        else:
            print("I don't think that will help")
