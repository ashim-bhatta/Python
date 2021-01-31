from turtle import  Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.x_move = 8
        self.y_move = 8

    def move_ball(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce(self, type):
        if type == 'wall':
            self.y_move *= -1
        if type == 'paddle':
            self.x_move *= -1
