from locations.location import Location
from things.photograph import Photograph

class Landing(Location):
    def __init__(self):
        super().__init__([Photograph()])

    def short_description(self):
        print("You are on the first floor landing.")

    def long_description(self):
        print("You are on the first floor landing.")
        print("The carpet is a bit threadbare, but has a nice floral pattern.")
        print("There is a photograph on the wall.")
        print("There is a window at the far end of the landing, also barred.")
