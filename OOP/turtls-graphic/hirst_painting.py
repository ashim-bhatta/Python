import colorgram
import turtle as t
from random import choice
t.colormode(255)
tim = t.Turtle()

random_colors = []
colors = colorgram.extract('images.jpg', 30)
for color in colors:
    rgb = color.rgb
    if rgb[0] >= 230 or rgb[1] >= 220 or rgb[2] >= 220:
        random_colors = random_colors
    else:
        random_colors.append((rgb[0], rgb[1], rgb[2]))


def forward_without_mark(num):
    tim.penup()
    tim.forward(num)
    tim.pendown()


tim.speed('fastest')
tim.shape('circle')
tim.setheading(220)
forward_without_mark(400)
tim.setheading(0)
direction = 'left'

for _ in range(10):
    for _ in range(10):
        tim.dot(20, choice(random_colors))
        forward_without_mark(50)
    if direction == 'left':
        tim.penup()
        tim.backward(50)
        tim.pendown()
        tim.left(90)
        forward_without_mark(50)
        tim.left(90)
        direction = 'right'
        print(direction)
    else:
        tim.penup()
        tim.backward(50)
        tim.pendown()
        tim.right(90)
        forward_without_mark(50)
        tim.right(90)
        direction = 'left'
        print(direction)

screen = t.Screen()
screen.exitonclick()