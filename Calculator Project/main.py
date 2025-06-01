import art

print(art.logo)  # Print the calculator logo/art at the start


# Define basic arithmetic functions
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Dictionary mapping operator symbols to corresponding functions
calc_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    should_accumulate = True  # Flag to control continuous calculation chaining
    first_number = int(input("Type first number: "))  # Get the first number from user

    while should_accumulate:
        # Display all available operators
        for symbol in calc_dict:
            print(symbol)

        # Ask user to pick an operator
        mathematical_operator = input("Type the operator + - * /: ")

        # Get the second number
        second_number = int(input("Type second number: "))

        # Perform calculation by calling the correct function from dictionary
        result = calc_dict[mathematical_operator](first_number, second_number)

        # Show the result with the correct operator symbol
        print(f"{first_number} {mathematical_operator} {second_number} = {result}")

        # Ask if the user wants to continue calculating with the current result
        choice = input(f"Enter 'y' to continue calculating with {result}, or 'x' to exit: ").lower()

        if choice == 'y':
            # Continue calculating by using the current result as first number
            first_number = result
        else:
            # Stop the current calculation loop and clear screen (by printing new lines)
            should_accumulate = False
            print("\n" * 20)
            # Restart calculator for a new session
            calculator()


# Start the calculator program
calculator()
