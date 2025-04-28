from state import has_state, set_state, has_item, add_item
from action_parser import is_synonym_of, starts_with_synonym
from map import has_visited, describe_map

def library_action(action):
    if (action == "" and not has_visited("library")) or action == "look":
        set_state("visited_library")
        print("You are in a dimly-lit library.")
        print("Every wall is shelved and there are hundreds of books here.")
        print("At least they look to be in alphabetical order if you knew what to look for.")
        describe_map()

    elif action == "":
        print("You are in the library.")

    elif is_synonym_of(action, "find", "earthsea") or is_synonym_of(action, "read", "earthsea"):
        print("You find the copy of Earthsea on the shelves.")
        if has_item("key"):
            print("You open the book to find it is hollow in the middle, now empty.")
        else:
            print("You open the book to find it is hollow in the middle, and containing a key.")
        set_state("book_found")

    elif starts_with_synonym(action, "find") or starts_with_synonym(action, "read"):
        print("There are hundreds of books here, but not that one.")

    elif is_synonym_of(action, "take", "key"):
        if has_state("book_found"):
            print("You take the key.")
            add_item("key")
        else:
            print("What key?")

    else:
        print("I don't think that will help")
