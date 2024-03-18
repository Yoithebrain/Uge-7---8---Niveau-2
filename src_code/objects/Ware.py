####
# An object representing the Ware inside the Warehouse system
# - CLY 18-03-24 -
####

# Imports

# Globals

# Class
class Ware:
    # Methods
    def __init__(self, id, name, description, quantity, price):
        self.id = id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price

    @classmethod
    def initialize(cls, engine):
        pass

    def add(self):
        pass

    def update(self, name=None, description=None, quantity=None, price=None):
        pass

    @classmethod
    def get(cls, ware_id):
        pass

    @classmethod
    def get_all(cls):
        pass

# Example usage:
# ware = Ware(name='Product A', description='Description of Product A', quantity=100, price=50)
# ware.add()
# ware.update(quantity=150)
# ware = Ware.get(1)
# print(ware)
# wares = Ware.get_all()
# for w in wares:
#     print(w)
