from base.state import inventory, has_state, set_state
from locations.location import Location
from things.book import Book
from things.kitchen_cupboard_key import KitchenCupboardKey

class Library(Location):
    def visit(self):
        self.visited = True
        if has_state("library_fire_4"):
            print("The smoke and fire overwhelms you")
            set_state("died")

    def short_description(self):
        print("You are in the library.")

    def long_description(self):
        if has_state("library_fire_1") or has_state("library_fire_2") or has_state("library_fire_3"):
            print("You are in the library and the library is on fire!")
            print("Get out!")
        else:
            print("You are in a darkened library.")
            print("There is no window and the light does not work.")
            print("Every wall is shelved and there appear to be hundreds of dusty books here.")
            print("Maybe there is something here if you knew what to look for and could see it.")

    def perform_action(self, action):
        verb, noun = action

        if verb == "read":
            if not has_state("candle_lit"):
                print("You can't see well enough to read anything.")
                return True

            book_name = has_state("book_name")
            book_key = has_state("book_key")
            if noun == book_key:
                self.ensure_book_present(True)
                if not inventory().has_direct_item_with_key(book_key):
                    print(f"You find the copy of {book_name} on the shelves.")
                if inventory().has_direct_item_with_key("small key"):
                    print("You open the book to find it is hollow in the middle, now empty.")
                else:
                    print("You open the book to find it is hollow in the middle, and containing a key.")

                return True

        return False

    def take_item(self, noun_key):
        book_name = has_state("book_name")
        book_key = has_state("book_key")
        if noun_key == book_key and not inventory().has_direct_item_with_key(book_key) and not self.has_direct_item_with_key(book_key) and has_state("candle_lit"):
            print(f"You find the copy of {book_name} on the shelves.")
            self.ensure_book_present()

        if super().take_item(noun_key) and noun_key == "key":
            print("As you are trying to take the key while also holding a book and a candle, you drop the latter and accidentally set fire to the shelf!")
            set_state("library_fire_1")

    def ensure_book_present(self, include_key=False):
        book_key = has_state("book_key")
        if not inventory().has_direct_item_with_key(book_key) and not self.has_direct_item_with_key(book_key):
            book_item = Book(book_key)
            self.add_item(book_item)
            if include_key:
                book_item.add_item(KitchenCupboardKey())
