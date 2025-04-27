SYNONYMS = {
    "take": ["take", "get", "collect", "pick up"],
    "open": ["open", "unlock"],
    "close": ["close"],
    "move": ["head", "go", "walk", "run", "move"]
}

def is_synonym_of(action_string, verb, noun):
    for synonym in SYNONYMS[verb]:
        if action_string == f"{synonym} {noun}":
            return True
    return False

def hall_action(action, state):
    if action == "":
        print("You are standing in a hallway. There is a locked door here.")
        print("To the north is the kitchen.")

    elif is_synonym_of(action, "move", "north"):
        state["room"] = "KITCHEN"
        kitchen_action("", state)

    elif is_synonym_of(action, "open", "door"):
        if state["has_key"]:
            state["escaped"] = True
        else:
            print("The door is locked")

    else:
        print("I don't think that will help")

def kitchen_action(action, state):
    if action == "":
        print("You are standing in a kitchen.")
        if state["chest_open"]:
            print("There is a heavy opened wooden chest in the corner.")
        else:
            print("There is a heavy closed wooden chest in the corner.")
        print("To the south is the hallway.")

    elif is_synonym_of(action, "move", "south"):
        state["room"] = "HALL"
        hall_action("", state)

    elif is_synonym_of(action, "take", "key"):
        if state["has_key"]:
            print("You already have the key")
        elif state["chest_open"]:
            print("You have taken the key")
            state["has_key"] = True
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
            if state["has_key"]:
                print("The chest is empty.")
            else:
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

def main():
    state = {
        "room": "HALL",
        "escaped": False,
        "has_key": False,
        "chest_open": False,
        "chest_opened": False
    }

    hall_action("", state)
    print("How will you get out?")

    while not state["escaped"]:
        action = input("> ").strip().lower()

        if state["room"] == "HALL":
            hall_action(action, state)

        elif state["room"] == "KITCHEN":
            kitchen_action(action, state)

    print("You unlock the door and walk out into the sunshine. Well done!")
    print("Game over")

main()
