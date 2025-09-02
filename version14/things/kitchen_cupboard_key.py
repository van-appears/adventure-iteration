from things.thing import Thing

class KitchenCupboardKey(Thing):
    def __init__(self):
        super().__init__(keys=["small key", "key"], carryable=True)

    def long_description(self):
        print("It's a small key.")
