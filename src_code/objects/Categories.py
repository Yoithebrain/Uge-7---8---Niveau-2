####
# An object representing the category of our wares inside the Warehouse system
# - CLY 18-03-24 -
####
# Imports
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src_code.db.Database import Database  # Assuming Base is defined in your Database module
# Get Base and Session from Database
db = Database()
Base = db.Base
Session = db.Session
# Globals

# Class
class Category(Base):
    __tablename__ = 'categories'
    CategoryID = Column(Integer, primary_key=True)
    Name = Column(String)
    Description = Column(String)

    # Define the relationship
    wares = relationship("Ware", back_populates="category")

    def __repr__(self):
        return str(self.as_dict())
    
    def as_dict(self):
        return {
            'CategoryID': self.CategoryID,
            'Name': self.Name,
            'Description': self.Description
        }

    @classmethod
    def add(cls, name, description):
        session = None
        try:
            session = Session()
            new_category = cls(
                Name=name,
                Description=description
            )
            session.add(new_category)
            session.commit()
            print("Category added successfully!")
        except Exception as e:
            print(f"Error adding category: {e}")
            if session:
                session.rollback()  # Rollback the transaction in case of an error
        finally:
            if session:
                session.close()

    @classmethod
    def read(cls, category_id):
        session = None
        try:
            session = Session()
            category = session.query(cls).filter_by(CategoryID=category_id).first()
            if category:
                print("Category found:", category)
                return category
            else:
                print("Category not found.")
                return None
        except Exception as e:
            print(f"Error reading category: {e}")
        finally:
            if session:
                session.close()

    @classmethod
    def update(cls, category_id, name=None, description=None):
        session = None
        try:
            session = Session()
            category = session.query(cls).filter_by(CategoryID=category_id).first()
            if category:
                if name:
                    category.Name = name
                if description:
                    category.Description = description
                session.commit()
                print("Category updated successfully!")
            else:
                print("Category not found.")
        except Exception as e:
            print(f"Error updating category: {e}")
            if session:
                session.rollback()
        finally:
            if session:
                session.close()

    @classmethod
    def delete(cls, category_id):
        pass


# Example usage - Debug code:
# category = Category.create(name='Category A', description='Description of Category A')
# category = Category.read(1)
# category.update(name='Updated Category A')
