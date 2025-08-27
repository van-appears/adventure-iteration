from locations.location import Location
from things.kitchen_cupboard import KitchenCupboard
from things.kitchen_fridge import KitchenFridge
from things.kitchen_bottle import KitchenBottle
from things.kitchen_drawers import KitchenDrawers

class Kitchen(Location):
    def __init__(self):
        super().__init__([
          KitchenCupboard(),
          KitchenFridge(),
          KitchenBottle(),
          KitchenDrawers()
        ])

    def short_description(self):
        print("You are in the kitchen.")

    def long_description(self):
        print("You are in a smallish kitchen, it looks quite bare.")
        print("There is a fridge, a set of locked cupboards, and some drawers.")
        print("There is also a very large glass bottle beside the sink.")
