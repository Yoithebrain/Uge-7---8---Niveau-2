from blessed import Terminal

class CategoriesMenu:
    def __init__(self):
        self.term = Terminal()
        self.options = {
            "1": "View Categories",
            "2": "Add Category",
            "3": "Update Category",
            "4": "Delete Category",
            "5": "Back to Main Menu"
        }

    def display(self):
        print(self.term.clear())
        print(self.term.bold_white_center("Category Management"))
        for key, value in self.options.items():
            print(f"{self.term.green(key)}. {self.term.bold(value)}")

    def get_choice(self):
        with self.term.cbreak():
            val = self.term.inkey()
            if val.code == self.term.KEY_ESCAPE:
                return "5"  # Exit if Escape key is pressed
            return val