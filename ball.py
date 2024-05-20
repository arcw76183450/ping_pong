from turtle import Turtle

BALL_SPEED = 10
SPEED_RATE = 0.5


class Ball(Turtle):
    """
    Turtle object handling the ball movement of the ping pong
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed = 1
        self.x_move = BALL_SPEED
        self.y_move = BALL_SPEED

    def move(self):
        """
        Function responsible for moving the ball at variable speed
        """
        new_x = self.xcor() + self.x_move * self.speed
        new_y = self.ycor() + self.y_move * self.speed
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Function handling the ball bouncing off the edges
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Function handling the ball bouncing off the paddles
        """
        self.speed += SPEED_RATE
        self.x_move *= -1

    def reset_position(self):
        """
        Function responsible for handling reset of ball when point is scored
        """
        self.bounce_x()
        self.speed = 1
        self.goto(0, 0)
