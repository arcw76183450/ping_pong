from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    """
    The turtle object for paddles in the game
    """

    def __init__(self, location):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(location)

    def go_up(self):
        """
        Function responsible for paddle to move up
        """
        if self.ycor() < 280:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def go_down(self):
        """
        Function responsible for paddle to move down
        """
        if self.ycor() > -280:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
