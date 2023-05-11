class Laptop:
    def __init__(self, name, brand, price, quantity, processor, graphics_card):
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.processor = processor
        self.graphics_card = graphics_card

    def __str__(self):
        return f"{self.name}, {self.brand}, ${self.price}, {self.quantity}, {self.processor}, {self.graphics_card}"