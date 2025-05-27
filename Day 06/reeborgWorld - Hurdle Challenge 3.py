# https://shorturl.at/nf92c - Reeborg's World - Hurdle Challenge 3

# Function to turn right by turning left three times
def turn_right():
    for _ in range(3):
        turn_left()

# Function to jump over a hurdle (wall)
def jump():
    turn_left()     
    move()
    for _ in range(2):
        turn_right()
        move()
    turn_left()

number_of_hurdles_jumped = 0

# Loop until the goal is reached
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
        number_of_hurdles_jumped += 1

print(f"Number of hurdles jumped: {number_of_hurdles_jumped}")
