# https://shorturl.at/LI0UH - Reeborg's World - Hurdle Challenge 1

# Function to turn right by turning left three times
def turn_right():
    for _ in range(3):
        turn_left()

# Function to jump over a hurdle (wall)
def jump():
    turn_left()
    for _ in range(2):
        move()
        turn_right()
    move()
    turn_left()

number_of_hurdles = 6  # Total number of hurdles to jump

# Loop to jump over all hurdles
for _ in range(number_of_hurdles):
    move()
    jump()
