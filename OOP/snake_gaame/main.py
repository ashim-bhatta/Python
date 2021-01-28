from turtle import Turtle, Screen
import time
import snake
screen = Screen()
screen.tracer(n=0)
screen.setup(width=700, height=700)
screen.bgcolor('black')
screen.title('Snake Game')

snake_game = snake.Snake()
screen.listen()
screen.onkey(fun=snake_game.up, key='Up')
screen.onkey(fun=snake_game.down, key='Down')
screen.onkey(fun=snake_game.left, key='Left')
screen.onkey(fun=snake_game.right, key='Right')

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.3)
    snake_game.move()

screen.exitonclick()