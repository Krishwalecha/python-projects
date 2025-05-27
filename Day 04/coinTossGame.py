import random

print("Welcome to the Coin Toss Game!")
print("Your mission is to guess the result of the coin toss.")

# Generate a random coin toss: 0 for Heads, 1 for Tails
flip = random.randint(0, 1)

# Get user's guess
guess = int(input("Guess the coin toss result (0 for Heads, 1 for Tails): "))

# Check if the guess matches the toss
if flip == guess:
    print("You guessed it right!")
else:
    print("Oops! That's not correct.")
    if flip == 0:
        print("The coin toss was Heads.")
    else:
        print("The coin toss was Tails.")
