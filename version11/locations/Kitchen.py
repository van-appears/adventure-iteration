from game.state import has_state, set_state, inventory
from locations.Location import Location
from things.KitchenCupboard import KitchenCupboard
from things.KitchenFridge import KitchenFridge

class Kitchen(Location):
    def __init__(self):
        super().__init__([KitchenCupboard(), KitchenFridge()])

    def short_description(self):
        print("You are in the kitchen.")

    def long_description(self):
        print("You are in a smallish kitchen, it looks quite bare.")
        print("There is a fridge and a set of locked cupboards.")
