import turtle as t
import random

class Food(t.Turtle):
    def __init__(self):
        """Initializes the food object with specific shape, color, and position."""
        super().__init__()  
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))
        
    def new_position(self):
        """
        Moves the food to a new random position on the screen.
        Y-coordinate range adjusted to avoid overlapping with scoreboard.
        """
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 270))
