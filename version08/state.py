STATE = {}

def reset():
    STATE.clear()
    STATE["room"] = "hall"
    STATE["inventory"] = set()

def has_state(key):
    if key not in STATE:
        return False
    return STATE[key]

def set_state(key, value=True):
    STATE[key] = value

def print_inventory():
    if len(STATE["inventory"]) == 0:
        print("You aren't carrying anything")
    else:
        print(f"You are carrying: {', '.join(STATE["inventory"])}")

def has_item(item):
    return item in STATE["inventory"]

def add_item(item):
    STATE["inventory"].add(item)

def debug():
    print(STATE)
