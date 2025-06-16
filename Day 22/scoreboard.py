from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 70, 'bold')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Refresh the score display on screen."""
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)

    def left_scores(self):
        """Increase left player's score and update display."""
        self.left_score += 1
        self.update_scoreboard()

    def right_scores(self):
        """Increase right player's score and update display."""
        self.right_score += 1
        self.update_scoreboard()
