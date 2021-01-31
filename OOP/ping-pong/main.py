from turtle import  Screen
from paddle import Paddle
from ball import Ball
from message import Message
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

left_paddle = Paddle()
left_paddle.paddle_position(-390)
right_paddle = Paddle()
right_paddle.paddle_position(380)
ball = Ball()
message = Message()


is_game_on = True
while is_game_on:
    screen.listen()
    screen.update()
    screen.onkey(key='w', fun=left_paddle.paddle_move_up)
    screen.onkey(key='s', fun=left_paddle.paddle_move_down)
    screen.onkey(key='Up', fun=right_paddle.paddle_move_up)
    screen.onkey(key='Down', fun=right_paddle.paddle_move_down)
    time.sleep(0.03)
    ball.move_ball()

    # detecting collision on up and down wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce('wall')

    # detecting collision on right wall
    if ball.xcor() > 390:
        ball.goto(0, 0)
        message.update_score('first')
        ball.bounce('paddle')
        message.after_score()

    # detecting collision on left wall
    if ball.xcor() < -390:
        ball.goto(0, 0)
        message.update_score('second')
        ball.bounce('paddle')
        message.after_score()

    # detecting collision on right and left paddle
    if ball.distance(left_paddle) <= 50 and ball.xcor() > -390 or ball.distance(right_paddle) <= 50 and ball.xcor() < 380:
        ball.bounce('paddle')

screen.exitonclick()