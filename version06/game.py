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

STATE = {
  "room": "hall",
  "inventory": set()
}

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

def has_item(item):
    return item in STATE["inventory"]

def add_item(item):
    STATE["inventory"].add(item)

def has(key):
    if key not in STATE:
        return False
    return STATE[key]

def set(key, value=True):
    STATE[key] = value

def has_visited(room):
    return f"visited_{room}" in MAP

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
        MAP[f"visited_{STATE["room"]}"] = True
        STATE["room"] = next_room
        return True
    else:
        print("There is no exit there.")
        return False

def hall_action(action):
    if has("eaten_honey"):
        print("The bear smells the honey that you dropped all over youself.")
        print("It decides you must be good to eat.")
        print("So it eats you.")
        set("died")

    elif (action == "" and not has_visited("hall")) or action == "describe":
        print("You don't know how you got here, but you're standing in the hall of a house.")
        if has("bear_fed",):
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
        set("died")

    elif is_synonym_of(action, "give", "honey"):
        if has_item("honey"):
            print("You carefully open the jar of honey and set it near the bear.")
            print("The bear sniffs it, then delightedly picks it up, moves to the corner of the room, and starts eating.")
            print("This is your chance to escape!")
            set("bear_fed")
        else:
            print("You don't have any honey.")

    elif is_synonym_of(action, "give", "hotsauce"):
        if has_item("hotsauce"):
            print("You carefully open the bottle of hotsaue and set it near the bear.")
            print("The bear sniffs it, picks it up, and tries some of it.")
            print("There is a pause.")
            print("The bear looks unhappy.")
            print("The bear looks angry.")
            print("The bear knows you are to blame.")
            print("The bear decides you might taste nicer than the hotsauce.")
            print("The bear eats you.")
            set("died")
        else:
            print("You don't have any hotsauce.")

    elif is_synonym_of(action, "open", "door"):
        if has("bear_fed"):
            set("escaped")
        else:
            print("I don't think so, there's a grumpy bear blocking the door.")

    else:
        print("I don't think that will help")

def office_action(action):
    if (action == "" and not has_visited("office")) or action == "describe":
        print("You are in a lovely wood-panelled office. There is a large wooden chest in the corner.")
        describe_map()

    elif action == "":
        print("You are in the office.")

    elif is_synonym_of(action, "take", "key"):
        if has_item("key"):
            print("You already have the key")
        elif has("chest_open"):
            print("You have taken the key")
            add_item("key")
        elif has("chest_opened"):
            print("You can't take the key, you closed the chest")
        else:
            print("What key?")

    elif is_synonym_of(action, "take", "chest"):
        print("The chest is far too heavy")

    elif is_synonym_of(action, "open", "chest"):
        if has("chest_open"):
            print("The chest is already open")
        else:
            print("You have opened the chest.")
            if has_item("key"):
                print("The chest is empty.")
            else:
                print("There is a key inside!")
            set("chest_open")
            set("chest_opened")

    elif is_synonym_of(action, "close", "chest"):
        if has("chest_open"):
            print("You have closed the chest")
            set("chest_open", False)
        else:
            print("The chest is already closed")

    else:
        print("I don't think that will help")

def kitchen_action(action):
    if (action == "" and not has_visited("kitchen")) or action == "describe":
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
            set("cupboard_open")
        else:
            print("You can't, the cupboard is locked.")

    elif is_synonym_of(action, "take", "honey"):
        if has("cupboard_open"):
            print("You take the honey.")
            add_item("honey")
        else:
            print("What honey?")

    elif is_synonym_of(action, "consume", "honey"):
        if has("eaten_honey"):
            print("You've already eaten the honey.")
            print("You've all covered in it, remember?")
        elif has("cupboard_open") or has_item("honey"):
            print("You start eating the honey.")
            print("You are a terribly messy eater, it gets everywhere, all down your front.")
            set("eaten_honey")

    elif is_synonym_of(action, "take", "hotsauce"):
        if has("cupboard_open"):
            print("You take the hotsauce.")
            add_item("hotsauce")
        else:
            print("What hotsauce?")

    elif is_synonym_of(action, "consume", "hotsauce"):
        if has("eaten_hotsauce"):
            print("You've already eaten the hotsauce.")
            print("Even thinking about it brings back sweats and headaches.")
        elif has("cupboard_open") or has_item("hotsauce", state):
            print("You start drinking the whole bottle of hotsauce.")
            print("Aarrgh... so hot... so painful... your stomach hurts")
            print("You want to be sick.")
            print("This was a bad idea.")
            set("eaten_hotsauce")

    elif is_synonym_of(action, "close", "cupboard"):
        if has("chest_open"):
            print("You have closed the chest")
            set("chest_open")
        else:
            print("The chest is already closed")

    else:
        print("I don't think that will help")

def main():
    hall_action("")
    print("How will you get out?")

    while not has("escaped") and not has("died"):
        action = input("> ").strip().lower()
        moving = None

        if starts_with_synonym(action, "move"):
            moving = move(action)
            action = ""

        if moving == False:
            pass

        elif has("room") == "hall":
            hall_action(action)

        elif has("room") == "kitchen":
            kitchen_action(action)

        elif has("room") == "office":
            office_action(action)

    if has("escaped"):
        print("You open the door and walk out into the sunshine. Well done!")
    else:
        print("You are very very dead. Bad luck!")

    print("Game over")

main()
