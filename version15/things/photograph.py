from base.state import has_state
from things.thing import Thing

class Photograph(Thing):
    def __init__(self):
        super().__init__(keys=["photograph", "photo"], carryable=False)

    def long_description(self):
        birthday = has_state("birthday")
        print("It is a photo of a cute doggy.")
        print(f"At the bottom of the photo it says 'Fluffikins, born {birthday}'.")
