SYNONYMS = {
    "take": ["take", "get", "collect", "pick up"],
    "open": ["open", "unlock"],
    "close": ["close"],
    "move": ["move", "head", "go", "walk", "run"],
    "attack": ["attack", "kick", "punch", "fight"],
    "pet": ["pet", "stroke", "cuddle", "pat"],
    "consume": ["consume", "eat", "drink"],
    "give": ["give", "throw", "drop"]
}

def is_synonym_of(action_string, verb, noun):
    for synonym in SYNONYMS[verb]:
        if action_string == f"{synonym} {noun}":
            return True
    return False

def has_item(item, state):
    return item in state["inventory"]

def add_item(item, state):
    state["inventory"].add(item)

def hall_action(action, state):
    if state["has_eaten_honey"]:
        print("The bear smells the honey that you dropped all over youself.")
        print("It decides you must be good to eat.")
        print("So it eats you.")
        state["dead"] = True

    elif (action == "" and not state["has_visited_hall"]) or action == "describe":
        print("You don't know how you got here, but you're standing in the hall of a house.")
        if state["bear_fed"]:
            print("There is a sleepy, well-fed bear in the corner of the room.")
        else:
            print("You would like to leave the house, but there is a grumpy looking bear in front of the exit.")
        print("The windows are barred, so it looks like the door is the only way out.")
        state["has_visited_hall"] = True

        if state["has_visited_kitchen"] and state["has_visited_office"]:
            print("The kitchen is to the north and the office is to the south.")
        elif state["has_visited_kitchen"]:
            print("The kitchen is to the north and there is another room to the south.")
        elif state["has_visited_office"]:
            print("There is a room to the north and the office is to the south.")
        else:
            print("There are rooms to the north and the south")

    elif action == "":
        print("You are in the hall.")

    elif is_synonym_of(action, "move", "north"):
        state["room"] = "KITCHEN"
        kitchen_action("", state)

    elif is_synonym_of(action, "move", "south"):
        state["room"] = "OFFICE"
        office_action("", state)

    elif is_synonym_of(action, "attack", "bear") or is_synonym_of(action, "pet", "bear"):
        print("The bear didn't like that, it is a wild animal after all.")
        print("It rips your head off and starts to eat your body.")
        state["dead"] = True

    elif is_synonym_of(action, "give", "honey"):
        if has_item("honey", state):
            print("You carefully open the jar of honey and set it near the bear.")
            print("The bear sniffs it, then delightedly picks it up, moves to the corner of the room, and starts eating.")
            print("This is your chance to escape!")
            state["bear_fed"] = True
        else:
            print("You don't have any honey.")

    elif is_synonym_of(action, "give", "hotsauce"):
        if has_item("hotsauce", state):
            print("You carefully open the bottle of hotsaue and set it near the bear.")
            print("The bear sniffs it, picks it up, and tries some of it.")
            print("There is a pause.")
            print("The bear looks unhappy.")
            print("The bear looks angry.")
            print("The bear knows you are to blame.")
            print("The bear decides you might taste nicer than the hotsauce.")
            print("The bear eats you.")
            state["dead"] = True
        else:
            print("You don't have any hotsauce.")

    elif is_synonym_of(action, "open", "door"):
        if state["bear_fed"]:
            state["escaped"] = True
        else:
            print("I don't think so, there's a grumpy bear blocking the door.")

    else:
        print("I don't think that will help")

def office_action(action, state):
    if (action == "" and not state["has_visited_office"]) or action == "describe":
        print("You are in a lovely wood-panelled office. There is a large wooden chest in the corner.")
        print("To the north is the door back to the hall.")
        state["has_visited_office"] = True

    elif action == "":
        print("You are in the office.")

    elif is_synonym_of(action, "move", "north"):
        state["room"] = "HALL"
        hall_action("", state)

    elif is_synonym_of(action, "take", "key"):
        if has_item("key", state):
            print("You already have the key")
        elif state["chest_open"]:
            print("You have taken the key")
            add_item("key", state)
        elif state["chest_opened"]:
            print("You can't take the key, you closed the chest")
        else:
            print("What key?")

    elif is_synonym_of(action, "take", "chest"):
        print("The chest is far too heavy")

    elif is_synonym_of(action, "open", "chest"):
        if state["chest_open"]:
            print("The chest is already open")
        else:
            print("You have opened the chest.")
            print("There is a key inside!")
            state["chest_open"] = True
            state["chest_opened"] = True

    elif is_synonym_of(action, "close", "chest"):
        if state["chest_open"]:
            print("You have closed the chest")
            state["chest_open"] = False
        else:
            print("The chest is already closed")

    else:
        print("I don't think that will help")

def kitchen_action(action, state):
    if (action == "" and not state["has_visited_kitchen"]) or action == "describe":
        print("You are in a smallish kitchen, it looks quite bare.")
        print("There is a fridge and a set of locked cupboards.")
        print("To the south is the door back to the hall.")
        state["has_visited_kitchen"] = True

    elif action == "":
        print("You are in the kitchen.")

    elif is_synonym_of(action, "move", "south"):
        state["room"] = "HALL"
        hall_action("", state)

    elif is_synonym_of(action, "open", "fridge"):
        print("You open the fridge and... nothing.")
        print("Not even a mouldy nubbin of cheese.")
        print("You close the fridge again.")

    elif is_synonym_of(action, "take", "fridge"):
        print("The fridge is far too heavy")

    elif is_synonym_of(action, "open", "cupboard"):
        if has_item("key", state):
            print("You unlock the cupboard.")
            print("There is a bottle of hotsauce and a pot of honey inside.")
            state["cupboard_open"] = True
        else:
            print("You can't, the cupboard is locked.")

    elif is_synonym_of(action, "take", "honey"):
        if state["cupboard_open"]:
            print("You take the honey.")
            add_item("honey", state)
        else:
            print("What honey?")

    elif is_synonym_of(action, "consume", "honey"):
        if state["has_eaten_honey"]:
            print("You've already eaten the honey.")
            print("You've all covered in it, remember?")
        elif state["cupboard_open"] or has_item("honey", state):
            print("You start eating the honey.")
            print("You are a terribly messy eater, it gets everywhere, all down your front.")
            state["has_eaten_honey"] = True

    elif is_synonym_of(action, "take", "hotsauce"):
        if state["cupboard_open"]:
            print("You take the hotsauce.")
            add_item("hotsauce", state)
        else:
            print("What hotsauce?")

    elif is_synonym_of(action, "consume", "hotsauce"):
        if state["has_eaten_hotsauce"]:
            print("You've already eaten the hotsauce.")
            print("Even thinking about it brings back sweats and headaches.")
        elif state["cupboard_open"] or has_item("hotsauce", state):
            print("You start drinking the whole bottle of hotsauce.")
            print("Aarrgh... so hot... so painful... your stomach hurts")
            print("You want to be sick.")
            print("This was a bad idea.")
            state["has_eaten_hotsauce"] = True

    elif is_synonym_of(action, "close", "cupboard"):
        if state["chest_open"]:
            print("You have closed the chest")
            state["chest_open"] = False
        else:
            print("The chest is already closed")

    else:
        print("I don't think that will help")

def main():
    state = {
        "room": "HALL",
        "has_visited_hall": False,
        "has_visited_kitchen": False,
        "has_visited_office": False,
        "has_eaten_honey": False,
        "has_eaten_hotsauce": False,
        "bear_fed": False,
        "escaped": False,
        "dead": False,
        "chest_open": False,
        "chest_opened": False,
        "inventory": set()
    }

    hall_action("", state)
    print("How will you get out?")

    while not state["escaped"] and not state["dead"]:
        action = input("> ").strip().lower()

        if state["room"] == "HALL":
            hall_action(action, state)

        elif state["room"] == "KITCHEN":
            kitchen_action(action, state)

        elif state["room"] == "OFFICE":
            office_action(action, state)

    if state["escaped"]:
        print("You open the door and walk out into the sunshine. Well done!")
    else:
        print("You are very very dead. Bad luck!")

    print("Game over")

main()
