import csv
import datetime
import os

# Define the inventory file's name
INVENTORY_FILE = "inventory.csv"

# Laptop class to hold laptop attributes
class Laptop:
    # Constructor to initialize laptop attributes
    def __init__(self, name, brand, price, quantity, processor, graphics_card):
        self.name = name
        self.brand = brand
        self.price = float(price)
        self.quantity = int(quantity)
        self.processor = processor
        self.graphics_card = graphics_card

    # String representation of the laptop object
    def __str__(self):
        return f"{self.name}, {self.brand}, ${self.price}, {self.quantity}, {self.processor}, {self.graphics_card}"

# LaptopShop class to manage laptop inventory and sales
class LaptopShop:
    # Constructor initializes the inventory_file and reads the inventory
    def __init__(self, inventory_file=INVENTORY_FILE):
        self.inventory_file = inventory_file
        self.inventory = self.read_inventory()

    # Read inventory from the CSV file
    def read_inventory(self):
        inventory = []
        if os.path.exists(self.inventory_file):
            with open(self.inventory_file, "r") as f:
                reader = csv.reader(f)
                next(reader)  # Skip the header row
                for row in reader:
                    if not row:  # Skip empty rows
                        continue
                    try:
                        laptop = Laptop(*row)
                        inventory.append(laptop)
                    except ValueError as e:
                        print(f"Error creating Laptop object: {e}")
        return inventory
        # Update the inventory CSV file
    def update_inventory(self):
        with open(self.inventory_file, "w") as f:
            writer = csv.writer(f)
            for laptop in self.inventory:
                writer.writerow([laptop.name, laptop.brand, laptop.price, laptop.quantity, laptop.processor, laptop.graphics_card])

    # Display the inventory of laptops
    def display_inventory(self):
        print("Available Laptops:")
        print("Name, Brand, Price, Quantity, Processor, Graphics Card")
        for laptop in self.inventory:
            print(laptop)

    # Find a laptop by its name in the inventory
    def find_laptop(self, laptop_name):
        for laptop in self.inventory:
            if laptop.name == laptop_name:
                return laptop
        return None

    def buy_laptop(self):
        print("Enter the details of the laptop to buy:")
        name = input("Name: ")
        brand = input("Brand: ")
        price = self.get_float("Price: ")
        quantity = int(input("Quantity: "))
        processor = input("Processor: ")
        graphics_card = input("Graphics Card: ")

        new_laptop = Laptop(name, brand, price, quantity, processor, graphics_card)
        self.inventory.append(new_laptop)
        self.update_inventory()
        print("Laptop added to inventory.")


    # Sell a laptop and generate an invoice
    def sell_laptop(self):
        self.display_inventory()
        laptop_name = input("Enter the name of the laptop to sell: ")
        customer_name = input("Enter the name of the customer: ")
        shipping_cost = self.get_float("Enter the shipping cost: ")

        laptop = self.find_laptop(laptop_name)

        if laptop:
            if laptop.quantity > 0:
                laptop.quantity -= 1
                invoice_total = laptop.price + shipping_cost
                self.create_invoice(laptop, customer_name, shipping_cost, invoice_total)
                print("Laptop sold and invoice generated.")
            else:
                print("Sorry, the laptop is out of stock.")
        else:
            print("Laptop not found in inventory.")

    # Get a float input from the user
    @staticmethod
    def get_float(prompt):
        while True:
            try:
                value = float(input(prompt))
                break
            except ValueError:
                print("Invalid input, please enter a valid number.")
        return value

    # Create an invoice for the laptop sale
    @staticmethod
    def create_invoice(laptop, customer_name, shipping_cost, invoice_total):
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        invoice_file = f"invoice_{timestamp}.txt"

        with open(invoice_file, "w") as f:
            f.write("Invoice\n")
            f.write("----------------------------------------------------------\n")
            f.write(f"Customer Name: {customer_name}\n")
            f.write(f"Laptop Name: {laptop.name}\n")
            f.write(f"Brand: {laptop.brand}\n")
            f.write(f"Price: ${laptop.price}\n")
            f.write(f"Shipping cost: ${shipping_cost}\n")
            f.write("----------------------------------------------------------\n")
            f.write(f"Total: ${invoice_total}\n")

    # Run the main loop for the laptop shop
    # Run the main loop for the laptop shop
    def run(self):
        while True:
            print("\nOptions:")
            print("1. Display inventory")
            print("2. Buy laptop")
            print("3. Sell laptop")
            print("4. Quit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.display_inventory()
            elif choice == 2:
                self.buy_laptop()
            elif choice == 3:
                self.sell_laptop()
                self.update_inventory()
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please try again.")

# Main function to run the laptop shop
if __name__ == "__main__":
    shop = LaptopShop()
    shop.run()