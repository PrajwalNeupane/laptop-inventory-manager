import os
from laptop import Laptop

class FileReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_laptops(self):
        laptops = []
        if not os.path.isfile(self.file_name):
            return laptops
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(', ')
                laptop = Laptop(data[0], data[1], float(data[2][1:]), int(data[3]), data[4], data[5])
                laptops.append(laptop)
        return laptops