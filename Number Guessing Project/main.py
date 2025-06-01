import art
import random

print(art.logo)  # Print game logo/art

# List of possible numbers to guess from
numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

# Randomly select the actual number from the list
actual_no = random.choice(numbers)

print(actual_no)  # Debug print: show the actual number (you might want to remove this in final game)

should_continue = True  # Controls number of attempts left

# Ask user to choose difficulty mode
mode = input("easy or hard: ").lower()

# Set attempts based on difficulty
if mode == "easy":
    should_continue = 10
if mode == "hard":
    should_continue = 5

# Main guessing loop while attempts remain
while should_continue:
    user_guess = int(input("Guess a number: "))
    print(f"You have {should_continue} attempts to complete the game")

    if user_guess > actual_no:
        print("Too high")
    if user_guess < actual_no:
        print("Too low")
    if user_guess == actual_no:
        print("Correct guess!")
        break

    should_continue -= 1  # Decrease attempts left
