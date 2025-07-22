from game.state import has_state, set_state
from locations.Location import Location
from things.OfficeChest import OfficeChest

class Office(Location):
    def __init__(self):
        super().__init__([OfficeChest()])

    def short_description(self):
        print("You are in the office.")

    def long_description(self):
        print("You are in a lovely wood-panelled office.")
        print("There is a large wooden chest in the corner.")
