import turtle
import pandas as pd

# Setup turtle
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
writer.speed("fastest")

# Setup screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"Day 25\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load data
states_data = pd.read_csv(r"Day 25\50_states.csv")
states_names = states_data["state"].to_list()

# Track guesses
guessed_states = []

def check_answer(guess):
    """Check user's guess, mark it on the map if correct."""
    if guess in states_names and guess not in guessed_states:
        guessed_states.append(guess)
        state_row = states_data[states_data["state"] == guess]
        x = int(state_row["x"].iloc[0])
        y = int(state_row["y"].iloc[0])
        writer.goto(x, y)
        writer.write(arg=guess, align="center", font=("Courier", 8, "bold"))

# Game loop
while len(guessed_states) < 50:
    user_guess = screen.textinput(
        title="U.S. States Quiz",
        prompt=f"Name a U.S. state:\nYou have guessed {len(guessed_states)} out of 50 states."
    )
    
    if user_guess is None:  # User clicked Cancel
        break
    
    check_answer(user_guess.capitalize())

screen.exitonclick()
