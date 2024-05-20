from turtle import Turtle

FONT_CONFIG = ("Arial", 34, "bold")


class Scoreboard(Turtle):
    """
    Turtle object handling the scoring of the game
    """
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.goto(0, 260)
        self.score_left = 0
        self.score_right = 0
        self.update_score()

    def update_score(self):
        """
        Function responsible for any sort of score update
        """
        self.clear()
        self.write(f"{self.score_left}:{self.score_right}", align="center", font=FONT_CONFIG)

    def update_score_right(self):
        """
        Handle the score update for right paddle
        """
        self.score_right += 1
        self.update_score()

    def update_score_left(self):
        """
        Handle the score update for right paddle
        """
        self.score_left += 1
        self.update_score()
