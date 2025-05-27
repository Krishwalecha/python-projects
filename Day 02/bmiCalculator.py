print("Welcome to the Body Mass Index (BMI) Calculator")

# Ask the user for their height and weight
height = float(input("Enter your height (in meters or centimeters): "))
if height > 3:
    height /= 100  # Convert centimeters to meters if needed

weight = float(input("Enter your weight in kilograms: "))

# Calculate BMI and round to two decimal places
bmi = round(weight / (height ** 2), 2)

# Display the BMI result
print(f"\nYour BMI is: {bmi}")

# Interpret and classify the BMI
if bmi >= 25:
    print("You are classified as overweight.")
elif 18.5 <= bmi < 25:
    print("You have a healthy weight.")
else:
    print("You are classified as underweight.")
