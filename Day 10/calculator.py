import art
import os

# Define basic arithmetic functions
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multiple(num1, num2):
    return num1 * num2

def divide(num1, num2):
    # Handle division by zero error
    if num2 == 0:
        return "Error: Cannot divide by zero."
    return num1 / num2

def clear_screen():
    # Clear the console screen for Windows or Unix-based systems
    os.system('cls' if os.name == 'nt' else 'clear')

# Mapping operators to corresponding functions
operations = {
    '+' : add,
    '-' : sub,
    '*' : multiple,
    '/' : divide
}

use_previous_result = False  # Flag to control whether to reuse previous result as first number
previous_result = 0          # Store last calculation result

print(art.calculator)        # Display calculator art/logo

while True:
    # Get first number, either fresh input or previous result
    if not use_previous_result:
        num1 = float(input("Enter first number: "))
    else:
        num1 = previous_result

    # Get operation from user and validate
    operator = input("Choose an operation (+, -, *, /): ").strip()
    if operator not in operations:
        print("Invalid operator. Please try again.")
        continue

    # Get second number input
    num2 = float(input("Enter second number: "))

    # Calculate result using chosen operation
    result = operations[operator](num1, num2)

    # Display result
    print(f"Result: {result}")
    previous_result = result  # Save result for potential reuse

    # Ask if user wants to continue calculating with the current result
    continue_choice = input("Continue with the result? (yes/no): ").strip().lower()
    if continue_choice == 'yes':
        use_previous_result = True
    else:
        # Ask if user wants to start a new calculation
        new_calc_choice = input("Start a new calculation? (yes/no): ").strip().lower()
        if new_calc_choice == 'yes':
            use_previous_result = False
            clear_screen()
            print(art.calculator)
        else:
            print("Thank you for using the Python Calculator!")
            break
