import turtle as t
from paddle import Paddle
from pong_ball import Ball
from scoreboard import ScoreBoard
import time

# Set up the game window
screen = t.Screen()
screen.title("Pong Battle")
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off animation for manual screen updates

# Draw the center dashed line
center_line = t.Turtle()
center_line.hideturtle()
center_line.color("white")
center_line.speed("fastest")
center_line.penup()
center_line.goto(0, -300)
center_line.setheading(90)

for _ in range(30):  # Create the dashed effect
    center_line.pendown()
    center_line.forward(20)
    center_line.penup()
    center_line.forward(20)

# Initialize game objects
ball = Ball()
left_paddle = Paddle(position=(-370, 0))
right_paddle = Paddle(position=(370, 0))
scoreboard = ScoreBoard()

# Set up controls
screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.05)  # Delay to control game speed
    screen.update()
    ball.move_ball()

    # Bounce off top or bottom wall
    if ball.wall_collision():
        ball.bounce_y()

    # Right side misses — left scores
    if ball.xcor() > 390:
        scoreboard.left_scores()
        ball.reset_position()

    # Left side misses — right scores
    if ball.xcor() < -390:
        scoreboard.right_scores()
        ball.reset_position()

    # Paddle collision detection
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 340) or \
       (ball.distance(left_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()

screen.exitonclick()
