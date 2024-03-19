####
# An object representing the Ware inside the Warehouse system
# - CLY 18-03-24 -
####
# imports
from sqlalchemy import Column, Integer, String, Float
from src_code.db.Database import Database
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from src_code.objects.Categories import Category
from src_code.objects.WareSupplier import WareSupplier

# Get Base and Session from Database
db = Database()
Base = db.Base
Session = db.Session

# Class
class Ware(Base):
    __tablename__ = 'wares'
    wareId = Column(Integer, primary_key=True)
    wareName = Column(String)
    wareDescription = Column(String)
    wareQuantity = Column(Integer)
    warePrice = Column(Float)
    wareCategoryId = Column(Integer, ForeignKey('categories.CategoryID'))
    wareSupplierId = Column(Integer, ForeignKey('waresupplier.WareID'))
    
    # Relationship
    category = relationship(Category, back_populates="wares")
    suppliers = relationship("WareSupplier", foreign_keys="[WareSupplier.WareID]", back_populates="ware")
    
    def __repr__(self):
         return f"<Ware(id='{self.wareId}', name='{self.wareName}', description='{self.wareDescription}', quantity={self.wareQuantity}, price={self.warePrice}, category_id={self.wareCategoryId})>"

    @classmethod
    def add(cls, name, description, quantity, price, category_id, supplier_id):
        session = None
        try:
            session = Session()
            print("MY SESSION: ", session)
            new_ware = cls(
                wareName=name,
                wareDescription=description,
                wareQuantity=quantity,
                warePrice=price,
                wareCategoryId=category_id,
                wareSupplierId=supplier_id
            )
            session.add(new_ware)
            session.commit()
            print("Ware added successfully!")
        except Exception as e:
            print(f"Error adding ware: {e}")
            if session:
                session.rollback()  # Rollback the transaction in case of an error
        finally:
            if session:
                session.close()
    @classmethod
    def update(cls, ware_id, name=None, description=None, quantity=None, price=None, category_id=None, supplier_id=None):
        session = None
        try:
            session = Session()
            ware = session.query(cls).filter_by(wareId=ware_id).first()
            if not ware:
                print(f"Ware with id {ware_id} not found.")
                return

            if name:
                ware.wareName = name
            if description:
                ware.wareDescription = description
            if quantity is not None:
                ware.wareQuantity = quantity
            if price is not None:
                ware.warePrice = price
            if category_id:
                ware.wareCategoryId = category_id
            if supplier_id:
                ware.wareSupplierId = supplier_id

            session.commit()
            print(f"Ware with id {ware_id} updated successfully!")
        except Exception as e:
            print(f"Error updating ware: {e}")
            if session:
                session.rollback()
        finally:
            if session:
                session.close()

    @classmethod
    def get(cls, ware_id):
        session = None
        try:
            session = Session()
            ware = session.query(cls).filter_by(wareId=ware_id).first()
            if ware:
                return ware
            else:
                print(f"Ware with ID {ware_id} not found.")
        except Exception as e:
            print(f"Error retrieving ware: {e}")
        finally:
            if session:
                session.close()

    @classmethod
    def get_all(cls):
        session = None
        try:
            session = Session()
            wares = session.query(cls).all()
            return wares
        except Exception as e:
            print(f"Error retrieving all wares: {e}")
        finally:
            if session:
                session.close()
    
    @classmethod
    def search(cls, column_name, search_term):
        session = None
        try:
            session = Session()
            # Get the attribute corresponding to the column name
            column_attribute = getattr(cls, column_name)
            # Filter the query based on the specified column and search term
            query = session.query(cls).filter(column_attribute.ilike(f"%{search_term}%"))
            results = query.all()
            return results
        except Exception as e:
            print(f"Error searching for wares: {e}")
        finally:
            if session:
                session.close()
    @classmethod
    def getsession(cls):
        return Session

# Example usage:
if __name__ == "__main__":
    # Connect to the database
    db.connect()

    # Add a new ware
    Ware.add(name='Product A', description='Description of Product A', quantity=100, price=50, category_id=1, supplier_id=1)

    # Update an existing ware
    Ware.update(ware_id=1, quantity=150)

    # Get a ware by ID
    ware = Ware.get(1)
    print(ware)

    # Get all wares
    wares = Ware.get_all()
    for w in wares:
        print(w)

    # Search for wares based on a column and search term
    search_results = Ware.search('wareName', 'Product')
    for result in search_results:
        print(result)

    # Close the database connection
    db.close()
