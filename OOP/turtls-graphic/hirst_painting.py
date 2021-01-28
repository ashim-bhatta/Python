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

tim.penup()

tim.speed('fastest')
tim.shape('circle')
tim.setheading(220)
tim.forward(400)
tim.setheading(0)
direction = 'left'

for _ in range(10):
    for _ in range(10):
        tim.dot(20, choice(random_colors))
        tim.forward(50)
    if direction == 'left':
        tim.backward(50)
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        direction = 'right'
    else:
        tim.backward(50)
        tim.right(90)
        tim.forward(50)
        tim.right(90)
        direction = 'left'

screen = t.Screen()
screen.exitonclick()