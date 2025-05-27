print("Welcome to the Tip Calculator")

# Get user input for currency, total bill, tip percentage, and number of people
currency = input("Enter the currency you want to use (e.g., INR, $, €, £): ")
total_bill = float(input(f"What was the total bill amount in {currency}? "))
tip = float(input("What percentage tip would you like to leave? (e.g., 5, 10, 15): "))
splitters = int(input("How many people are splitting the bill? "))

# Calculate tip, final amount, and per-person share
tip_amount = (tip / 100) * total_bill
final_bill = total_bill + tip_amount
bill_per_person = final_bill / splitters

# Display the results
print(f"\nTotal bill (including tip): {currency} {round(final_bill, 2)}")
print(f"Each person should pay: {currency} {round(bill_per_person, 2)}")

print("\nThank you for using the Tip Calculator!")
