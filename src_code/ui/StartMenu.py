from blessed import Terminal
from .WareMenu import WareMenu
from .SupplierMenu import SupplierMenu
from .CategoriesMenu import CategoriesMenu
from .TransactionMenu import TransactionMenu

class StartMenu:
    def __init__(self, session):
        self.term = Terminal()
        self.options = {
            "1": "Manage Wares",
            "2": "Manage Suppliers",
            "3": "Manage Categories",
            "4": "Manage Transactions",
            "5": "Exit"
        }
        self.session = session

    def display(self):
        print(self.term.clear())
        print(self.term.center(self.term.bold("Warehouse Management System")))
        for key, value in self.options.items():
            print(f"{self.term.green(key)}. {self.term.bold(value)}")

    def get_choice(self):
        with self.term.cbreak():
            val = self.term.inkey()
            if val.code == self.term.KEY_ESCAPE:
                return "5"  # Exit if Escape key is pressed
            return val

    def manage_wares(self):
        wares_menu = WareMenu(self.session)
        wares_menu.start()
            #choice = wares_menu.get_choice()
            #if choice == "5":
                #break
                #return choice  # Return to start menu
            # Handle other menu options

    def manage_suppliers(self):
        suppliers_menu = SupplierMenu()
        while True:
            suppliers_menu.display()
            choice = suppliers_menu.get_choice()
            if choice == "5":
                break  # Return to start menu
            # Handle other menu options

    def manage_categories(self):
        categories_menu = CategoriesMenu()
        while True:
            categories_menu.display()
            choice = categories_menu.get_choice()
            if choice == "5":
                break  # Return to start menu
            # Handle other menu options

    def manage_transactions(self):
        # Init the transactions menu
        transactions_menu = TransactionMenu(self.session)
        # Starts the menu, this will run until you go back. Then the menu will comeback to this object.
        transactions_menu.start()
        '''
        while True:
            transactions_menu.display()
            choice = transactions_menu.get_choice()
            if choice == "5":
                break  # Return to start menu
            # Handle other menu options
        '''
    def start(self):
        while True:
            self.display()
            choice = self.get_choice()
            if choice == "5":
                break  # Exit the program
            elif choice == "1":
                self.manage_wares()
            elif choice == "2":
                self.manage_suppliers()
            elif choice == "3":
                self.manage_categories()
            elif choice == "4":
                self.manage_transactions()