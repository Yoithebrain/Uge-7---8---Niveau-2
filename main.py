# src_code/run_ware.py

# Import the Ware object
from src_code.objects.Ware import Ware
from src_code.objects.Categories import Category
from src_code.objects.Transaction import Transaction
from src_code.db.Database import Database

def main():
    db = Database()
    session = db.Session()
    # Example usage
    # Create a new ware
    #new_ware = Ware(wareName='Product A', wareDescription='Description of Product A', wareQuantity=100, warePrice=50, wareCategoryId=1, wareSupplierId=1)
    #my_session = new_ware.getsession()
    #print("MY SEESION: ", my_session)
    
    #new_ware = Ware(wareName='Product A', wareDescription='Description of Product A', wareQuantity=100, warePrice=50, wareCategoryId=1, wareSupplierId=1)
    #new_ware.add(new_ware.wareName, new_ware.wareDescription, new_ware.wareQuantity, new_ware.warePrice, new_ware.wareCategoryId, new_ware.wareSupplierId)

    # Update the quantity of an existing ware
    #Ware.update(ware_id=1, quantity=150)

    # Add a new ware
    Ware.add(session, name='Product A', description='Description of Product A', quantity=100, price=50, category_id=1, supplier_id=1)

    # Update an existing ware
    Ware.update(session, ware_id=1, quantity=150)

    # Get a ware by ID
    ware = Ware.get(session, 1)
    print(ware)

    # Get all wares
    wares = Ware.get_all(session)
    for w in wares:
        print(w)

    # Search for wares based on a column and search term
    search_results = Ware.search(session, 'wareName', 'Product')
    for result in search_results:
        print(result)


   # Adding a new category
    Category.add(session, name='Category A', description='Description of Category A')
    
    # Reading a category
    category = Category.read(session, 1)
    print(category)
    
    # Updating a category
    Category.update(session, category_id=1, name='Updated Category A')

    # Create a new transaction
    new_transaction = Transaction.create(session, ware_id=1, quantity=10, transaction_type='IN', transaction_date='2024-03-18')
    print("New Transaction:", new_transaction)

    # Retrieve a transaction by its ID
    retrieved_transaction = Transaction.read(session, 1)
    print("Retrieved Transaction:", retrieved_transaction)

    # Update a transaction
    Transaction.update(session, 1, quantity=20)
    updated_transaction = Transaction.read(session, 1)
    print("Updated Transaction:", updated_transaction)

    # Delete a transaction
    #Transaction.delete(session, 1)

    # Report transactions within a date range
    transactions_report = Transaction.report(session, start_date='2024-03-01', end_date='2024-03-31', transaction_type='IN')
    print("Transactions Report:")
    for transaction in transactions_report:
        print(transaction)

    # Don't forget to close the session when you're done
    session.close()

if __name__ == "__main__":
    main()
