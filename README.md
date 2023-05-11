Introduction
------------
This project aims to develop a simple, user-friendly laptop selling and buying system. The users can manage laptop stocks, purchase, and sell laptops while generating receipts for each transaction. The objectives of this project include:

1. Implementing a robust program to handle laptop inventory.
2. Providing an easy-to-use interface for purchasing and selling laptops.
3. Generating and saving receipts for each transaction.
4. Ensuring proper error handling and validation of user inputs.

Discussion and Analysis
-----------------------

*Algorithm

1. Import required modules and classes.
2. Define Laptop class with methods to initialize and represent laptops.
3. Define FileReader class with methods to read laptops data from a file.
4. Define FileWriter class with methods to write laptops data to a file.
5. Define LaptopOperations class with methods to perform various operations on laptops, such as add, update, display, and generate receipts.
6. Define a display_welcome_screen() function to display the welcome screen for the laptop store.
7. Define a main() function to manage the overall flow of the program:
    7.1. Initialize LaptopOperations object.
    7.2. Create a 'receipts' folder if it doesn't exist.
    7.3. Run a loop until the user decides to exit:
        7.3.1. Display the welcome screen and available laptops.
        7.3.2. Show options (Purchase, Sell, Exit) and get user input.
        7.3.3. Perform the selected operation:
            7.3.3.1. If Purchase, get customer name, selected laptops and quantities, update laptop quantities, and generate the receipt.
            7.3.3.2. If Sell, get customer name, selected laptops and quantities, update laptop quantities with shipping option, and generate the receipt.
            7.3.3.3. If Exit, display a thank you message and break the loop.
        7.3.4. Handle exceptions and display appropriate error messages.
8. Call the main() function to execute the program.

*Flow Chart

*Pseudocode
For ‘main.py’

Import required modules and classes

Define display_welcome_screen() function:
    Set text color to blue and bold
    Define screen width
    Print welcome screen
    Reset text color to default

Define main() function:
    Initialize LaptopOperations object
    Create 'receipts' folder if it doesn't exist

    Loop until user exits:
        Call display_welcome_screen()
        Display laptops
        Display options (Purchase, Sell, Exit)
        Get user input

        Try:
            If user input is "1" (Purchase):
                Get customer name
                Initialize selected_laptops list

                Loop until user finishes selecting laptops:
                    Get laptop ID and quantity
                    If laptop_id is -1, break the loop
                    Append (laptop_id, quantity) to selected_laptops list
                    Update laptop quantity (increase)

                Generate receipt for purchase
                Print success message

            If user input is "2" (Sell):
                Get customer name
                Initialize selected_laptops list

                Loop until user finishes selecting laptops:
                    Try:
                        Get laptop ID
                        If laptop_id is -1, break the loop
                        Check if laptop_id is valid:
                            Get quantity
                            Append (laptop_id, quantity) to selected_laptops list
                            Update laptop quantity (decrease)
                        Else:
                            Print "Invalid laptop ID" message
                    Catch exceptions and display appropriate error messages

                Ask if the user wants to include shipping
                Generate receipt for selling with or without shipping
                Print success message

            If user input is "3" (Exit):
                Print exit message and break the loop

            Else:
                Print "Invalid input" message

        Catch exceptions and display appropriate error messages

Call main() function

For write.py

Import Laptop class

Define FileWriter class:
    Initialization method with file_name as a parameter:
        Set file_name as an instance variable

    Define write_laptops() method with laptops as a parameter:
        Open the file in 'write' mode using 'with' statement and the file_name instance variable:
            Loop over each laptop in the laptops list:
                Write the string representation of the laptop to the file, followed by a newline character

For operations.py 

Import required modules and classes

Define LaptopOperations class:
    Initialization method with file_name as a parameter:
        Set file_name, FileReader, FileWriter, and laptops as instance variables

    Define add_laptop() method with laptop as a parameter:
        Append laptop to laptops list
        Call write_laptops() method with laptops list

    Define update_laptop() method with laptop_id, quantity, add as parameters:
        Get laptop by laptop_id
        If add is True, increase laptop quantity
        Else, check if updated quantity is greater than or equal to 0:
            Decrease laptop quantity
            If not, display error message and return
        Call write_laptops() method with laptops list

    Define get_laptop_by_id() method with laptop_id as a parameter:
        Return laptop from laptops list by laptop_id

    Define display_laptops() method:
        Define table header and separator
        Print table header and separator
        Loop over laptops and print laptop information
        Print table separator

    Define generate_receipt() method with selected_laptops, customer_name, is_purchase, is_shipping as parameters:
        Get date_time and receipt_id
        Set text color to cyan
        Build receipt header and details
        Calculate total, VAT, and total with VAT
        If is_shipping is True, add shipping cost and calculate total with shipping
        Build receipt footer
        Reset text color to default
        Set text color to green
        Print receipt
        Save receipt to a file in 'receipts' folder

For read.py

Import required modules and classes

Define FileReader class:
    Initialization method with file_name as a parameter:
        Set file_name as an instance variable

    Define read_laptops() method:
        Initialize empty laptops list
        Check if the file exists, if not, return the empty laptops list
        Open the file in 'read' mode using 'with' statement and the file_name instance variable:
            Read lines from the file
            Loop over each line:
                Split the line into data
                Create a Laptop object with data
                Append the Laptop object to laptops list
        Return laptops list

For Laptop.py

Define Laptop class:
    Initialization method with name, brand, price, quantity, processor, graphics_card as parameters:
        Set name, brand, price, quantity, processor, and graphics_card as instance variables

    Define __str__() method:
        Return a formatted string with name, brand, price, quantity, processor, and graphics_card separated by commas



* Data Structures
  - The primary data structure used in this project is the `Laptop` class. The class holds laptop information such as name, brand, price, quantity, processor, and graphics card. Below is a code snippet of the Laptop class:




  - The `LaptopOperations` class manages a list of `Laptop` objects, which represents the inventory. This list is updated whenever a laptop is purchased or sold.

  - Apart from the `Laptop` class, the project also uses various other data structures such as lists, tuples, and dictionaries to manage and organize data. Here are some examples:

    1. Lists:
       - Lists are used to store multiple `Laptop` objects, hold selected laptops during purchase and sale operations, and manage the lines read from the file. Below is a code snippet that demonstrates the use of lists:
       
```python
self.laptops = self.file_reader.read_laptops()

selected_laptops = [(laptop_id, quantity)]
```



    2. Tuples:
       - Tuples are used to store a pair of values (laptop_id, quantity) during the purchase and sale of laptops. They are useful when multiple values need to be grouped together. Here's an example of using tuples:



    3. Dictionaries:
       - Dictionaries are not explicitly used in the project. However, they can be employed to improve the search functionality when looking for laptops by their attributes. For instance, a dictionary can map laptop IDs to their corresponding `Laptop` objects, allowing for faster access:

```python
laptop_dict = {laptop_id: laptop for laptop_id, laptop in enumerate(self.laptops)}
```

      With a dictionary like this, it is possible to efficiently find a laptop by its ID:

```python
laptop = laptop_dict[laptop_id]
```

   By using these data structures, the application can efficiently manage, access, and update laptop inventory and transactions.

Program
-------

The program is implemented using multiple Python files, each handling a specific functionality:

1. `main.py`: This is the primary file that runs the program and handles user input. It consists of the main menu where users can choose to purchase, sell or exit the program. It also creates the 'receipts' folder for storing generated receipts.

   The main menu provides three options: Purchase, Sell, and Exit. Users can select an option by entering the corresponding number. For the Purchase and Sell options, the user enters the customer name, laptop ID, and quantity of laptops to be purchased or sold. The program then generates a receipt with the transaction details and updates the inventory.

2. `laptop.py`: Contains the `Laptop` class definition for creating laptop objects with attributes such as name, brand, price, quantity, processor, and graphics card. This class is used to represent individual laptops in the inventory.

3. `operations.py`: Defines the `LaptopOperations` class, which manages the inventory of laptops and handles operations such as displaying available laptops, updating stock, and generating receipts. The class uses the FileReader and FileWriter classes to read and write laptop data from/to a text file.

4. `read.py`: Contains the `FileReader` class which reads laptops data from a text file and creates a list of `Laptop` objects. This class is used by the `LaptopOperations` class to initialize the inventory.

5. `write.py`: Implements the `FileWriter` class, which writes the updated laptops list back to the text file after performing operations like purchasing or selling. This class is used by the `LaptopOperations` class to save the updated inventory.

Purchase and Sale Process
-------------------------
The program allows users to purchase and sell laptops by selecting the appropriate option from the main menu. During the purchase and sale process, users enter the customer name, laptop ID, and quantity of laptops to be purchased or sold. The program then updates the inventory, generates a receipt, and saves the receipt as a text file in the 'receipts' folder.

Creation of Text Files
----------------------
When the program generates a receipt, it creates a new text file in the 'receipts' folder with the receipt details. Each receipt text file is named after the receipt ID, which is a unique identifier based on the current timestamp.

Displaying the Receipt and Terminating the Program
--------------------------------------------------
Upon completing a purchase or sale transaction, the program displays the receipt in the shell, showing the transaction details, customer name, and total amount. Users can view the corresponding text file in the 'receipts' folder for a saved copy of the receipt.

To terminate the program, users can select the Exit option from the main menu. The program will display a farewell message and exit gracefully.

-------

The following test scenarios are covered:

* Test 1: Demonstrate the implementation of try and except to handle invalid inputs.
  
  Objective: Test error handling for invalid inputs.
  Action: Provide an invalid input during the laptop purchase or sale process.
  Expected Result: The program should display an error message and prompt the user to enter the correct input.
  Actual Result: [To be filled based on the test execution]
  Conclusion: [To be filled based on the test execution]

* Test 2: Test the purchase and sale of laptops with negative values and non-existent values as input.
  
  Objective: Test the application's ability to handle incorrect laptop IDs and quantities.
  Action: Provide a negative value or non-existent laptop ID during the purchase or sale process.
  Expected Result: The program should display an error message and prompt the user to enter a valid laptop ID or quantity.
  Actual Result: [To be filled based on the test execution]
  Conclusion: [To be filled based on the test execution]

* Test 3: Verify the file generation during the purchase of multiple laptops, display the output in the shell, and show the purchased laptop details in a text file.
  
  Objective: Test the receipt generation and file creation during the purchase process.
  Action: Purchase multiple laptops and complete the transaction.
  Expected Result: The program should display the receipt in the shell, and a text file containing the receipt should be created in the 'receipts' folder.
  Actual Result: [To be filled based on the test execution]
  Conclusion: [To be filled based on the test execution]

* Test 4: Test the file generation during the sales process of multiple laptops, display the output in the shell, and show the sold laptop details in a text file.
  
  Objective: Test the receipt generation and file creation during the sales process.
  Action: Sell multiple laptops and complete the transaction.
  Expected Result: The program should display the receipt in the shell, and a text file containing the receipt should be created in the 'receipts' folder.
  Actual Result: [To be filled based on the test execution]
  Conclusion: [To be filled based on the test execution]

* Test 5: Validate the update in stock of laptops upon purchase and sale, and ensure the updates are reflected in the text file.
  
  Objective: Test the inventory update upon purchase and sale of laptops.
  Action: Perform purchase and sale transactions and check the inventory update in the text file.
  Expected Result: The stock of laptops should be updated in the text file after each transaction.
  Actual Result: [To be filled based on the test execution]
  Conclusion: [To be filled based on the test execution]

These tests ensure that the laptop selling and buying system can handle various user inputs and scenarios, and the inventory updates and receipt generation work as expected.


Conclusion
----------
In conclusion, the laptop selling and buying system successfully meets the project objectives by providing an easy-to-use platform for managing laptop inventory, purchasing and selling laptops, and generating receipts for each transaction. The program ensures proper error handling and validation of user inputs, making it a reliable tool for laptop shop management.

