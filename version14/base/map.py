from locations.hall import Hall
from locations.kitchen import Kitchen
from locations.library import Library
from locations.office import Office
from locations.stairs import Stairs
from locations.landing import Landing
from locations.bedroom import Bedroom
from locations.bathroom import Bathroom

LOCATIONS = {}

MAP = {
    "hall": {
        "north": "kitchen",
        "south": "office",
        "east": "stairs"
    },
    "kitchen": {
        "south": "hall"
    },
    "library": {
        "west": "office"
    },
    "office": {
        "north": "hall",
        "east": "library"
    },
    "landing": {
        "north": "bedroom",
        "east": "stairs",
        "south": "bathroom"
    },
    "bedroom": {
        "south": "landing"
    },
    "bathroom": {
        "north": "landing"
    }
}

def reset_map():
    LOCATIONS.clear()
    LOCATIONS["hall"] = Hall()
    LOCATIONS["kitchen"] = Kitchen()
    LOCATIONS["library"] = Library()
    LOCATIONS["office"] = Office()
    LOCATIONS["stairs"] = Stairs()
    LOCATIONS["landing"] = Landing()
    LOCATIONS["bedroom"] = Bedroom()
    LOCATIONS["bathroom"] = Bathroom()
    MAP["__current__"] = "hall"

def current_location():
    return LOCATIONS[MAP["__current__"]]

def describe_map():
    exits = MAP[MAP["__current__"]]
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
        print(f"There are rooms to the {", ".join(not_visited)}.")
    elif len(not_visited) > 0:
        print(f"There is a room to the {not_visited[0]}.")

def move(direction):
    exits = MAP[MAP["__current__"]]
    if direction in exits:
        next_room = exits[direction]
        if hasattr(LOCATIONS[next_room], "pass_through"):
            LOCATIONS[next_room].visit()
            next_room = LOCATIONS[next_room].pass_through(MAP["__current__"])

        MAP["__current__"] = next_room
        return True

    print("There is no exit there.")
    return False

def move_to(location):
    if MAP["__current__"] == location:
        print(f"You are already at the {location}!")
        return False

    if LOCATIONS[location].was_visited():
        if hasattr(LOCATIONS[location], "pass_through"):
            MAP[""] = LOCATIONS[location].pass_through(MAP["__current__"])
            return True

        exits = MAP[MAP["__current__"]]
        if not location in exits.values():
            print(f"You walk back through the house to the {location}.")
        MAP["__current__"] = location
        return True

    print(f"You haven't visited any {location} yet.")
    return False
