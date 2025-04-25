from os import system

SYNONYMS = {
    "move": ["move", "head", "go", "walk", "run"],
    "move to": ["move to", "head to", "go to", "walk to", "run to"],
    "take": ["take", "get", "collect", "pick up"],
    "open": ["open", "unlock"],
    "close": ["close"],
    "attack": ["attack", "kick", "punch", "fight"],
    "pet": ["pet", "stroke", "cuddle", "pat"],
    "consume": ["consume", "eat", "drink"],
    "give": ["give", "throw", "drop"]
}

MAP = {
    "hall": {
        "north": "kitchen",
        "south": "office"
    },
    "kitchen": {
        "south": "hall"
    },
    "office": {
        "north": "hall"
    }
}

STATE = {}

def reset():
    STATE.clear()
    STATE["room"] = "hall"
    STATE["inventory"] = set()

    for key in MAP:
        if key.startswith("visited_"):
            MAP[key] = False

def starts_with_synonym(action_string, verb):
    for synonym in SYNONYMS[verb]:
        if action_string.startswith(f"{synonym} "):
            return True
    return False

def is_synonym_of(action_string, verb, noun):
    for synonym in SYNONYMS[verb]:
        if action_string == f"{synonym} {noun}":
            return True
    return False

def print_inventory():
    if len(STATE["inventory"]) == 0:
        print("You aren't carrying anything")
    else:
        print(f"You are carrying: {', '.join(STATE["inventory"])}")

def has_item(item):
    return item in STATE["inventory"]

def add_item(item):
    STATE["inventory"].add(item)

def has_state(key):
    if key not in STATE:
        return False
    return STATE[key]

def set_state(key, value=True):
    STATE[key] = value

def print_instructions():
    print("INSTRUCTIONS")
    print("To perform an action use 'verb noun' e.g. 'take item', 'open door'.")
    print("To move use 'go' or 'walk' with a direction e.g. 'go north'.")
    print("To move to a location you have visited before use 'go to' e.g. 'go to hall'.")
    print("To see a room description again use command 'look'")
    print("To see what you are carrying use command 'inventory'.")
    print("To exit the game use command 'quit'.")
    print("To see these instuctions again use command 'instructions'.")

def has_visited(room):
    return f"visited_{room}" in MAP and MAP[f"visited_{room}"]

def describe_map():
    exits = MAP[STATE["room"]]
    visited = []
    not_visited = []
    for direction, room in exits.items():
        if has_visited(room):
            visited.append((direction, room))
        else:
            not_visited.append(direction)

    for direction, room in visited:
        print(f"To the {direction} is the {room}.")

    if len(not_visited) > 0:
        if (len(not_visited) > 1):
            print(f"There are rooms to the {", ".join(not_visited)}")
        else:
            print(f"There is a room to the {not_visited[0]}.")

def move(action_string):
    direction = action_string.split(" ")[1]
    exits = MAP[STATE["room"]]
    if direction in exits:
        next_room = exits[direction]
        STATE["room"] = next_room
        return True
    else:
        print("There is no exit there.")
        return False

def move_to(action_string):
    location = action_string.split(" ")[2]
    if f"visited_{location}" in MAP and MAP[f"visited_{location}"]:
        exits = MAP[STATE["room"]]
        if not location in exits.values():
            print(f"You walk back through the house to the {location}.")
        STATE["room"] = location
        return True
    else:
        print(f"You haven't visited any {location} yet.")
        return False

def hall_action(action):
    if has_state("eaten_honey"):
        print("The bear smells the honey that you dropped all over youself.")
        print("It decides you must be good to eat.")
        print("So it eats you.")
        set_state("died")

    elif (action == "" and not has_visited("hall")) or action == "look":
        MAP["visited_hall"] = True
        print("You don't know how you got here, but you're standing in the hall of a house.")
        if has_state("bear_fed",):
            print("There is a sleepy, well-fed bear in the corner of the room.")
        else:
            print("You would like to leave the house, but there is a grumpy looking bear in front of the exit.")
        print("The windows are barred, so it looks like the door is the only way out.")
        describe_map()

    elif action == "":
        print("You are in the hall.")

    elif is_synonym_of(action, "attack", "bear") or is_synonym_of(action, "pet", "bear"):
        print("The bear didn't like that, it is a wild animal after all.")
        print("It rips your head off and starts to eat your body.")
        set_state("died")

    elif is_synonym_of(action, "give", "honey"):
        if has_item("honey"):
            print("You open the jar of honey and set it near the bear.")
            print("The bear sniffs it, then delightedly picks it up, moves to the corner of the room, and starts eating.")
            print("This is your chance to escape!")
            set_state("bear_fed")
        else:
            print("You don't have any honey.")

    elif is_synonym_of(action, "give", "hotsauce"):
        if has_item("hotsauce"):
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

    elif is_synonym_of(action, "open", "door"):
        if has_state("bear_fed"):
            set_state("escaped")
        else:
            print("I don't think so, there's a grumpy bear blocking the door.")

    else:
        print("I don't think that will help")

def office_action(action):
    if (action == "" and not has_visited("office")) or action == "look":
        MAP["visited_office"] = True
        print("You are in a lovely wood-panelled office. There is a large wooden chest in the corner.")
        describe_map()

    elif action == "":
        print("You are in the office.")

    elif is_synonym_of(action, "take", "key"):
        if has_item("key"):
            print("You already have the key")
        elif has_state("chest_open"):
            print("You have taken the key")
            add_item("key")
        elif has_state("chest_opened"):
            print("You can't take the key, you closed the chest")
        else:
            print("What key?")

    elif is_synonym_of(action, "take", "chest"):
        print("The chest is far too heavy")

    elif is_synonym_of(action, "open", "chest"):
        if has_state("chest_open"):
            print("The chest is already open")
        else:
            print("You have opened the chest.")
            print("There is a key inside!")
            set_state("chest_open")
            set_state("chest_opened")

    elif is_synonym_of(action, "close", "chest"):
        if has_state("chest_open"):
            print("You have closed the chest")
            set_state("chest_open", False)
        else:
            print("The chest is already closed")

    else:
        print("I don't think that will help")

def kitchen_action(action):
    if (action == "" and not has_visited("kitchen")) or action == "look":
        MAP["visited_kitchen"] = True
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
        elif has_state("cupboard_open") or has_item("hotsauce", state):
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

def main():
    hall_action("")
    print("How will you get out?")

    while not has_state("escaped") and not has_state("died") and not has_state("quit"):
        action = input("> ").strip().lower()
        moving = None

        if starts_with_synonym(action, "move to"):
            moving = move_to(action)
            action = ""

        elif starts_with_synonym(action, "move"):
            moving = move(action)
            action = ""

        if moving == False:
            pass

        if action == "instructions":
            print_instructions()

        elif action == "inventory":
            print_inventory()

        elif action == "quit":
            set_state("quit")

        elif has_state("room") == "hall":
            hall_action(action)

        elif has_state("room") == "kitchen":
            kitchen_action(action)

        elif has_state("room") == "office":
            office_action(action)

    if has_state("escaped"):
        print("You open the door and walk out into the sunshine. Well done!")
        print("Game over")
        return True

    elif has_state("died"):
        print("You are very very dead. Bad luck!")
        print("Game over")
        return True

    else:
        return False

def game():
    system("clear||cls")
    print_instructions()
    print("")
    playing = True
    while playing:
        reset()
        game_over = main()
        if game_over:
            print("")
            replay = input("Do you want to play again? yes or no? ").strip().lower()
            if replay.startswith("no"):
                playing = False
            elif not replay.startswith("yes"):
                print("I'll take that as 'no'.")
                playing = False
            else:
                system("clear||cls")
        else:
            playing = False

    print("Goodbye!")

game()
