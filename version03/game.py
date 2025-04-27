escaped = False
has_key = False
chest_open = False
chest_opened = False

synonyms = {
    "take": ["take", "get", "collect", "pick up"],
    "open": ["open", "unlock"],
    "close": ["close"]
}

def describe():
    print("You are standing in a room with a locked door.")
    if chest_open:
        print("There is a heavy opened wooden chest in the corner.")
    else:
        print("There is a heavy closed wooden chest in the corner.")

def is_synonym_of(action_string, verb, noun):
    for synonym in synonyms[verb]:
        if action_string == f"{synonym} {noun}":
            return True
    return False

describe()
print("How will you get out?")

while not escaped:
    action = input("> ").strip().lower()

    if action == "":
        describe()

    if is_synonym_of(action, "take", "key"):
        if has_key:
            print("You already have the key")
        elif chest_open:
            print("You have taken the key")
            has_key = True
        elif chest_opened:
            print("You can't take the key, you closed the chest")
        else:
            print("What key?")

    elif is_synonym_of(action, "take", "chest"):
        print("The chest is far too heavy")

    elif is_synonym_of(action, "open", "chest"):
        if chest_open:
            print("The chest is already open")
        else:
            print("You have opened the chest")
            if has_key:
                print("The chest is empty.")
            else:
                print("There is a key inside!")
            chest_open = True
            chest_opened = True

    elif is_synonym_of(action, "close", "chest"):
        if chest_open:
            print("You have closed the chest")
            chest_open = False
        else:
            print("The chest is already closed")

    elif is_synonym_of(action, "open", "door"):
        if has_key:
            escaped = True
        else:
            print("The door is locked")

    elif action != "":
        print("I don't think that will help")

print("""You unlock the door and walk out into the sunshine. Well done!
Game over""")
