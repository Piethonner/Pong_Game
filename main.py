from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor("black")
screen.title("PONG#")
screen.tracer(0)

ball = Ball()
score = Scoreboard()

# Creates paddles
r_paddle = Paddle((450, 0))
l_paddle = Paddle((-450, 0))
paddle_hit = 0

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Collision with wall
    if ball.ycor() > 385 or ball.ycor() < -385:
        ball.bounce_y()

    # Collision with paddles
    if paddle_hit == 0:
        if ball.distance(r_paddle) < 45 and ball.xcor() > 360 or ball.distance(l_paddle) < 45 and ball.xcor() < -360:
            ball.bounce_x()
            paddle_hit = 1
    else:
        if -300 < ball.xcor() < 300:
            paddle_hit = 0

    # Right Miss
    if ball.xcor() > 440:
        ball.reset_position()
        score.l_point()

    # Left Miss
    if ball.xcor() < -440:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
