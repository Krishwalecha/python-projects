import color_extractor
import turtle as t
import random

# Setup turtle and screen
turtle = t.Turtle()
screen = t.Screen()
t.colormode(255)           
turtle.shape('arrow')
turtle.speed("fastest")    
turtle.pu()
turtle.hideturtle()

# Move turtle to starting position (bottom-left-ish)
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)       # Face right

# Extract colors from the image
color_extractor.extract_colors('Day 18/hirst_painting.jpg', 50)

number_of_dots = 100 # Total dots to draw

# Draw dots in a 10x10 grid
for dot_count in range(1, number_of_dots + 1):
    turtle.dot(20, random.choice(color_extractor.colors_list))  # Draw dot with random extracted color
    turtle.fd(50)   # Move forward to next dot position

    if dot_count % 10 == 0:  # Every 10 dots, move up and back to start of new row
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

screen.exitonclick()
