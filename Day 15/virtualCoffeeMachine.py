import credentials
from datetime import datetime
import time
import art
import os

drinks = {
    'Espresso': {
        'water': 50, 
        'coffee': 18, 
        'milk': 0
    },
    'Latte': {
        'water': 200, 
        'coffee': 24, 
        'milk': 150
    },
    'Cappuccino': {
        'water': 250, 
        'coffee': 24, 
        'milk': 100
    }
}

resources = {
    'water': 250,
    'coffee': 76,
    'milk': 150
}

cost = {
    'Espresso': 250,
    'Latte': 300,
    'Cappuccino': 350
}

total_earnings = 0

def print_report(resources):
    """Print current resource levels and total earnings."""
    print(f"Water: {resources['water']} ml")
    print(f"Coffee: {resources['coffee']} mg")
    print(f"Milk: {resources['milk']} ml")
    print(f"Total earnings: {total_earnings} INR")

def get_note_count(denomination):
    """Get count of given currency denomination from user."""
    try:
        count = int(input(f"Number of {denomination} rupees note: "))
        return max(0, count)
    except ValueError:
        print("Invalid input. Assuming 0.")
        return 0

def process_bill(drink):
    """
    Process payment for the selected drink.
    Returns tuple (payment_successful: bool, total_paid: int).
    """
    print(f"Please pay {cost[drink]} INR.")
    total = (
        get_note_count(50) * 50 +
        get_note_count(100) * 100 +
        get_note_count(200) * 200 +
        get_note_count(500) * 500
    )
    
    if total == cost[drink]:
        return True, total
    elif total > cost[drink]:
        print(f"Here's your change of: {total - cost[drink]} INR.")
        return True, total
    else:
        print("Insufficient amount paid. Try again.")
        return False, total

def print_receipt(drink, amount_paid):
    """Print receipt with date, item, cost, amount paid, and change."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\n========== RECEIPT ==========")
    print(f"Date: {now}")
    print(f"Item: {drink}")
    print(f"Amount Paid: {amount_paid} INR")
    print(f"Cost: {cost[drink]} INR")
    if amount_paid > cost[drink]:
        print(f"Change Returned: {amount_paid - cost[drink]} INR")
    else:
        print(f"Change Returned: 0 INR")
    print("Thank you for your purchase!")
    print("=============================\n")

def sufficient_resource(drink):
    """Check if enough resources are available for the chosen drink."""
    for item in drinks[drink]:
        if resources[item] < drinks[drink][item]:
            shortage = drinks[drink][item] - resources[item]
            print(f"Sorry, there is not enough {item}. You need {shortage} more.")
            return False
    return True

def refill_resource():
    """Refill chosen resource by user-input amount."""
    resource = input("Which resource you want to refill? (Water/Coffee/Milk): ").lower()
    try:
        amount = int(input(f"How much you want to refill {resource} by? "))
    except ValueError:
        print("Invalid input, enter numeric value.")
        return
    
    if resource in resources:
        resources[resource] += amount
        print("Refilled successfully!")
    else:
        print("Resource doesn't exist in inventory, try again!")

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print(art.coffee)
    print("Welcome to Virtual Coffee Machine!")
    drink_input = input('What would you like? (Espresso/Latte/Cappuccino): ').strip().lower()

    if drink_input == 'off':
        # Admin login to shut down machine
        while True:
            name = input("Enter your username: ").capitalize()
            try:
                password = int(input("Enter your password: "))
            except ValueError:
                print("Password must be numeric.")
                continue
            
            if name == credentials.ADMIN_NAME and password == credentials.ADMIN_PASSWORD:
                print("Goodbye!")
                exit()
            else:
                print("Invalid credentials. Try again.")
                choice = input("Press Enter to continue or type 'exit' to return to the main menu: ").strip().lower()
                if choice == 'exit':
                    break

    elif drink_input == 'report':
        print_report(resources)

    elif drink_input == 'refill':
        refill_resource()

    elif drink_input.title() in drinks:
        drink = drink_input.title()
        if sufficient_resource(drink):
            success, amount_paid = process_bill(drink)
            if success:
                print(f"Dispensing your {drink} ...")
                time.sleep(1)
                print(f"Here's your {drink}. Thank you for trying out Virtual Coffee Machine.")
                for resource in drinks[drink]:
                    resources[resource] -= drinks[drink][resource]
                total_earnings += cost[drink]
                print_receipt(drink, amount_paid)
    else:
        print("Invalid option. Please choose a valid drink.")

    time.sleep(5)
    clear_screen()
