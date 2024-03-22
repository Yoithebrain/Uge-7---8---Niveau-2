from blessed import Terminal
from src_code.objects.Transaction import Transactions
from datetime import datetime
class TransactionMenu:
    def __init__(self, session):
        self.term = Terminal()
        self.session = session
        self.transactions = Transactions()

        self.options = {
            "1": "Add Transaction",
            "2": "Read Transaction",
            "3": "Update Transaction",
            "4": "Generate Transaction Report",
            "5": "Back to Main Menu"
        }

    def display(self):
        print(self.term.clear())
        print(self.term.center(self.term.bold("Transaction Management")))
        for key, value in self.options.items():
            print(f"{self.term.green(key)}. {self.term.bold(value)}")

    def get_choice(self):
        with self.term.cbreak():
            val = self.term.inkey()
            if val.code == self.term.KEY_ESCAPE:
                return "5"  # Exit if Escape key is pressed
            return val

    def add_transaction(self):
        print(self.term.clear())
        print(self.term.center(self.term.bold("Add Transaction")))
        try:
            ware_id = int(input("Enter Ware ID: "))
            quantity = int(input("Enter Quantity: "))
            transaction_type = input("Enter Transaction Type (IN/OUT): ").upper()
            transaction_date = input("Enter Transaction Date (YYYY-MM-DD HH:MM:SS): ")
            self.transactions.create(self.session, ware_id, quantity, transaction_type, transaction_date)
            print("Transaction added successfully!")
        except ValueError:
            print("Invalid input. Please enter a valid integer for Ware ID and Quantity.")
        input("Press Enter to continue...")

    def read_transaction(self):
        print(self.term.clear())
        print(self.term.center(self.term.bold("Read Transaction")))
        try:
            transaction_id = int(input("Enter Transaction ID: "))
            transaction = self.transactions.read(self.session, transaction_id)
            if transaction:
                print(transaction)
            else:
                print("Transaction not found.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for Transaction ID.")
        input("Press Enter to continue...")

    def update_transaction(self):
        print(self.term.clear())
        print(self.term.center(self.term.bold("Update Transaction")))
        try:
            transaction_id = int(input("Enter Transaction ID to update: "))
            ware_id = int(input("Enter Ware ID (Enter 0 to skip): "))
            quantity = int(input("Enter Quantity (Enter 0 to skip): "))
            transaction_type = input("Enter Transaction Type (IN/OUT) (Enter 0 to skip): ").upper()
            self.transactions.update(self.session, transaction_id, ware_id, transaction_type, quantity)
            print("Transaction updated successfully!")
        except ValueError:
            print("Invalid input. Please enter valid integers for Transaction ID, Ware ID, and Quantity.")
        input("Press Enter to continue...")

    def generate_report(self):
        print(self.term.clear())
        print(self.term.center(self.term.bold("Generate Transaction Report")))

        # Prompt for start date input with error handling
        while True:
            start_date_input = input("Enter Start Date (YYYY-MM-DD): ")
            try:
                start_date = datetime.strptime(start_date_input, "%Y-%m-%d").date()
                break  # Break the loop if input is valid
            except ValueError:
                print("Invalid date format. Please enter date in YYYY-MM-DD format.")

        # Prompt for end date input with error handling
        while True:
            end_date_input = input("Enter End Date (YYYY-MM-DD): ")
            try:
                end_date = datetime.strptime(end_date_input, "%Y-%m-%d").date()
                if end_date < start_date:
                    print("End date cannot be earlier than start date.")
                    continue
                break  # Break the loop if input is valid
            except ValueError:
                print("Invalid date format. Please enter date in YYYY-MM-DD format.")

        transaction_type = input("Enter Transaction Type (IN/OUT): ").upper()
        transactions = self.transactions.report(self.session, start_date, end_date, transaction_type)
        if transactions:
            for transaction in transactions:
                print(transaction)
        else:
            print("No transactions found.")
        input("Press Enter to continue...")

    def start(self):
        while True:
            self.display()
            choice = self.get_choice().lower()
            if choice == "1":
                self.add_transaction()
            elif choice == "2":
                self.read_transaction()
            elif choice == "3":
                self.update_transaction()
            elif choice == "4":
                self.generate_report()
            elif choice == "5":
                break  # Back to Main Menu