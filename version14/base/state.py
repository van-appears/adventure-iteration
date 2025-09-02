from base.container import Container

STATE = {}

def reset_state():
    keep_get_action = STATE["__GET_ACTION"]
    STATE.clear()
    STATE["room"] = "hall"
    STATE["inventory"] = Container()
    STATE["__GET_ACTION"] = keep_get_action

def has_state(key):
    if key not in STATE:
        return False
    return STATE[key]

def set_state(key, value=True):
    STATE[key] = value

def get_action_method():
    return STATE["__GET_ACTION"]

def inventory():
    return STATE["inventory"]

def next_state():
    if has_state("hall_fire_4"):
        print("The hall is now completely ablaze.")
        print("You have no means of escaping.")
        print("Eventually the smoke and fire overwhelms you.")
        set_state("died")
    elif has_state("hall_fire_3"):
        set_state("hall_fire_4")
    elif has_state("hall_fire_2"):
        print("The fire has now spread to the hall.")
        if has_state("bear_fed"):
            print("The bear looks up from the honey; it is looking scared.")
        else:
            print("The bear is looking scared.")
        set_state("hall_fire_3")
    elif has_state("hall_fire_1"):
        set_state("hall_fire_2")
    elif has_state("office_fire_2"):
        print("The office is now completely ablaze.")
        set_state("hall_fire_1")
    elif has_state("office_fire_1"):
        set_state("office_fire_2")
    elif has_state("library_fire_4"):
        print("The fire has now spread to the office.")
        set_state("office_fire_1")
    elif has_state("library_fire_3"):
        print("The library is now completely ablaze.")
        set_state("library_fire_4")
    elif has_state("library_fire_2"):
        print("The fire spreads rapidly up the bookcase.")
        set_state("library_fire_3")
    elif has_state("library_fire_1"):
        set_state("library_fire_2")

def keep_going():
    return not has_state("escaped") and not has_state("died") and not has_state("quit")