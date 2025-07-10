from os import system
from game.state import reset, has_state, set_state, keep_going, inventory
from game.action_parser import parse_action
from game.map import move, move_to, current_location, describe_map

def print_instructions():
    print("INSTRUCTIONS")
    print("To perform an action use 'verb noun' e.g. 'take item', 'open door'.")
    print("To move use 'go' or 'walk' with a direction e.g. 'go north'.")
    print("To move to a location you have visited before use 'go to' e.g. 'go to hall'.")
    print("To see a room description again use command 'look'")
    print("To see what you are carrying use command 'inventory'.")
    print("To exit the game use command 'quit'.")
    print("To see these instuctions again use command 'instructions'.")

def main():
    current_location().long_description()
    current_location().visit()
    print("How will you get out?")



    while keep_going():
        action = parse_action(input("> "))
        verb, noun = action

        if verb == "move to":
            if move_to(noun):
                current_location().short_description()
                current_location().visit()

        elif verb == "move":
            if move(noun):
                if current_location().was_visited():
                    current_location().short_description()
                else:
                    current_location().long_description()
                    current_location().print_items()
                    describe_map()
                current_location().visit()

        elif verb == "describe":
            current_location().long_description()
            current_location().print_items()
            describe_map()

        elif verb == "instructions":
            print_instructions()

        elif verb == "inventory":
            print_inventory()

        elif verb == "quit":
            set_state("quit")

        elif verb == None:
            print("I don't understand.")

        else:
            current_location().perform_action(action)

    if has_state("escaped"):
        print("You open the door and walk out into the sunshine. Well done!")
        print("Game over")
        return True

    if has_state("died"):
        print("You are very very dead. Bad luck!")
        print("Game over")
        return True

    return False

def print_inventory():
    keys = inventory().item_keys()
    if len(keys) == 0:
        print("You aren't carrying anything.")
    else:
        print(f"You are carrying: {', '.join(keys)}")

def game():
    system("clear||cls")
    print_instructions()
    print("")
    playing = True
    while playing:
        reset()
        game_over = main()
        if game_over:
            print("")
            replay = input("Do you want to play again? yes or no? ").strip().lower()
            if replay.startswith("no"):
                playing = False
            elif not replay.startswith("yes"):
                print("I'll take that as 'no'.")
                playing = False
            else:
                system("clear||cls")
        else:
            playing = False

    print("Goodbye!")

if __name__ == "__main__":
    game()
