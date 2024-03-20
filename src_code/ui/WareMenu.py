###
# The menu that manages wares
# - CLY 20-03-24 -
###

from Menu import Menu

class WareMenu(Menu):
    def __init__(self):
        options = {
            "1": "Add Ware",
            "2": "Update Ware",
            "3": "Delete Ware"
        }
        super().__init__("Ware Management", options)