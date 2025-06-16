import turtle as t
import time
from snake import Snake
from snake_food import Food
from score_board import Score

# Screen setup
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create game objects
snake = Snake()
food = Food()
score_board = Score()

# Key bindings
screen.listen()
screen.onkey(snake.up, "Up" )
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()

    # Detect collision with Food
    if food.distance(snake.head) < 15:
        food.new_position()
        score_board.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.wall_collision():
        score_board.reset()
        snake.reset()

    # Detect collision with tail
    if snake.tail_collision():
        score_board.reset()
        snake.reset()
