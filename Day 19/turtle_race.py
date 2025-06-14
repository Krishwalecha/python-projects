import turtle as t
import random

# Set up the screen
screen = t.Screen()
screen.title("Turtle Race")
screen.setup(width=500, height=400)

# Colors and positions
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_positions = [-150, -100, -50, 0, 50, 100, 150]

# Ask user for bet and validate input
user_bet = ""
while user_bet not in rainbow_colors:
    user_bet = screen.textinput(
        title="Make your bet",
        prompt="Which turtle will win the race?\nEnter a color (red/orange/yellow/green/blue/indigo/violet):"
    )
    if user_bet:
        user_bet = user_bet.strip().lower()
    else:
        user_bet = ""

# Draw finish line
finish_line = t.Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.goto(225, -180)
finish_line.left(90)
finish_line.pendown()
finish_line.forward(360)

# Create racers
turtles = []
for index in range(7):
    racer = t.Turtle(shape="turtle")
    racer.color(rainbow_colors[index])
    racer.penup()
    racer.goto(x=-225, y=y_positions[index])
    turtles.append(racer)

# Race logic
winner = None
race_on = True

while race_on:
    for racer in turtles:
        racer.forward(random.randint(1, 10))
        if racer.xcor() >= 225:
            winner = racer.pencolor()
            race_on = False
            break

# Display result
result = t.Turtle()
result.hideturtle()
result.penup()
result.goto(0, 180)
if winner.lower() == user_bet:
    result.write("🎉 Congratulations! You won! 🎉", align="center", font=("Arial", 16, "bold"))
else:
    result.write(f"{winner.capitalize()} won the race. You lost.", align="center", font=("Arial", 16, "bold"))

# Wait for click to exit
screen.exitonclick()
