# Dictionary containing the menu items and their prices
menu_items = {
    1: {"Item name": "Apple", "Price": 0.49},
    2: {"Item name": "Tea - Thai iced", "Price": 3.99},
    3: {"Item name": "Fried banana", "Price": 4.49},
    4: {"Item name": "Spring roll", "Price": 2.99}
}

# Empty list to store the customer's order
order = []

# Start taking orders from the customer
while True:
    # Display the menu
    print("Menu:")
    for key, item in menu_items.items():
        print(f"{key}. {item['Item name']} - ${item['Price']}")

    # Ask the customer to select an item by entering its number
    menu_selection = input("Please enter the menu item number you would like to order: ")

    # Check if the input is a valid number
    if not menu_selection.isdigit():
        print("Error: Please enter a valid number.")
        continue

    menu_selection = int(menu_selection)  # Convert the input to an integer

    # Check if the selected item exists in the menu
    if menu_selection not in menu_items:
        print("Error: Menu item does not exist. Please try again.")
        continue

    # Get the item name and price from the menu
    item_name = menu_items[menu_selection]["Item name"]
    price = menu_items[menu_selection]["Price"]

    # Ask the customer how many of the selected item they want to order
    quantity_input = input(f"How many {item_name}s would you like to order? (default is 1): ")

    # Check if the quantity input is a valid number
    if not quantity_input.isdigit():
        quantity = 1  # Default quantity is 1 if the input is invalid
    else:
        quantity = int(quantity_input)  # Convert the input to an integer

    # Add the item to the order list
    order.append({
        "Item name": item_name,
        "Price": price,
        "Quantity": quantity
    })

    # Ask the customer if they want to order anything else
    while True:
        more_order = input("Would you like to order anything else? (y/n): ").lower()
        if more_order == 'y':
            break  # Continue with the main loop to place another order
        elif more_order == 'n':
            print("Thank you for your order!")
            
            # Print the order receipt
            print("\nOrder Receipt:")
            print("Item name                 | Price  | Quantity")
            print("--------------------------|--------|----------")

            # Calculate the total price of the order
            total_price = sum(item["Price"] * item["Quantity"] for item in order)
            
            # Print each item in the order
            for item in order:
                item_name = item["Item name"]
                price = item["Price"]
                quantity = item["Quantity"]

                # Formatting for better readability
                name_spaces = ' ' * (26 - len(item_name))
                price_spaces = ' ' * (6 - len(f"{price:.2f}"))
                quantity_spaces = ' ' * (8 - len(str(quantity)))

                # Print each line of the receipt
                print(f"{item_name}{name_spaces}| ${price:.2f}{price_spaces}| {quantity}{quantity_spaces}")

            # Print the total price at the end
            print("--------------------------|--------|----------")
            print(f"Total Price: ${total_price:.2f}")
            exit()  # Exit the program after printing the receipt
        else:
            print("Error: Invalid input. Please enter 'y' or 'n'.")  # Ask the user to enter a valid response
