from Menu import Menu

class TransactionMenu(Menu):
    def __init__(self):
        options = {
            "1": "Add Transaction",
            "2": "Read Transaction",
            "3": "Update Transaction",
            "4": "Delete Transaction",
            "5": "Generate Transaction Report"
        }
        super().__init__("Transaction Management", options)