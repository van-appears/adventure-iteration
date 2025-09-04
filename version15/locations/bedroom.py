from locations.location import Location
from things.notebook import Notebook
from base.state import inventory

class Bedroom(Location):
    def __init__(self):
        super().__init__([Notebook()])

    def short_description(self):
        print("You are in the bedroom.")

    def long_description(self):
        print("You are in a small bedroom.")
        print("There is a small bed and a small bedside table.")
