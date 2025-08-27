from locations.location import Location
from things.candle import Candle

class Bathroom(Location):
    def __init__(self):
        super().__init__([Candle()])

    def short_description(self):
        print("You are in the bedroom.")

    def long_description(self):
        print("You are in an avocado-green bathroom, very 70s-style.")
        print("There is a scented candle beside the bath.")
