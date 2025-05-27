print("Welcome to the Python Pizza Store!")

# Ask the user for size, chicken, and cheese preferences
size = input("What size pizza would you like? S, M, or L: ").upper()
add_chicken = input("Would you like to add chicken? (Y/N): ").upper()
extra_cheese = input("Would you like extra cheese? (Y/N): ").upper()

# Start with a base bill of 0
bill = 0

# Add cost based on pizza size
if size == 'S':
    bill += 200
elif size == 'M':
    bill += 250
elif size == 'L':
    bill += 300
else:
    print("Invalid size. Please choose S, M, or L.")
    exit()

# Add cost for chicken
if add_chicken == 'Y':
    if size == 'S':
        bill += 50
    else:
        bill += 70

# Add cost for extra cheese
if extra_cheese == 'Y':
    bill += 30

# Display the total bill
print(f"Your final bill is: INR {bill}")
