from os import system
from hall import hall_action
from kitchen import kitchen_action
from office import office_action
from library import library_action

from state import reset, has_state, set_state, print_inventory
from action_parser import is_synonym_of, starts_with_synonym
from map import move, move_to

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
    hall_action("")
    print("How will you get out?")

    while not has_state("escaped") and not has_state("died") and not has_state("quit"):
        action = input("> ").strip().lower()
        moving = None

        if starts_with_synonym(action, "move to"):
            moving = move_to(action)
            action = ""
        elif starts_with_synonym(action, "move"):
            moving = move(action)
            action = ""

        if moving is False:
            pass
        elif action == "instructions":
            print_instructions()
        elif action == "inventory":
            print_inventory()
        elif action == "quit":
            set_state("quit")
        elif has_state("room") == "hall":
            hall_action(action)
        elif has_state("room") == "kitchen":
            kitchen_action(action)
        elif has_state("room") == "office":
            office_action(action)
        elif has_state("room") == "library":
            library_action(action)

    if has_state("escaped"):
        print("You open the door and walk out into the sunshine. Well done!")
        print("Game over")
        return True

    if has_state("died"):
        print("You are very very dead. Bad luck!")
        print("Game over")
        return True

    return False

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
