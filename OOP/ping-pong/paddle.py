from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def paddle_position(self, x_cor):
        self.goto(x_cor, 0)

    def paddle_move_up(self):
        y = self.ycor()
        x = self.xcor()
        self.goto(x, y + 50)

    def paddle_move_down(self):
        y = self.ycor()
        x = self.xcor()
        self.goto(x, y - 50)
