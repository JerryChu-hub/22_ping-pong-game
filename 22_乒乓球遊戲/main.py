from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
score_board = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "W")
screen.onkey(l_paddle.go_down, "S")


game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 350:
        ball.bounce_paddle()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_paddle()



    if ball.distance(r_paddle) > 50 and ball.xcor() > 390:
        score_board.l_increase_score()
        ball.reset()

    if ball.distance(l_paddle) > 50 and ball.xcor() < -390:
        score_board.r_increase_score()
        ball.reset()
        

screen.exitonclick()