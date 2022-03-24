from turtle import Screen, Turtle
from field import Field
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

EDGE_X = 400
EDGE_Y = 300

screen = Screen()
screen.setup(width=EDGE_X*2, height=EDGE_Y*2)
screen.title('Ping Pong')
screen.bgcolor('black')
screen.tracer(0)

field = Field()
paddle_r = Paddle(EDGE_X-50)
paddle_l = Paddle(-(EDGE_X-50))

screen.listen()
screen.onkeypress(paddle_r.up, "Up")
screen.onkeypress(paddle_r.down, "Down")
screen.onkeypress(paddle_l.up, "s")
screen.onkeypress(paddle_l.down, "x")

ball = Ball()
scoreboard = Scoreboard()

is_on = True
while is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with edges
    if ball.ycor() > (EDGE_Y-10) or ball.ycor() < -(EDGE_Y-10):
        ball.bounce_y()

    # Detect collision with right paddle
    if (ball.xcor() > 320 and ball.distance(paddle_r) < 50) or (ball.xcor() < -320 and ball.distance(paddle_l) < 50):
        ball.bounce_x()

    # Detect right paddle miss ball
    if ball.xcor() > EDGE_X:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -EDGE_X:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
