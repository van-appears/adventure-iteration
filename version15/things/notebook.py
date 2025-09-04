from base.state import has_state
from things.thing import Thing

class Notebook(Thing):
    def __init__(self):
        super().__init__(key="notebook", carryable=True)

    def long_description(self):
        book = has_state("book")
        print("The notebook is empty, except for an instruction written on the first page.")
        print(f"On the page is written 'Read {book}'.")

    def perform_action(self, action):
        verb, _ = action
        if verb == "read":
            book = has_state("book")
            print("The notebook is empty, except for an instruction written on the first page.")
            print(f"On the page is written 'Read {book}'.")
            return True

        return False
