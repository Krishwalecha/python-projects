# Prompt user to enter their height in centimeters
height = int(input("Enter your height in centimeters: "))
bill = 0  # Initialize bill amount

# Check if the user is tall enough to ride
if height >= 120:
    print("Congratulations! You are tall enough to ride the roller coaster.")
    
    # Ask for user's age to determine ticket price
    age = int(input("Please enter your age: "))
    
    # Determine ticket price based on age
    if age <= 12:
        print("Child ticket costs 100 INR.")
        bill += 100
    elif age <= 18:
        print("Youth ticket costs 150 INR.")
        bill += 150
    elif 45 <= age <= 55:
        # Special free ride for midlife age group
        print("Everything is going to be okay. Enjoy your free ride!")
    else:
        print("Adult ticket costs 200 INR.")
        bill += 200

    # Ask if the user wants a photo taken
    wants_photo = input("Would you like a photo taken? (Y/N): ").upper()
    
    # Add photo cost if applicable
    if wants_photo == 'Y':
        if 45 <= age <= 55:
            # Free photo for midlife riders as well
            print("You also get a free photo!")
        else:
            print("Photos cost an additional 50 INR.")
            bill += 50

    # Print the total bill amount
    print(f"Your total bill is {bill} INR.")

else:
    # User is too short to ride
    print("Sorry, you need to grow taller before you can ride.")
