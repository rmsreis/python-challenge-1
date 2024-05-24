# Order System

This project implements a simple order system where customers can place orders from a menu, and the system prints a receipt with the total price of all items ordered.

## Features

- Display a menu with items and prices.
- Allow customers to place orders by selecting items and specifying quantities.
- Validate customer input to ensure correctness.
- Print a formatted receipt showing all ordered items, their prices, quantities, and the total price.

## Menu Items

The menu contains the following items:

1. Apple - $0.49
2. Tea - Thai iced - $3.99
3. Fried banana - $4.49
4. Spring roll - $2.99

## Code Structure

The code is written in a linear manner and contains the following main sections:

1. **Menu Items Dictionary**: Defines the available menu items and their prices.
2. **Order List**: An empty list that will store the customer's order.
3. **Main Loop**: Continuously prompts the customer for their order until they choose to stop.
4. **Input Validation**: Ensures that the customer's menu selection and quantity inputs are valid.
5. **Order Processing**: Appends the customer's order to the order list.
6. **Receipt Printing**: Displays a formatted receipt with all ordered items and the total price.

## Usage

1. **Run the Code**: Execute the script to start the order system.
2. **Place Orders**: Follow the prompts to select menu items and specify quantities.
3. **Complete Order**: Choose to stop ordering when prompted, and the receipt will be printed.

## Example Interaction

```
Menu:
1. Apple - $0.49
2. Tea - Thai iced - $3.99
3. Fried banana - $4.49
4. Spring roll - $2.99
Please enter the menu item number you would like to order: 2
How many Tea - Thai iceds would you like to order? (default is 1): 2
Would you like to order anything else? (y/n): y
Menu:
1. Apple - $0.49
2. Tea - Thai iced - $3.99
3. Fried banana - $4.49
4. Spring roll - $2.99
Please enter the menu item number you would like to order: 3
How many Fried bananas would you like to order? (default is 1): 1
Would you like to order anything else? (y/n): n
Thank you for your order!

Order Receipt:
Item name                 | Price  | Quantity
--------------------------|--------|----------
Tea - Thai iced           | $3.99  | 2
Fried banana              | $4.49  | 1
--------------------------|--------|----------
Total Price: $12.47

```


## Notes

- Ensure Python is installed on your system to run the script.
- Customize the menu items and prices as needed by modifying the menu_items dictionary.
- The system will handle input errors and guide the user accordingly.


---------------------------------
*Developed by Roberto dos Reis*