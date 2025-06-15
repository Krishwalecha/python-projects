import turtle as t

# Constants for text alignment and font style
ALIGNMENT = 'center'
FONT = ('Arial', 12, 'bold')

class Score(t.Turtle):
    def __init__(self):
        """Initializes the Score object with default score and screen setup."""
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=275)
        self.write(f"Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases the score by 1 and updates the display."""
        self.score += 1
        self.clear()  # Clear previous score
        self.write(f"Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self, msg):
        """
        Displays a game over message in the center of the screen.

        Args:
            msg (str): Additional message to display with 'GAME OVER'.
        """
        self.goto(0, 0)
        self.write(f"GAME OVER. {msg}", move=False, align=ALIGNMENT, font=FONT)
