from os import system
from base.state import reset_state, has_state, set_state, keep_going, inventory, next_state, get_action_method
from base.action_parser import input_action, parse_action
from base.map import reset_map, move, move_to, current_location, describe_map

def print_instructions():
    print("INSTRUCTIONS")
    print("To perform an action use 'verb noun' e.g. 'take item', 'open door'.")
    print("To move use 'go' or 'walk' with a direction e.g. 'go north'.")
    print("To move to a location you have visited before use 'go to' e.g. 'go to hall'.")
    print("To see more information on a room or item use command 'describe' or 'describe item'")
    print("To see what you are carrying use command 'inventory'.")
    print("To exit the game use command 'quit'.")
    print("To see these instructions again use command 'instructions'.")

def main():
    next_action = get_action_method()
    current_location().long_description()
    describe_map()

    print()
    print("How will you get out?")

    while keep_going():
        action = parse_action(next_action())
        verb, noun = action

        if verb is None:
            print("I don't understand.")

        elif verb == "move to":
            if move_to(noun):
                current_location().short_description()

        elif verb == "move":
            if move(noun):
                if current_location().was_visited():
                    current_location().short_description()
                else:
                    current_location().long_description()
                    describe_map()
                    current_location().print_items()

        elif verb == "describe":
            describe(noun)

        elif verb == "instructions":
            print_instructions()

        elif verb == "inventory":
            print_inventory()

        elif verb == "quit":
            set_state("quit")

        elif verb == "take":
            current_location().take_item(noun)

        else:
            perform_action(action)

        if keep_going():
            next_state()
            current_location().visit()

    if has_state("escaped"):
        print("Well done!")
        return True

    if has_state("died"):
        print("You are very very dead. Bad luck!")
        print("Game over")
        return True

    return False

def describe(noun):
    if noun is None:
        current_location().long_description()
        describe_map()
        current_location().print_items()
        return

    inv_items = inventory().find_items_with_key(noun)
    if len(inv_items) > 1:
        print(f"Your inventory contains {len(inv_items)} like that: {item_keys(inv_items)}")
    elif len(inv_items) == 1:
        print(f"Your inventory includes: {inv_items[0][1].keys[0]}")
        inv_items[0][1].long_description()

    loc_items = current_location().find_items_with_key(noun)
    if len(loc_items) > 1:
        print(f"There are {len(loc_items)} like that here: {item_keys(loc_items)}")
    elif len(loc_items) == 1:
        print(f"Here there is: {loc_items[0][1].keys[0]}")
        loc_items[0][1].long_description()

    if len(inv_items) == 0 and len(loc_items) == 0:
        print("There isn't one of these here.")

def item_keys(items):
    item_keys = []
    for item in items:
        item_keys.append(item.keys[0])
    return item_keys

def perform_action(action):
    _, noun = action
    actioned = current_location().perform_action(action)
    if not actioned:
        for item in current_location().items:
            if noun in item.keys:
                actioned = item.perform_action(action)
    if not actioned:
        for item in inventory().items:
            if noun in item.keys:
                actioned = item.perform_action(action)
    if not actioned:
        print("I don't understand that.")

def print_inventory():
    keys = inventory().item_keys()
    if len(keys) == 0:
        print("You aren't carrying anything.")
    else:
        print(f"You are carrying: {', '.join(keys)}")

def yes_no_question(message):
    answer = input(f"{message} yes or no? ").strip().lower()
    if answer in ("y", "yes"):
        return True

    if answer in ("n", "no"):
        return False

    print("I'll take that as 'no'.")
    return False

def game():
    system("clear||cls")
    set_state("__GET_ACTION", input_action)
    if yes_no_question("Do you want to see instructions?"):
        print_instructions()

    print("")
    playing = True
    while playing:
        reset_state()
        reset_map()

        game_over = main()
        if game_over:
            print("")
            playing = yes_no_question("Do you want to play again?")
            if playing:
                system("clear||cls")
        else:
            playing = False

    print("Goodbye!")

if __name__ == "__main__":
    game()
