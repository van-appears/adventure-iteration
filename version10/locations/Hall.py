from game.state import has_state, set_state, inventory
from locations.Location import Location

class Hall(Location):
    def visit(self):
        self.visited = True
        if has_state("eaten_honey"):
            print("The bear smells the honey that you dropped all over youself.")
            print("It decides you must be good to eat.")
            print("So it eats you.")
            set_state("died")

    def short_description(self):
        print("You are in the hall.")

    def long_description(self):
        print("You are standing in the hall of a house.")
        if has_state("bear_fed",):
           print("There is a sleepy, well-fed bear in the corner of the room.")
        else:
           print("There is a grumpy looking bear in front of the exit.")
        print("The windows are barred, so it looks like the door is the only way out.")

    def perform_action(self, action):
        verb, noun = action

        if verb == "take":
            self.take_item(noun)

        elif (verb == "attack" or verb == "pet") and noun == "bear":
            print("The bear didn't like that, it is a wild animal after all.")
            print("It rips your head off and starts to eat your body.")
            set_state("died")

        elif verb == "give" and noun == "honey":
            if inventory().has_item("honey"):
                print("You open the jar of honey and set it near the bear.")
                print("The bear sniffs it, then delightedly picks it up, moves to the corner of the room, and starts eating.")
                print("This is your chance to escape!")
                set_state("bear_fed")
            else:
                print("You don't have any honey.")

        elif verb == "give" and noun == "hotsauce":
            if inventory().has_item("hotsauce"):
                print("You open the bottle of hotsauce and set it near the bear.")
                print("The bear sniffs it, picks it up, and tries some of it.")
                print("There is a pause.")
                print("The bear looks unhappy.")
                print("The bear looks angry.")
                print("The bear knows you are to blame.")
                print("The bear decides you might taste nicer than the hotsauce.")
                print("The bear eats you.")
                set_state("died")
            else:
                print("You don't have any hotsauce.")

        elif verb == "open" and noun == "door":
            if has_state("bear_fed"):
                set_state("escaped")
            else:
                print("I don't think so, there's a grumpy bear blocking the door.")

        else:
            print("I don't think that will help")
