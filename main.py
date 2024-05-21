# Dictionary containing the menu items and their prices
menu_items = {
    1: {"Item name": "Apple", "Price": 0.49},
    2: {"Item name": "Tea - Thai iced", "Price": 3.99},
    3: {"Item name": "Fried banana", "Price": 4.49},
    4: {"Item name": "Spring roll", "Price": 2.99}
}

# Initial empty order list to store customer orders
order = []

# Main loop for taking orders
while True:
    # Print the menu
    print("Menu:")
    for key, item in menu_items.items():
        print(f"{key}. {item['Item name']} - ${item['Price']}")

    # Prompt user to select a menu item by entering the item number
    menu_selection = input("Please enter the menu item number you would like to order: ")

    # Validate if the input is a digit
    if not menu_selection.isdigit():
        print("Error: Please enter a valid number.")
        continue

    menu_selection = int(menu_selection)  # Convert input to integer

    # Check if the selected menu item exists
    if menu_selection not in menu_items:
        print("Error: Menu item does not exist. Please try again.")
        continue

    # Retrieve the item name and price from the menu
    item_name = menu_items[menu_selection]["Item name"]
    price = menu_items[menu_selection]["Price"]

    # Prompt user to enter the quantity for the selected item
    quantity_input = input(f"How many {item_name}s would you like to order? (default is 1): ")

    # Validate if the quantity input is a digit
    if not quantity_input.isdigit():
        quantity = 1  # Default quantity is 1 if input is invalid
    else:
        quantity = int(quantity_input)  # Convert input to integer

    # Append the order details to the order list
    order.append({
        "Item name": item_name,
        "Price": price,
        "Quantity": quantity
    })

    # Inner loop to check if the customer wants to place another order
    while True:
        # Prompt user to continue ordering or finish
        more_order = input("Would you like to order anything else? (y/n): ").lower()
        if more_order == 'y':
            break  # Exit inner loop and continue with the main loop for another order
        elif more_order == 'n':
            print("Thank you for your order!")
            
            # Print the receipt
            print("\nOrder Receipt:")
            print("Item name                 | Price  | Quantity")
            print("--------------------------|--------|----------")

            # Calculate the total price of the order
            total_price = sum(item["Price"] * item["Quantity"] for item in order)
            
            # Loop through each ordered item to print the receipt
            for item in order:
                item_name = item["Item name"]
                price = item["Price"]
                quantity = item["Quantity"]

                # Calculate spaces for formatting
                name_spaces = ' ' * (26 - len(item_name))
                price_spaces = ' ' * (6 - len(f"{price:.2f}"))
                quantity_spaces = ' ' * (8 - len(str(quantity)))

                # Print each line of the receipt
                print(f"{item_name}{name_spaces}| ${price:.2f}{price_spaces}| {quantity}{quantity_spaces}")

            # Print total price
            print("--------------------------|--------|----------")
            print(f"Total Price: ${total_price:.2f}")
            exit()  # Exit the program after printing the receipt
        else:
            print("Error: Invalid input. Please enter 'y' or 'n'.")  # Prompt user for correct input
