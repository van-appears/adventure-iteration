from locations.Hall import Hall
from locations.Kitchen import Kitchen
from locations.Library import Library
from locations.Office import Office

LOCATIONS = {
    "hall": Hall(),
    "kitchen": Kitchen(),
    "library": Library(),
    "office": Office()
}

MAP = {
    "current": "hall",
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

def current_location():
    return LOCATIONS[MAP["current"]]

def describe_map():
    exits = MAP[MAP["current"]]
    visited = []
    not_visited = []
    for direction, room in exits.items():
        if LOCATIONS[room].was_visited():
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
    exits = MAP[MAP["current"]]
    if direction in exits:
        next_room = exits[direction]
        MAP["current"] = next_room
        return True

    print("There is no exit there.")
    return False

def move_to(action_string):
    location = action_string.split(" ")[2]
    if MAP["current"] == location:
        print(f"You are already in the {location}!")
        return False

    if LOCATIONS[location].was_visited():
        exits = MAP[MAP["current"]]
        if not location in exits.values():
            print(f"You walk back through the house to the {location}.")
        MAP["current"] = location
        return True

    print(f"You haven't visited any {location} yet.")
    return False
