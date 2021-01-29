from turtle import  Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_value = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 320)
        self.shape(name=None)
        self.write(f'Score : {self.score_value}', move=False, font=("Verdana", 20, "normal"), align='center')

    def update_score(self):
        self.score_value += 1
        self.clear()
        self.write(f'Score : {self.score_value}', move=False, font=("Verdana", 20, "normal"), align='center')

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over', move=False, font=("Verdana", 20, "normal"), align='center')
