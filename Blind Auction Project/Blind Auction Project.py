import art
print(art.logo)  # Print the logo art at the start

def highest_bidder(new_dict):
    # Initialize variables to track the highest bid and the winner's name
    winner = ""
    highest_bid = 0

    # Loop through each bidder and their bid amount in the dictionary
    for bidder in new_dict:
        bid_amount = new_dict[bidder]
        # Check if the current bid is higher than the recorded highest bid
        if bid_amount > highest_bid:
            highest_bid = bid_amount  # Update highest bid
            winner = bidder           # Update winner's name
    # Print the winner and their bid amount
    print(f"The winner is {winner} with a bid amt of {highest_bid}")

bids = {}               # Dictionary to store bidder names and their bid amounts
continue_bidding = True # Control variable to keep the bidding process running

while continue_bidding:
    name = input("Enter your name?")          # Ask user for their name
    price = int(input("Enter bid amount"))    # Ask user for their bid amount (converted to int)
    bids[name] = price                         # Save the bid in the dictionary

    should_continue = input("Do you want to continue or not? yes or no").lower()
    # Decide whether to continue or stop bidding based on user input
    if should_continue == "no":
        continue_bidding = False  # Stop the bidding loop
        highest_bidder(bids)      # Call function to find and print the highest bidder
    elif should_continue == "yes":
        print("\n" * 20)          # Clear the screen by printing new lines for next bidder