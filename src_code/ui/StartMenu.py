from blessed import Terminal
from WareMenu import WareMenu
from SupplierMenu import SupplierMenu
from CategoriesMenu import CategoriesMenu
from TransactionMenu import TransactionMenu

class StartMenu:
    def __init__(self):
        self.term = Terminal()
        self.options = {
            "1": "Manage Wares",
            "2": "Manage Suppliers",
            "3": "Manage Categories",
            "4": "Manage Transactions",
            "5": "Exit"
        }

    def display(self):
        print(self.term.clear())
        print(self.term.bold_white_center("Warehouse Management System"))
        for key, value in self.options.items():
            print(f"{self.term.green(key)}. {self.term.bold(value)}")

    def get_choice(self):
        with self.term.cbreak():
            val = self.term.inkey()
            if val.code == self.term.KEY_ESCAPE:
                return "5"  # Exit if Escape key is pressed
            return val

    def manage_wares(self):
        wares_menu = WareMenu()
        wares_menu.display()
        wares_menu.get_choice()

    def manage_suppliers(self):
        suppliers_menu = SupplierMenu()
        suppliers_menu.display()
        suppliers_menu.get_choice()

    def manage_categories(self):
        categories_menu = CategoriesMenu()
        categories_menu.display()
        categories_menu.get_choice()

    def manage_transactions(self):
        transactions_menu = TransactionMenu()
        transactions_menu.display()
        transactions_menu.get_choice()
