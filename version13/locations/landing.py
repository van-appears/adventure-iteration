from locations.location import Location

class Landing(Location):
    def short_description(self):
        print("You are on the first floor landing.")

    def long_description(self):
        print("You are on the first floor landing.")
        print("The carpet is a bit threadbare, but has a nice floral pattern.")
        print("There are some patches on the wall where there might have been paintings or photos.")
        print("There is a window at the far end of the landing, also barred.")
