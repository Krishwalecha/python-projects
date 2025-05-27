# https://shorturl.at/ezuqZ - Reeborg's World - Hurdle Challenge 2

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

num_of_hurdles_jumped = 0

# Keep moving and jumping until reaching the goal
while not at_goal():
    move()
    jump()
    num_of_hurdles_jumped += 1

print(f"Number of hurdles jumped: {num_of_hurdles_jumped}")

    