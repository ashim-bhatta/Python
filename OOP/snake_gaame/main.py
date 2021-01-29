from turtle import Screen, Turtle
from food import Food
from score import Score
import time
import snake

screen = Screen()
screen.tracer(n=0)
screen.setup(width=700, height=700)
screen.bgcolor('black')
screen.title('Snake Game')

snake_game = snake.Snake()
snake_food = Food()
score = Score()

screen.listen()
screen.onkey(fun=snake_game.up, key='Up')
screen.onkey(fun=snake_game.down, key='Down')
screen.onkey(fun=snake_game.left, key='Left')
screen.onkey(fun=snake_game.right, key='Right')

is_game_on = True
while is_game_on:
    screen.update()
    snake_game.move()

    # detect collision with food
    if snake_game.head.distance(snake_food) < 20:
        snake_food.change_food_location()
        score.update_score()
        snake_game.extend_snake()

    # detect collision with wall
    if snake_game.head.xcor() > 338 or snake_game.head.xcor() < -340 or snake_game.head.ycor() > 320 or snake_game.head.ycor() < -320:
        score.game_over()
        is_game_on = False
        # x = snake_game.head.xcor()
        # y = snake_game.head.ycor()
        # snake_game.head.goto(-x, y)
    # elif snake_game.head.ycor() > 320 or snake_game.head.ycor() < -320:
    #     x = snake_game.head.xcor()
    #     y = snake_game.head.ycor()
    #     snake_game.head.goto(x, -y)

    # detect collision with body parts
    for snake_part in snake_game.snake_body[2:]:
        if snake_game.head.distance(snake_part) < 20:
            score.game_over()
            is_game_on = False

    # updating snake speed according to snake length
    if len(snake_game.snake_body) < 4:
        time.sleep(0.3)
    elif len(snake_game.snake_body) < 9:
        time.sleep(0.25)
    elif len(snake_game.snake_body) < 15:
        time.sleep(0.2)
    elif len(snake_game.snake_body) < 20:
        time.sleep(0.15)
    elif len(snake_game.snake_body) < 25:
        time.sleep(0.1)
screen.exitonclick()
