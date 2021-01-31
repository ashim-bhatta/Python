from turtle import Turtle
import time

class Message(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.shape(name=None)
        self.first_player_score = 0
        self.second_player_score = 0
        self.score_track()

    def update_score(self, player):
        self.clear()
        if player == 'first':
            self.first_player_score += 1
            self.score_track()

        elif player == 'second':
            self.second_player_score += 1
            self.score_track()

    def after_score(self):
        self.goto(0, 0)
        self.write(f'{self.first_player_score} | {self.second_player_score}', move=False,
                   font=("Verdana", 35, "normal"), align='center')
        time.sleep(0.5)
        self.clear()
        self.score_track()

    def score_track(self):
        self.goto(-50, 250)
        self.write(f'{self.first_player_score}', move=False,
                   font=("Verdana", 35, "normal"), align='center')
        self.goto(50, 250)
        self.write(f'{self.second_player_score}', move=False,
                   font=("Verdana", 35, "normal"), align='center')