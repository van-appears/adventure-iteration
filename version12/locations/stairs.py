from locations.location import Location

class Stairs(Location):
    def pass_through(self, last_room):
        if last_room in ("landing", "bedroom"):
            print("You go down the stairs and back into the hall.")
            return "hall"

        print("You go up the stairs to the landing.")
        return "landing"
