from base.state import has_state, set_state, inventory
from locations.location import Location

class Hall(Location):
    def __init__(self):
        super().__init__()
        self.visited = True

    def visit(self):
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

        if verb in ("attack", "pet") and noun == "bear":
            print("The bear didn't like that, it is a wild animal after all.")
            print("It rips your head off and starts to eat your body.")
            set_state("died")
            return True

        if verb in ("give", "throw") and noun == "honey":
            if inventory().has_direct_item_with_key("honey"):
                print("You open the jar of honey and set it near the bear.")
                print("The bear sniffs it, picks it up, moves to the corner of the room, and starts eating.")
                print("The door is no longer blocked!")
                set_state("bear_fed")
            else:
                print("You don't have any honey.")
            return True

        if verb in ("give", "throw") and noun == "hotsauce":
            if inventory().has_direct_item_with_key("hotsauce"):
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
            return True

        if verb == "throw" and noun == "hammer":
            if inventory().has_direct_item_with_key("hammer"):
                print("You throw the hammer with excellent aim.")
                print("It makes a lovely 'boink' noise as it bounces off the bear's head.")
                print("There is a pause.")
                print("The bear looks unhappy.")
                print("The bear looks angry.")
                print("With excellent aim, the bear's claws rip your chest open.")
                print("The are some lovely crunching and squelching noises as the bear eats you.")
                set_state("died")
            else:
                print("You don't have a hammer.")
            return True

        if verb == "open" and noun == "door":
            if has_state("bear_fed"):
                if inventory().has_direct_item_with_key("door key"):
                    print("You unlock the door and walk out into the sunshine.")
                    if has_state("hall_fire_2"):
                        print("The terrified bear comes running out the door after you, and squishes you flat.")
                        set_state("died")
                    else:
                        set_state("escaped")
                else:
                    print("The door is locked! You only have a small key, which does not work here.")
            else:
                print("I don't think so, there's a grumpy bear blocking the door.")
            return True

        return False
