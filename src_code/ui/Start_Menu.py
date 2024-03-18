from blessed import Terminal

class StartMenu:
    def __init__(self):
        self.term = Terminal()
        self.options = ["View Categories", "View Transactions", "View Wares", "Exit"]
        self.selected_option = 0

    def display(self):
        with self.term.fullscreen(), self.term.cbreak(), self.term.hidden_cursor():
            while True:
                print(self.term.clear())  # Clear the screen
                #print(self.term.on_green())
                for i, option in enumerate(self.options):
                    if i == self.selected_option:
                        # Set selected option color to white on green background
                        print(self.term.white_on_green(self.term.reverse(option)))
                    elif option == "Exit":
                        # Set "Exit" option color to white on red background
                        print(self.term.white_on_red(option))
                    else:
                        # Set other options color to white on default background
                        print(self.term.white(option))
                
                key = self.term.inkey()
                if key.name == "q" or key.name == "Q":
                    break
                elif key.name == "KEY_DOWN" and self.selected_option < len(self.options) - 1:
                    self.selected_option += 1
                elif key.name == "KEY_UP" and self.selected_option > 0:
                    self.selected_option -= 1
                elif key.name == "KEY_ENTER" or key.code == self.term.KEY_ENTER:
                    self.execute_selected_option()

    def execute_selected_option(self):
        if self.selected_option == 0:
            self.view_categories()
        elif self.selected_option == 1:
            self.view_transactions()
        elif self.selected_option == 2:
            self.view_wares()
        elif self.selected_option == 3:
            self.exit()

    def view_categories(self):
        print("Viewing categories...")
        # Implement your view_categories function here

    def view_transactions(self):
        print("Viewing transactions...")
        # Implement your view_transactions function here

    def view_wares(self):
        print("Viewing wares...")
        # Implement your view_wares function here

    def exit(self):
        print("Exiting...")
        exit()
        # Implement your exit function here
        # You may want to add cleanup code or other operations before exiting