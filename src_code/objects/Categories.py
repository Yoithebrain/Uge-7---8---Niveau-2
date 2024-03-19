####
# An object representing the category of our wares inside the Warehouse system
# - CLY 18-03-24 -
####
# Imports
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src_code.db.Database import Base  # Assuming Base is defined in your Database module

# Globals

# Class
class Category(Base):
    __tablename__ = 'categories'
    CategoryID = Column(Integer, primary_key=True)
    Name = Column(String)
    Description = Column(String)

    # Define the relationship
    wares = relationship("Ware", back_populates="category")

    @classmethod
    def create(cls, name, description):
        pass

    @classmethod
    def read(cls, category_id):
        pass

    @classmethod
    def update(cls, category_id, name=None, description=None):
        pass

    @classmethod
    def delete(cls, category_id):
        pass


# Example usage - Debug code:
# category = Category.create(name='Category A', description='Description of Category A')
# category = Category.read(1)
# category.update(name='Updated Category A')
