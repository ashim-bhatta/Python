from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.speed('fastest')
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.food_color = ['red', 'orange', 'blue', 'green', 'yellow', 'purple']
        self.change_food_location()

    def change_food_location(self):
        self.color(random.choice(self.food_color))
        x = random.randint(-320, 320)
        y = random.randint(-320, 300)
        self.goto(x, y)
