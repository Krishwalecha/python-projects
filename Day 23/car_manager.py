import random
from car import Car

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 6) == 1:  # Approx every 6 loops
            new_car = Car()
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
