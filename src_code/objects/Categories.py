####
# An object representing the category of our wares inside the Warehouse system
# - CLY 18-03-24 -
####
# Imports

# Globals

# Class
class Category:
    # Methods
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

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
