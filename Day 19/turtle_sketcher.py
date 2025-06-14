import turtle as t

# Create turtle and screen objects
turtle = t.Turtle()
screen = t.Screen()
turtle.shape('arrow')
turtle.speed(0)

def move_forward():
    """Move the turtle forward by 10 units."""
    turtle.forward(10)

def move_backward():
    """Move the turtle backward by 10 units."""
    turtle.backward(10)
    
def turn_left():
    """Rotate the turtle 10 degrees counterclockwise."""
    turtle.left(10)

def turn_right():
    """Rotate the turtle 10 degrees clockwise."""
    turtle.right(10)

def clear_and_reset():
    """Clear the drawing and reset turtle to the home position."""
    turtle.penup()
    turtle.clear()
    turtle.home()
    turtle.pendown()

# Keyboard bindings
screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='Up', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='Down', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='Left', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='Right', fun=turn_right)
screen.onkey(key='c', fun=clear_and_reset)

# Exit on screen click
screen.exitonclick()
