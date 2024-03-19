from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src_code.db.Database import Base  # Import Base from the correct location

class Supplier(Base):
    __tablename__ = 'suppliers'
    SupplierID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(100))
    ContactName = Column(String(100))
    Email = Column(String(100))
    Phone = Column(String(20))
    Address = Column(String(255))

    wares = relationship("WareSupplier", foreign_keys="[WareSupplier.SupplierID]", back_populates="supplier")
