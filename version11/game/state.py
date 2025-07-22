from game.Container import Container

STATE = {
    "inventory": Container()
}

def reset():
    STATE.clear()
    STATE["room"] = "hall"
    STATE["inventory"] = Container()

def has_state(key):
    if key not in STATE:
        return False
    return STATE[key]

def set_state(key, value=True):
    STATE[key] = value

def inventory():
    return STATE["inventory"]

def keep_going():
    return not has_state("escaped") and not has_state("died") and not has_state("quit")
