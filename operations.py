from read import FileReader
from write import FileWriter
from laptop import Laptop
import time

class LaptopOperations:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_reader = FileReader(file_name)
        self.file_writer = FileWriter(file_name)
        self.laptops = self.file_reader.read_laptops()

    def add_laptop(self, laptop):
        self.laptops.append(laptop)
        self.file_writer.write_laptops(self.laptops)

    def update_laptop(self, laptop_id, quantity, add=True):
        laptop = self.laptops[laptop_id]
        if add:
            laptop.quantity += quantity
        else:
            if laptop.quantity - quantity >= 0:
                laptop.quantity -= quantity
            else:
                print(f"Error: Not enough stock available for {laptop.name}.")
                return
        self.file_writer.write_laptops(self.laptops)

    def get_laptop_by_id(self, laptop_id):
        return self.laptops[laptop_id]

    def display_laptops(self):
        screen_width = 120

        table_header = "| {0:<2} | {1:<20} | {2:<10} | {3:<7} | {4:<15} | {5:<15} |".format("ID", "Laptop Name", "Price", "Quantity", "Processor", "Graphics Card")
        table_separator = "-" * len(table_header)
        Header = "\nAvailable Laptops:"

        print(Header.center(screen_width))
        print("\n" + table_separator.center(screen_width))
        print(table_header.center(screen_width))
        print(table_separator.center(screen_width))

        for idx, laptop in enumerate(self.laptops):
            row = "| {0:<2} | {1:<20} | ${2:<8} | {3:<7} | {4:<15} | {5:<15} |".format(str(idx), laptop.name, str(laptop.price), str(laptop.quantity), laptop.processor, laptop.graphics_card)
            print(row.center(screen_width))

        print(table_separator.center(screen_width))
    
    def generate_receipt(self, selected_laptops, customer_name, is_purchase=True, is_shipping=False):
        total = 0
        total_with_vat = 0 

        date_time = time.strftime('%Y-%m-%d %H:%M:%S')
        receipt_id = f"{int(time.time())}_multi"

        # Set text color to cyan
        print("\033[0;36;48m")

        # Print receipt header
        receipt = f"{'*' * 40}\n"
        receipt += f"{'Laptop Shop Receipt':^40}\n"
        receipt += f"{'*' * 40}\n"

        # Set text color to yellow
        print("\033[0;33;48m")

        receipt += f"Receipt ID: {receipt_id}\n"
        receipt += f"Date & Time: {date_time}\n"
        receipt += f"{'-' * 40}\n"
        receipt += f"{'Item':<20}{'Price':<10}{'Quantity':<10}\n"
        receipt += f"{'-' * 40}\n"

        total = 0

        # Handle single laptop purchase
        if isinstance(selected_laptops, int):
            laptop_id = selected_laptops
            quantity = customer_name  # In this case, the 'customer_name' argument holds the quantity value
            laptop = self.get_laptop_by_id(laptop_id)
            receipt += f"{laptop.name:<20}${laptop.price:<10}{quantity:<10}\n"
            total += laptop.price * quantity
            selected_laptops = [(laptop_id, quantity)]  # Convert it into list form for later use

        # Handle multiple laptop purchases
        else:
            for laptop_id, quantity in selected_laptops:
                laptop = self.get_laptop_by_id(laptop_id)
                receipt += f"{laptop.name:<20}${laptop.price:<10}{quantity:<10}\n"
                total += laptop.price * quantity

        receipt += f"{'-' * 40}\n"
        receipt += f"{'Total':<30}${round(total, 2):<10}\n"
        
        # Calculate and display VAT and Total
        if not is_purchase:
            receipt += f"{'VAT (13%)':<30}${total * 0.13:<10}\n"
            total_with_vat = total * 1.13
            receipt += f"{'Total (with VAT)':<30}${round(total_with_vat, 2):<10}\n"
        
        if is_shipping:
            receipt += f"{'Shipping':<30}${500:<10}\n"
            receipt += f"{'Total (with Shipping)':<30}${round(total_with_vat + 500, 2):<10}\n"

        receipt += f"{'-' * 40}\n"
        receipt += f"{'Customer Name':<15}{customer_name:<25}\n"
        receipt += f"{'-' * 40}\n"

        # Set text color to magenta
        print("\033[0;35;48m")
        receipt += f"{'Thank You for Your Business!':^40}\n"
        receipt += f"{'*' * 40}\n"

        # Reset text color to default
        print("\033[0;37;48m")

        # Set text color to green
        print("\033[0;32;48m")

        print(receipt)

        with open(f"receipts/{receipt_id}.txt", "w") as receipt_file:
            receipt_file.write(receipt)