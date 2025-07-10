from game.state import has_state, set_state, inventory
from locations.Location import Location

class Kitchen(Location):
    def short_description(self):
        print("You are in the kitchen.")

    def long_description(self):
        print("You are in a smallish kitchen, it looks quite bare.")
        print("There is a fridge and a set of locked cupboards.")

    def perform_action(self, action):
        verb, noun = action

        if verb == "take" and noun == "fridge":
            print("The fridge is far too heavy")

        elif verb == "take":
            self.take_item(noun)

        elif verb == "open" and noun == "fridge":
            print("You open the fridge and... nothing.")
            print("Not even a mouldy nubbin of cheese.")
            print("You close the fridge again.")

        elif verb == "open" and noun == "cupboard":
            if inventory().has_item("key"):
                print("You unlock the cupboard.")
                self.add_item("honey")
                self.add_item("hotsauce")
                self.print_items()
                set_state("cupboard_open")
            else:
                print("You can't, the cupboard is locked.")

        elif verb == "consume" and noun == "honey":
            if has_state("eaten_honey"):
                print("You've already eaten the honey.")
                print("You've all covered in it, remember?")
            elif has_state("cupboard_open") or inventory().has_item("honey"):
                print("You start eating the honey.")
                print("You are a terribly messy eater, it gets everywhere, all down your front.")
                set_state("eaten_honey")

        elif verb == "consume" and noun == "hotsauce":
            if has_state("eaten_hotsauce"):
                print("You've already eaten the hotsauce.")
                print("Even thinking about it brings back sweats and headaches.")
            elif has_state("cupboard_open") or inventory().has_item("hotsauce"):
                print("You start drinking the whole bottle of hotsauce.")
                print("Aarrgh... so hot... so painful... your stomach hurts")
                print("You want to be sick.")
                print("This was a bad idea.")
                set_state("eaten_hotsauce")

        elif verb == "close" and noun == "cupboard":
            if has_state("chest_open"):
                print("You have closed the chest")
                set_state("chest_open")
            else:
                print("The chest is already closed")

        else:
            print("I don't think that will help")
