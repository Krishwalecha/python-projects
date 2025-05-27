# https://shorturl.at/h5TA6 - Reeborg's World - Hardle Challenge 4

# Function to turn right by turning left three times
def turn_right():
    for _ in range(3):
        turn_left()

# Function to jump over a hurdle (wall)
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

# Loop until the goal is reached
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
