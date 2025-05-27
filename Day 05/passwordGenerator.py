import random

# Character sets used for password generation
alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%^&*()_='
digits = '0123456789'

print("Welcome to the Python Password Generator!")

# Ask user for the type of password they want
user_choice = input("Would you like a custom password or a randomly generated one? (Enter 'Custom' or 'Random'): ").strip().capitalize()

if user_choice == 'Custom':
    # User specifies exact counts
    num_alphabets = int(input("Enter the number of alphabets you'd like: "))
    num_symbols = int(input("Enter the number of symbols you'd like: "))
    num_digits = int(input("Enter the number of digits you'd like: "))
    
elif user_choice == 'Random':
    # User sets max count, actual counts are randomized but at least 3
    max_chars_per_type = int(input("Enter the maximum number of characters per type (minimum 4): "))
    if max_chars_per_type < 4:
        print("Too few characters! Setting maximum characters per type to 4.")
        max_chars_per_type = 4
        
    num_alphabets = random.randint(3, max_chars_per_type)
    num_symbols = random.randint(3, max_chars_per_type)
    num_digits = random.randint(3, max_chars_per_type)

else:
    print("Invalid choice! Please enter 'Custom' or 'Random'.")
    exit()

# Generate the list of characters for the password
password_chars = (
    random.choices(alphabets, k=num_alphabets) +
    random.choices(symbols, k=num_symbols) +
    random.choices(digits, k=num_digits)
)

# Shuffle characters to randomize the order
random.shuffle(password_chars)

# Join list into a string to form the final password
generated_password = "".join(password_chars)

print(f"Your secure password is: {generated_password}")
