import turtle as t
import os

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

        # Safe file path handling for compatibility
        self.file_path = os.path.join("Day 20 and 21", "high_score.txt")
        try:
            with open(self.file_path) as file:
                contents = file.read()
            self.high_score = int(contents)
        except (FileNotFoundError, ValueError):
            self.high_score = 0

        self.write(f"Score = {self.score} | High score = {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases the score by 1 and updates the display."""
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears and updates the scoreboard with current and high scores."""
        self.clear()
        self.write(f"Score = {self.score} | High score = {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        """Resets the score and updates the high score file if needed."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open(self.file_path, mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
