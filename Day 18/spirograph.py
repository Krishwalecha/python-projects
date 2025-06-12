from turtle import Turtle as t, Screen
from random_colors import gen_random_color

turtle = t()
screen = Screen()
screen.colormode(255)
turtle.shape("arrow")
turtle.speed("fastest")
screen.bgcolor('black')

def draw_spirograph(size_of_gap):
    # Draw circles rotated by size_of_gap degrees until full circle is complete
    for _ in range(360 // size_of_gap):
        turtle.color(gen_random_color())   # Set random color
        turtle.circle(200) # Draw circle with radius 200
        # Rotate turtle heading by size_of_gap degrees
        turtle.setheading(turtle.heading() + size_of_gap)

draw_spirograph(5)  # Draw spirograph with 5-degree gap between circles

screen.exitonclick()
