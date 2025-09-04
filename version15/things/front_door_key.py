from things.thing import Thing

class FrontDoorKey(Thing):
    def __init__(self):
        super().__init__(keys=["door key", "front door key", "key"], carryable=True)

    def long_description(self):
        print("It's a key with a fob with 'front door key' written on it.")
