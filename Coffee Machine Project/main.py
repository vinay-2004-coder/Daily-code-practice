# Coffee machine menu with ingredients required and cost of each drink
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0  # Total money earned by the machine
resources = {
    "water": 300,   # Amount of water available (ml)
    "milk": 200,    # Amount of milk available (ml)
    "coffee": 100,  # Amount of coffee available (grams)
}

is_on = True  # Flag to keep machine running

def is_resource_sufficient(order_ingredients):
    """Checks if resources are sufficient to make the drink.
    Returns True if enough, False if any ingredient is insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            # Not enough of this ingredient
            return False
    return True

def process_coins():
    """Prompts user to insert coins and calculates the total amount."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Checks if the payment is sufficient.
    Returns True if successful, False otherwise."""
    if money_received >= drink_cost:
        global profit
        change = round(money_received - drink_cost, 2)  # Calculate change
        print(f"Here is ${change} in change.")
        profit += drink_cost  # Add cost to profit
        return True
    else:
        print("Sorry, not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deducts the required ingredients from the resources and serves coffee."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

# Main loop to run the coffee machine
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False  # Turn off the machine
    elif choice == "report":
        # Print current resource status and profit
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        # Check if enough resources to make drink
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()  # Process inserted coins
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])  # Make coffee if payment OK
        else:
            print("Sorry, there are not enough resources to make that drink.")
