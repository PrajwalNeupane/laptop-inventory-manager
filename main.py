import os
from operations import LaptopOperations

def display_welcome_screen():

    # Set text color to blue and bold
    print("\033[1;34;48m")

    # Define screen width
    screen_width = 100

    print("\n" + "=" * screen_width)
    print("Welcome to the Laptop Shop".center(screen_width))
    print("=" * screen_width + "\n")

    # Reset text color to default
    print("\033[0;37;48m")

def main():
    laptop_operations = LaptopOperations("laptops.txt")

    # Create 'receipts' folder if it doesn't exist
    if not os.path.exists("receipts"):
        os.makedirs("receipts")

    while True:
        display_welcome_screen()
        laptop_operations.display_laptops()
        print("\nOptions:")
        print("1. Purchase")
        print("2. Sell")
        print("3. Exit")
        user_input = input("Enter your choice (1-3): ")

        try:
            if user_input == "1":
                customer_name = input("Enter the customer name: ")
                selected_laptops = []

                while True:
                    laptop_id = int(input("Enter laptop ID to purchase (-1 to finish): "))
                    if laptop_id == -1:
                        break
                    quantity = int(input("Enter the quantity: "))
                    selected_laptops.append((laptop_id, quantity))
                    laptop_operations.update_laptop(laptop_id, quantity, add=True)

                laptop_operations.generate_receipt(selected_laptops, customer_name, is_purchase=True)
                print("Laptop stock updated after purchase.")
            elif user_input == "2":
                customer_name = input("Enter the customer name: ")
                selected_laptops = []

                while True:
                    try:
                        laptop_id = int(input("Enter laptop ID to sell (-1 to finish): "))
                        if laptop_id == -1:
                            break
                        
                        if laptop_id >= 0 and laptop_id < len(laptop_operations.laptops):
                            quantity = int(input("Enter the quantity: "))
                            selected_laptops.append((laptop_id, quantity))
                            laptop_operations.update_laptop(laptop_id, quantity, add=False)
                        else:
                            print("Invalid laptop ID. Please try again.")

                    except ValueError:
                        print("Invalid input. Please enter numbers only.")
                    except IndexError:
                        print("Laptop ID is out of range. Please try again.")
                    except Exception as e:
                        print(f"An error occurred: {e}")

                is_shipping = input("Include Shipping ($500) (y/n)")
                if is_shipping.lower() == "y":
                    laptop_operations.generate_receipt(selected_laptops, customer_name, is_purchase=False, is_shipping=True)

                print("Laptop stock updated after selling multiple laptop types.")
            elif user_input == "3":
                print("Thank you for using the laptop selling/buying system.")
                break
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()