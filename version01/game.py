print("You are standing in a room with a closed door. How will you get out?")

escaped = False
while not escaped:
    action = input("> ").strip().lower()
    if action == "open door":
        escaped = True
    elif not action == "":
        print("I don't think that will help")

print("You open the door and walk out into the sunshine. Well done!")
print("Game over")
