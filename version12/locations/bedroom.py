from locations.location import Location
from things.candle import Candle

class Bedroom(Location):
    def __init__(self):
        super().__init__([Candle()])

    def short_description(self):
        print("You are in the bedroom.")

    def long_description(self):
        print("You are in a small bedroom.")
        print("There is a small bed and a small bedside table.")
