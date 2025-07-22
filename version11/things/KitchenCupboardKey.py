from game.state import has_state, set_state, inventory
from things.Thing import Thing
from things.Honey import Honey
from things.Hotsauce import Hotsauce

class KitchenCupboardKey(Thing):
    def __init__(self):
        super().__init__("key", True)

    def long_description(self):
        print("It's a small key.")
