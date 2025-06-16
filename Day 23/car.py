from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(x=280, y=random.randint(-250, 250))
        self.setheading(180)