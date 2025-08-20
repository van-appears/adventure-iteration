from things.thing import Thing

class Hammer(Thing):
    def __init__(self):
        super().__init__("hammer", True)

    def long_description(self):
        print("It is a nice solid hammer.")
