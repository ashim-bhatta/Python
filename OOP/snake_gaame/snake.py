from turtle import Turtle, Screen
import random
snake_color = ['red', 'orange', 'blue', 'green', 'yellow', 'purple']

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.head.shape('circle')

    def create_snake(self):
        x_axis = 0
        for _ in range(0, 3):
            self.add_snake_part(x_axis, 0, random.choice(snake_color))
            x_axis -= 20

    def add_snake_part(self, x, y, color):
        snake_part = Turtle('square')
        snake_part.color(color)
        snake_part.shapesize(stretch_wid=0.7)
        snake_part.penup()
        snake_part.goto(x, y)
        self.snake_body.append(snake_part)

    def extend_snake(self):
        x = self.snake_body[- 1].xcor()
        y = self.snake_body[- 1].xcor()
        self.add_snake_part(x, y, random.choice(snake_color))

    def move(self):
        for snake_pos in range(len(self.snake_body) - 1, 0, -1):
            x = self.snake_body[snake_pos - 1].xcor()
            y = self.snake_body[snake_pos - 1].ycor()
            self.snake_body[snake_pos].goto(x, y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() == 270:
            return
        self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            return
        self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0:
            return
        self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180:
            return
        self.head.setheading(0)