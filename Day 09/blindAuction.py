import os
import art

def clear_screen():
    # Clear the console screen for Windows or Unix-based systems
    os.system('cls' if os.name == 'nt' else 'clear')

def find_highest_bidder(bids_dict, item_name):
    # Determine the highest bidder and their bid for a given item
    highest_bid = 0
    winner = ""

    # Iterate over all bidders using keys and get bid amounts manually
    for bidder in bids_dict:
        bid = bids_dict[bidder]
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder
            
    # Display the winner for the item
    print(f"\nHighest bidder for '{item_name}' is {winner} with a bid of ₹{highest_bid:.2f}.\n")

def main():
    print("Welcome to the Secret Auction Program!")
    # List of items to auction
    items = ['Antique Vase', 'Antique Clock']

    # Loop over each item, showing its position out of total items
    for idx, item in enumerate(items, 1):
        bids = {}  # Dictionary to store bids for current item
        print(f"\nBidding for item {idx}/{len(items)}: {item}\n")
        print(art.gavel)  # Print gavel art for auction theme

        while True:
            # Ask bidder's name and format it properly
            name = input("What is your name? ").strip().title()

            # Validate bid input ensuring it is a valid float number
            while True:
                try:
                    bid_amount = float(input("What's your bid? ₹"))
                    break
                except ValueError:
                    print("Please enter a valid number for the bid.")

            # Record the bid amount with bidder's name as key
            bids[name] = bid_amount

            # Ask if there are more bidders; validate input to yes/no only
            while True:
                more_bidders = input("Are there any other bidders? (Yes/No): ").strip().lower()
                if more_bidders in ['yes', 'no']:
                    break
                print("Please enter 'Yes' or 'No'.")

            if more_bidders == 'no':
                # No more bidders, clear screen and show highest bidder for current item
                clear_screen()
                find_highest_bidder(bids, item)
                break
            else:
                # Clear screen for next bidder to keep bids secret
                clear_screen()

    print("Thanks for participating in the auction!")

if __name__ == "__main__":
    main()
