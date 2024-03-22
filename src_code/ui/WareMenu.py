###
# The menu that manages wares
# - CLY 20-03-24 -
###

from blessed import Terminal
from src_code.objects.Ware import Ware
class WareMenu:
    def __init__(self, session):
        self.term = Terminal()
        self.options = {
            "1": "Add Ware",
            "2": "Update Ware",
            "3": "Get Ware",
            "4": "Search Ware",
            "5": "Exit"
        }
        self.session = session  # Assuming you have a session object initialized
        self.ware = Ware() # Initalize ware object

    def display(self):
        print(self.term.clear())
        print(self.term.center(self.term.bold(("Ware Management"))))
        for key, value in self.options.items():
            print(f"{self.term.green(key)}. {self.term.bold(value)}")
        #print(self.session)
    def get_choice(self):
        with self.term.cbreak():
            val = self.term.inkey()
            if val.code == self.term.KEY_ESCAPE:
                return "5"  # Exit if Escape key is pressed
            return val

    def add_ware(self):
        if self.ware:
            name = input("Enter ware name: ")
            description = input("Enter ware description: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            category_id = int(input("Enter category ID: "))
            #supplier_id = int(input("Enter supplier ID: "))
            #print(self.ware)
            self.ware.add(session = self.session, name=str(name), description=str(description), quantity=int(quantity), price=int(price), category_id=int(category_id))
            print("Ware added successfully!")
        else:
            print("Error: Ware object is not initialized properly.")
        input("Press Enter to continue...")


    def update_ware(self):
        ware_id = int(input("Enter ware ID to update: "))
        # Assuming you want to update all attributes, you can modify this accordingly
        name = input("Enter new ware name: ")
        description = input("Enter new ware description: ")
        quantity = int(input("Enter new quantity: "))
        price = float(input("Enter new price: "))
        category_id = int(input("Enter new category ID: "))
        #supplier_id = int(input("Enter new supplier ID: "))
        Ware.update(self.session, ware_id, name, description, quantity, price, category_id)
        input("Press Enter to continue...")

    def get_ware(self):
        ware_id = int(input("Enter ware ID to get: "))
        ware = self.ware.get(self.session, ware_id)
        print(ware)
        input("Press Enter to continue...")

    def search_ware(self):
        column_name = input("Enter column name to search: ")
        search_term = input("Enter search term: ")
        results = Ware.search(self.session, column_name, search_term)
        print(results)
        input("Press Enter to continue...")

    def exit_menu(self):
        self.session.close()
    
    def start(self):
        while True:
            self.display()
            choice = self.get_choice()

            if choice == "1":
                self.add_ware()
            elif choice == "2":
                self.update_ware()
            elif choice == "3":
                self.get_ware()
            elif choice == "4":
                self.search_ware()
            elif choice == "5":
                self.exit_menu()
                break
            else:
                print("Invalid choice. Please select a valid option.")