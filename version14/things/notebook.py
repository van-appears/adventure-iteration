from things.thing import Thing

class Notebook(Thing):
    def __init__(self):
        super().__init__(key="notebook", carryable=True)

    def long_description(self):
        print("The notebook is empty, except for an instruction written on the first page.")
        print("On the page is written 'Read Earthsea'.")

    def perform_action(self, action):
        verb, _ = action
        if verb == "read":
            print("The notebook is empty, except for an instruction written on the first page.")
            print("On the page is written 'Read Earthsea'.")
            return True

        return False
