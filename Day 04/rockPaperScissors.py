import random
import art  # Custom module with ASCII art for Rock, Paper, Scissors

print("Welcome to the Rock, Paper, Scissors game!")
print("What do you choose?")
print("0: Rock\n1: Paper\n2: Scissors")

# Get user input and validate
try:
    user_choice = int(input("Enter 0, 1, or 2: "))
    if user_choice not in [0, 1, 2]:
        print("Invalid choice! Please enter 0, 1, or 2.")
        exit()
except ValueError:
    print("Invalid input! Please enter a number (0, 1, or 2).")
    exit()

# Computer randomly chooses
computer_choice = random.randint(0, 2)

# Show choices with ASCII art
print(f"\nYou chose:\n{art.options[user_choice]}")
print(f"Computer chose:\n{art.options[computer_choice]}")

# Determine the outcome
if user_choice == computer_choice:
    print("It's a tie!")
elif (
    (user_choice == 0 and computer_choice == 2) or
    (user_choice == 1 and computer_choice == 0) or
    (user_choice == 2 and computer_choice == 1)
):
    print("Congrats, you won!")
else:
    print("Oops, computer won!")
