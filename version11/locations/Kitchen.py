from locations.location import Location
from things.kitchen_cupboard import KitchenCupboard
from things.kitchen_fridge import KitchenFridge

class Kitchen(Location):
    def __init__(self):
        super().__init__([KitchenCupboard(), KitchenFridge()])

    def short_description(self):
        print("You are in the kitchen.")

    def long_description(self):
        print("You are in a smallish kitchen, it looks quite bare.")
        print("There is a fridge and a set of locked cupboards.")
