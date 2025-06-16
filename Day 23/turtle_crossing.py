import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
game_active = True  # controls movement/spawning

screen.listen()
screen.onkey(player.move_forward, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if game_active:
        car_manager.create_car()
        car_manager.move_cars()

        # Check collision
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                scoreboard.game_over()
                screen.onkey(None, "Up")  # Disable movement
                game_active = False       # Stop updates
                
        # Check crossing
        if player.ycor() > 280:
            player.reset_position()
            car_manager.increase_speed()
            scoreboard.increment_level()


