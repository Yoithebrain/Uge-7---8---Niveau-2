####
# An object representing the Ware inside the Warehouse system
# - CLY 18-03-24 -
####
# imports
from sqlalchemy import Column, Integer, String, Float
from src_code.db.Database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from src_code.objects.Categories import Category
from src_code.objects.WareSupplier import WareSupplier


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
    transactions = relationship("Transaction", back_populates="ware")

    
    def as_dict(self):
        return {
            'wareId': self.wareId,
            'wareName': self.wareName,
            'wareDescription': self.wareDescription,
            'wareQuantity': self.wareQuantity,
            'warePrice': self.warePrice,
            'wareCategoryId': self.wareCategoryId,
            'wareSupplierId': self.wareSupplierId
        }

    def __repr__(self):
        return str(self.as_dict())

    @classmethod
    def add(cls, session, name, description, quantity, price, category_id, supplier_id):
        try:
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
            session.rollback()

    @classmethod
    def update(cls, session, ware_id, name=None, description=None, quantity=None, price=None, category_id=None, supplier_id=None):
        try:
            ware = session.query(cls).filter_by(wareId=ware_id).first()
            if ware:
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
            else:
                print(f"Ware with id {ware_id} not found.")
        except Exception as e:
            print(f"Error updating ware: {e}")
            session.rollback()

    @classmethod
    def get(cls, session, ware_id):
        try:
            ware = session.query(cls).filter_by(wareId=ware_id).first()
            if ware:
                return ware
            else:
                print(f"Ware with ID {ware_id} not found.")
        except Exception as e:
            print(f"Error retrieving ware: {e}")

    @classmethod
    def get_all(cls, session):
        try:
            wares = session.query(cls).all()
            return wares
        except Exception as e:
            print(f"Error retrieving all wares: {e}")
    
    @classmethod
    def search(cls, session, column_name, search_term):
        try:
            # Get the attribute corresponding to the column name
            column_attribute = getattr(cls, column_name)
            # Filter the query based on the specified column and search term
            query = session.query(cls).filter(column_attribute.ilike(f"%{search_term}%"))
            results = query.all()
            return results
        except Exception as e:
            print(f"Error searching for wares: {e}")