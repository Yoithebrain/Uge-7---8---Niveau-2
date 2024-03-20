###
# Inherited menu interface
# - CLY 20-03-24 -
###
from blessed import Terminal

class Menu:
    def __init__(self, title, options):
        self.title = title
        self.options = options

    def display(self):
        term = Terminal()
        print(term.clear())
        print(term.center(term.bold(self.title)))
        for key, value in self.options.items():
            print(f"{key}. {value}")
        print(f"{len(self.options) + 1}. Back to Main Menu")

    def get_choice(self):
        term = Terminal()
        with term.location(0, term.height - 1):
            return input(term.bold("Enter your choice: "))