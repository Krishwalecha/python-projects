from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        """Update ball's position based on its current trajectory."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_collision(self):
        """Detect collision with the top or bottom wall."""
        return self.ycor() > 280 or self.ycor() < -280

    def bounce_y(self):
        """Reverse vertical movement when hitting top/bottom."""
        self.y_move *= -1

    def bounce_x(self):
        """Reverse horizontal movement (on paddle bounce)."""
        self.x_move *= -1

    def reset_position(self):
        """Center the ball and reverse horizontal direction after scoring."""
        self.goto(0, 0)
        self.bounce_x()
