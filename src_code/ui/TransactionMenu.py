from blessed import Terminal

class TransactionMenu():
    def __init__(self):
        self.term = Terminal()
        self.options = {
            "1": "Add Transaction",
            "2": "Read Transaction",
            "3": "Update Transaction",
            "4": "Delete Transaction",
            "5": "Generate Transaction Report"
        }
        #super().__init__("Transaction Management", options)


    def display(self):
        print(self.term.clear())
        print(self.term.center(self.term.bold(("Transaction management"))))
        for key, value in self.options.items():
            print(f"{self.term.green(key)}. {self.term.bold(value)}")

    def get_choice(self):
        with self.term.cbreak():
            val = self.term.inkey()
            if val.code == self.term.KEY_ESCAPE:
                return "5"  # Exit if Escape key is pressed
            return val