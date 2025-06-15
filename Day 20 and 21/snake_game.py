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

game_is_on = True

snake = Snake()
food = Food()
score_board = Score()

screen.listen()
screen.onkey(snake.up, "Up" )
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()

    # Detect collision with Food
    if food.distance(snake.head) < 15:
        food.new_position()
        score_board.increase_score()
        snake.extend()

    if snake.wall_collision():
        game_is_on = False
        score_board.game_over("YOU COLLIDED WITH THE WALL!")
    
    if snake.tail_collision():
        game_is_on = False
        score_board.game_over("YOU RAN INTO YOUR OWN TAIL!")

screen.exitonclick()
