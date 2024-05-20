from __future__ import annotations

from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

# Screen config
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping pong")
screen.tracer(0)


def exit_program():
    """
    Function to exit the game by shutting off Turtle
    """
    screen.bye()


def key_listeners(left, right):
    """
    Handles all the key press interactions in the game
    :param left: the turtle object of left paddle
    :param right: the turtle object of the right paddle
    """
    screen.listen()
    screen.onkeypress(left.go_up, "w")
    screen.onkeypress(left.go_down, "s")
    screen.onkeypress(right.go_up, "Up")
    screen.onkeypress(right.go_down, "Down")
    screen.onkey(exit_program, "x")


def ping_pong():
    """
    The driver code of the game
    :return:
    """
    paddle_left = Paddle((-350, 0))
    paddle_right = Paddle((350, 0))
    key_listeners(paddle_left, paddle_right)
    ball = Ball()
    scoreboard = Scoreboard()
    is_game_on = True
    while is_game_on:
        time.sleep(0.1)
        screen.update()
        if ball is not None:
            ball.move()
            # detect collision with wall
            if ball.ycor() > 285 or ball.ycor() < -285:
                ball.bounce_y()
            # detect collision with paddle_right
            if (ball.distance(paddle_right) < 50 and ball.xcor() > 320 or
                    ball.distance(paddle_left) < 50 and ball.xcor() < -320):
                ball.bounce_x()
            # detect ball is out of bounds
            if ball.xcor() > 380:
                ball.reset_position()
                scoreboard.update_score_left()
            if ball.xcor() < -380:
                ball.reset_position()
                scoreboard.update_score_right()
    screen.exitonclick()


if __name__ == '__main__':
    ping_pong()
