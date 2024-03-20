###
# The menu that manages wares
# - CLY 20-03-24 -
###

from blessed import Terminal

class WareMenu():
    def __init__(self):
        self.term = Terminal()
        self.options = {
            "1": "Add Ware",
            "2": "Update Ware",
            "3": "Get Ware"
        }
        #super().__init__("Ware Management", options)

    def display(self):
        print(self.term.clear())
        print(self.term.center(self.term.bold(("Ware Management"))))
        for key, value in self.options.items():
            print(f"{self.term.green(key)}. {self.term.bold(value)}")

    def get_choice(self):
        with self.term.cbreak():
            val = self.term.inkey()
            if val.code == self.term.KEY_ESCAPE:
                return "5"  # Exit if Escape key is pressed
            return val