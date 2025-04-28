from state import has_state, set_state

MAP = {
    "hall": {
        "north": "kitchen",
        "south": "library"
    },
    "kitchen": {
        "south": "hall"
    },
    "library": {
        "north": "hall",
        "west": "office"
    },
    "office": {
        "east": "library"
    }
}

def has_visited(room):
    return has_state(f"visited_{room}")

def describe_map():
    exits = MAP[has_state("room")]
    visited = []
    not_visited = []
    for direction, room in exits.items():
        if has_visited(room):
            visited.append((direction, room))
        else:
            not_visited.append(direction)

    for direction, room in visited:
        print(f"To the {direction} is the {room}.")

    if len(not_visited) > 1:
        print(f"There are rooms to the {", ".join(not_visited)}")
    elif len(not_visited) > 0:
        print(f"There is a room to the {not_visited[0]}.")

def move(action_string):
    direction = action_string.split(" ")[1]
    exits = MAP[has_state("room")]
    if direction in exits:
        next_room = exits[direction]
        set_state("room", next_room)
        return True

    print("There is no exit there.")
    return False

def move_to(action_string):
    location = action_string.split(" ")[2]
    if has_state("room") == location:
        print(f"You are already in the {location}!")
        return False

    if has_visited(location):
        exits = MAP[has_state("room")]
        if not location in exits.values():
            print(f"You walk back through the house to the {location}.")
        set_state("room", location)
        return True

    print(f"You haven't visited any {location} yet.")
    return False
