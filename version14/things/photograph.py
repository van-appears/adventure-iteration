from things.thing import Thing

class Photograph(Thing):
    def __init__(self):
        super().__init__(keys=["photograph", "photo"], carryable=False)

    def long_description(self):
        print("It is a photo of a cute doggy.")
        print("At the bottom of the photo it says 'Fluffikins, born November 22nd'.")
