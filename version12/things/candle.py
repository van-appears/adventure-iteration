from game.state import has_state, set_state, inventory
from things.thing import Thing

class Candle(Thing):
    def __init__(self):
        super().__init__("candle", True)

    def long_description(self):
        if has_state("candle_lit"):
            print("It is a lit candle giving off a faint but interesting scnet. Careful now!")
        else:
            print("It is a tall white candle.")
            print("There is a label on the side that says it is watermelon and nettle scented. Odd.")

    def perform_action(self, action):
        verb, _ = action

        if verb == "light":
            if has_state("candle_lit"):
                print("It's already lit!")
            elif inventory().has_item_with_key("matches"):
                print("You light the candle with one of the matches. Careful now!")
                inventory().find_item_with_key("matches")[1].match_count -= 1
                set_state("candle_lit")
            else:
                print("Light it with what?")
            return True

        return False