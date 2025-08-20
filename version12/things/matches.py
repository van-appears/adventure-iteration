from game.state import set_state, has_state
from things.thing import Thing

class Matches(Thing):
    def __init__(self):
        super().__init__(["matches", "match"], True)
        self.match_count = 3

    def long_description(self):
        print(f"It is a small box of {self.match_count} matches.")

    def perform_action(self, action):
        verb, _ = action

        if verb == "light":
            print("You light a match. It gives off a feeble glow.")
            self.match_count -= 1
            if self.match_count == 0:
                print("There are no matches left.")

                if not has_state("candle_lit"):
                    print("I dunno, I'd have thought in an adventure game matches might be useful for something.")
                    print("But you decided to burn them all for nothing.")
                    print("You never do manage to find a way out.")
                    print("You and the bear get more and more hungry.")
                    print("Eventually the bear decides to eat you.")
                    print("You find that being eaten alive is unpleasant.")
                    set_state("died")
            return True

        return False
