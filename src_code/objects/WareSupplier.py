# waresupplier.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from src_code.db.Database import Base  # Import Base from the correct location
from src_code.objects.Supplier import Supplier

class WareSupplier(Base):
    __tablename__ = 'waresupplier'
    WareID = Column(Integer, ForeignKey('wares.wareId'), primary_key=True)
    SupplierID = Column(Integer, ForeignKey('suppliers.SupplierID'), primary_key=True)
    
    ware = relationship("Ware", back_populates="suppliers", foreign_keys=[WareID])
    supplier = relationship("Supplier", back_populates="wares", foreign_keys=[SupplierID])
