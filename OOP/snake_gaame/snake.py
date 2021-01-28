from turtle import Turtle, Screen


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        x_axis = 0
        for _ in range(0, 3):
            snake_part = Turtle('square')
            snake_part.color('white')
            snake_part.penup()
            snake_part.speed('slow')
            snake_part.pensize(1)
            snake_part.goto(x_axis, 0)
            self.snake_body.append(snake_part)
            x_axis -= 20

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