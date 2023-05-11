from laptop import Laptop

class FileWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_laptops(self, laptops):
        with open(self.file_name, 'w') as file:
            for laptop in laptops:
                file.write(str(laptop) + '\n')