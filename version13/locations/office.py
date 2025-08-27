from locations.location import Location
from base.state import has_state, set_state
from things.office_chest import OfficeChest

class Office(Location):
    def __init__(self):
        super().__init__([OfficeChest()])

    def visit(self):
        self.visited = True
        if has_state("office_fire_3"):
            print("The smoke and fire overwhelms you.")
            set_state("died")

    def short_description(self):
        print("You are in the office.")

    def long_description(self):
        print("You are in a lovely wood-panelled office.")
        print("There is a large wooden chest in the corner.")
