print("""You are standing in a room with a locked door.
There is a table with a key on it.
How will you get out?""")

escaped = False
has_key = False

while not escaped:
    action = input("> ").strip().lower()

    if action in ("take key", "get key", "pick up key"):
        if has_key:
            print("You already have the key")
        else:
            print("You have taken the key")
            has_key = True

    elif "key" in action.split(" "):
        print("I don't know how to do that with the key")

    elif action in ("open door", "unlock door"):
        if has_key:
            escaped = True
        else:
            print("The door is locked")

    elif "door" in action.split(" "):
        print("I don't know how to do that with the door")

    elif action != "":
        print("I don't think that will help")

print("""You unlock the door and walk out into the sunshine. Well done!
Game over""")
