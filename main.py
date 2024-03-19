# src_code/run_ware.py

# Import the Ware object
from src_code.objects.Ware import Ware
from src_code.objects.Categories import Category
from src_code.objects.Transaction import Transaction
def main():
    # Example usage
    # Create a new ware
    #new_ware = Ware(wareName='Product A', wareDescription='Description of Product A', wareQuantity=100, warePrice=50, wareCategoryId=1, wareSupplierId=1)
    #my_session = new_ware.getsession()
    #print("MY SEESION: ", my_session)
    
    #new_ware = Ware(wareName='Product A', wareDescription='Description of Product A', wareQuantity=100, warePrice=50, wareCategoryId=1, wareSupplierId=1)
    #new_ware.add(new_ware.wareName, new_ware.wareDescription, new_ware.wareQuantity, new_ware.warePrice, new_ware.wareCategoryId, new_ware.wareSupplierId)

    # Update the quantity of an existing ware
    #Ware.update(ware_id=1, quantity=150)

    # Retrieve a ware by its ID
    retrieved_ware = Ware.get(1)
    print("Retrieved Ware:", retrieved_ware)

    # Retrieve all wares
    #print("All Wares:")
    #for ware in all_wares:
    #    print(ware)
    # Read a category by its ID
    retrieved_category = Category.read(1)
    print("Retrieved Category:", retrieved_category)

    # Update a category's name and description
    Category.update(category_id=1, name='Updated Category A', description='Updated description')

    # Create a new transaction
    new_transaction = Transaction.create(ware_id=1, quantity=10, transaction_type='IN', transaction_date='2024-03-18')
    print("New Transaction:", new_transaction)
    
    # Retrieve a transaction by its ID
    retrieved_transaction = Transaction.read(1)
    print("Retrieved Transaction:", retrieved_transaction)

    # Update a transaction
    Transaction.update(transaction_id=1, quantity=20)
    updated_transaction = Transaction.read(1)
    print("Updated Transaction:", updated_transaction)

    # Delete a transaction
    Transaction.delete(transaction_id=1)

    # Report transactions within a date range
    transactions_report = Transaction.report(start_date='2024-03-01', end_date='2024-03-31', transaction_type='IN')
    print("Transactions Report:")
    for transaction in transactions_report:
        print(transaction)
if __name__ == "__main__":
    main()
