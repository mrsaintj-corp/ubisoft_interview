from genericpath import isfile
import os
from datetime import datetime

class Inventory:
    def __init__(self, path):
        self.path   = path

        if not os.path.isfile(self.path):
            inventory   = open(self.path, "w")
            inventory.write("localhost")
            inventory.close()

        with open(self.path) as inventory:
            content = inventory.readlines()

        self.inventory_arr   = [x.strip() for x in content]

    def get_inventory(self):
        return self.inventory_arr