from blessed import Terminal

class SupplierMenu:
    def __init__(self):
        self.term = Terminal()
        self.options = {
            "1": "View Suppliers",
            "2": "Add Supplier",
            "3": "Update Supplier",
            "4": "Delete Supplier"
        }

    def display(self):
        print(self.term.clear())
        print(self.term.center(self.term.bold(("Supplier Management"))))
        for key, value in self.options.items():
            print(f"{self.term.green(key)}. {self.term.bold(value)}")

    def get_choice(self):
        with self.term.cbreak():
            val = self.term.inkey()
            if val.code == self.term.KEY_ESCAPE:
                return "5"  # Exit if Escape key is pressed
            return val
