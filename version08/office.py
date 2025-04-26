from state import has_state, set_state, has_item, add_item
from action_parser import is_synonym_of
from map import has_visited, describe_map

def office_action(action):
    if (action == "" and not has_visited("office")) or action == "look":
        set_state("visited_office")
        print("You are in a lovely wood-panelled office. There is a large wooden chest in the corner.")
        describe_map()

    elif action == "":
        print("You are in the office.")

    elif is_synonym_of(action, "take", "key"):
        if has_item("key"):
            print("You already have the key")
        elif has_state("chest_open"):
            print("You have taken the key")
            add_item("key")
        elif has_state("chest_opened"):
            print("You can't take the key, you closed the chest")
        else:
            print("What key?")

    elif is_synonym_of(action, "take", "chest"):
        print("The chest is far too heavy")

    elif is_synonym_of(action, "open", "chest"):
        if has_state("chest_open"):
            print("The chest is already open")
        else:
            print("You have opened the chest.")
            print("There is a key inside!")
            set_state("chest_open")
            set_state("chest_opened")

    elif is_synonym_of(action, "close", "chest"):
        if has_state("chest_open"):
            print("You have closed the chest")
            set_state("chest_open", False)
        else:
            print("The chest is already closed")

    else:
        print("I don't think that will help")
