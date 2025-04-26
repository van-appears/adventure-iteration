from state import has_state, set_state, has_item, add_item
from action_parser import is_synonym_of
from map import has_visited, describe_map

def kitchen_action(action):
    if (action == "" and not has_visited("kitchen")) or action == "look":
        set_state("visited_hall")
        print("You are in a smallish kitchen, it looks quite bare.")
        print("There is a fridge and a set of locked cupboards.")
        describe_map()

    elif action == "":
        print("You are in the kitchen.")

    elif is_synonym_of(action, "open", "fridge"):
        print("You open the fridge and... nothing.")
        print("Not even a mouldy nubbin of cheese.")
        print("You close the fridge again.")

    elif is_synonym_of(action, "take", "fridge"):
        print("The fridge is far too heavy")

    elif is_synonym_of(action, "open", "cupboard"):
        if has_item("key"):
            print("You unlock the cupboard.")
            print("There is a bottle of hotsauce and a pot of honey inside.")
            set_state("cupboard_open")
        else:
            print("You can't, the cupboard is locked.")

    elif is_synonym_of(action, "take", "honey"):
        if has_state("cupboard_open"):
            print("You take the honey.")
            add_item("honey")
        else:
            print("What honey?")

    elif is_synonym_of(action, "consume", "honey"):
        if has_state("eaten_honey"):
            print("You've already eaten the honey.")
            print("You've all covered in it, remember?")
        elif has_state("cupboard_open") or has_item("honey"):
            print("You start eating the honey.")
            print("You are a terribly messy eater, it gets everywhere, all down your front.")
            set_state("eaten_honey")

    elif is_synonym_of(action, "take", "hotsauce"):
        if has_state("cupboard_open"):
            print("You take the hotsauce.")
            add_item("hotsauce")
        else:
            print("What hotsauce?")

    elif is_synonym_of(action, "consume", "hotsauce"):
        if has_state("eaten_hotsauce"):
            print("You've already eaten the hotsauce.")
            print("Even thinking about it brings back sweats and headaches.")
        elif has_state("cupboard_open") or has_item("hotsauce"):
            print("You start drinking the whole bottle of hotsauce.")
            print("Aarrgh... so hot... so painful... your stomach hurts")
            print("You want to be sick.")
            print("This was a bad idea.")
            set_state("eaten_hotsauce")

    elif is_synonym_of(action, "close", "cupboard"):
        if has_state("chest_open"):
            print("You have closed the chest")
            set_state("chest_open")
        else:
            print("The chest is already closed")

    else:
        print("I don't think that will help")
