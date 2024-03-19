# src_code/run_ware.py

# Import the Ware object
from src_code.objects.Ware import Ware

def main():
    # Example usage
    # Create a new ware
    #new_ware = Ware(wareName='Product A', wareDescription='Description of Product A', wareQuantity=100, warePrice=50, wareCategoryId=1, wareSupplierId=1)
    #my_session = new_ware.getsession()
    #print("MY SEESION: ", my_session)
    
    new_ware = Ware(wareName='Product A', wareDescription='Description of Product A', wareQuantity=100, warePrice=50, wareCategoryId=1, wareSupplierId=1)
    new_ware.add(new_ware.wareName, new_ware.wareDescription, new_ware.wareQuantity, new_ware.warePrice, new_ware.wareCategoryId, new_ware.wareSupplierId)

    # Update the quantity of an existing ware
    Ware.update(ware_id=1, quantity=150)

    # Retrieve a ware by its ID
    retrieved_ware = Ware.get(1)
    print("Retrieved Ware:", retrieved_ware)

    # Retrieve all wares
    all_wares = Ware.get_all()
    print("All Wares:")
    for ware in all_wares:
        print(ware)

if __name__ == "__main__":
    main()
