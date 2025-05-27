import art  # Assuming you use this module for ASCII art or similar

print("Welcome to the Treasure Hunt!")
print("Your mission is to find the treasure.")

# First decision at the crossroad
crossroad = input("You are at a crossroad. Do you want to go left or right? ").strip().lower()

if crossroad == 'left':
    # Arrived at the lake scenario
    lake = input("You come to a lake. Do you want to swim across or wait for a boat? ").strip().lower()
    
    if lake == 'wait':
        # Arrived at the house with 3 doors
        door = input("You arrive at a house with 3 doors: red, yellow, and blue. Which color do you choose? ").strip().lower()
        
        if door == 'yellow':
            print("You found the treasure! You win!")
        elif door == 'red':
            print("It's a room full of fire. Game over.")
        elif door == 'blue':
            print("You enter a room of beasts. Game over.")
        else:
            print("You chose a door that doesn't exist. Game over.")
            
    elif lake == 'swim':
        print("You got attacked by a shark. Game over.")
    else:
        print("Invalid choice at the lake. Game over.")
        
else:
    print("You fell into a hole. Game over.")
