# https://shorturl.at/pdWrm - Reeborg's World - Escaping the maze

# Function to turn right by turning left three times
def turn_right():
    for _ in range(3):
        turn_left()

# Loop until the goal is reached
while not at_goal():
    if right_is_clear() and front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
