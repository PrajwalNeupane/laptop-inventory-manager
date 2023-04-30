import csv
import random
import os

INVENTORY_FILE = "inventory.csv"
LAPTOP_NAMES = ["Razer Blade", "XPS", "Alienware", "Swift 7", "Macbook Pro 16"]
BRANDS = ["Razer", "Dell", "Alienware", "Acer", "Apple"]
PROCESSORS = ["i5 9th Gen", "i7 7th Gen", "i7 11th Gen", "i9 10th Gen", "i5 11th Gen"]
GRAPHICS_CARDS = ["GTX 3060", "GTX 3070", "RTX 3060", "RTX 3070", "RTX 3080"]

def generate_random_laptop_data():
    name = random.choice(LAPTOP_NAMES)
    brand = random.choice(BRANDS)
    price = random.uniform(900, 3500)
    quantity = random.randint(1, 50)
    processor = random.choice(PROCESSORS)
    graphics_card = random.choice(GRAPHICS_CARDS)
    return [name, brand, f"{price:.2f}", quantity, processor, graphics_card]

def generate_inventory(num_laptops=50):
    inventory = []

    for _ in range(num_laptops):
        laptop_data = generate_random_laptop_data()
        inventory.append(laptop_data)

    return inventory

def write_inventory_to_csv(inventory):
    if not os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, "w") as f:
            writer = csv.writer(f)
            writer.writerows(inventory)

if __name__ == "__main__":
    inventory = generate_inventory()
    write_inventory_to_csv(inventory)
    print("Random inventory generated.")