####
# An object representing the transactions of our wares inside the Warehouse system
# - CLY 18-03-24 -
####

# Imports

# Globals

# Class
class Transaction:
    # Methods
    def __init__(self, id, ware_id, quantity, transaction_type, timestamp):
        self.id = id
        self.ware_id = ware_id
        self.quantity = quantity
        self.transaction_type = transaction_type
        self.timestamp = timestamp

    @classmethod
    def create(cls, ware_id, quantity, transaction_type, timestamp):
        pass

    @classmethod
    def read(cls, transaction_id):
        pass

    @classmethod
    def update(cls, transaction_id, ware_id=None, quantity=None, transaction_type=None, timestamp=None):
        pass

    @classmethod
    def delete(cls, transaction_id):
        pass

    @classmethod
    def report(cls, start_date=None, end_date=None, transaction_type=None):
        pass

# Example usage:
# transactions = Transaction.report(start_date='2024-03-01', end_date='2024-03-31', transaction_type='IN')
# for transaction in transactions:
#     print(transaction)