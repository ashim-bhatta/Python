from turtle import Turtle, Screen
from random import choice

pony = Turtle()
pony.speed('fastest')
screen = Screen()
screen.screensize(20000, 20000, 'white')

i = 0
while i < 4:
    pony.right(90)
    pony.forward(100)
    i += 1

for _ in range(50):
    pony.pencolor('black')
    pony.forward(3)
    pony.pencolor('white')
    pony.forward(3)
color = [
    'CornflowerBlue', 'DarkOrchid', 'DeepSkyBlue', 'IndianRed', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen'
]

for i in range(3, 90):
    line_color = choice(color)
    for j in range(i):
        pony.pencolor(line_color)
        pony.forward(30)
        pony.right(360 / i)

direction = [90, 180, 270, 360]
pony.pensize(10)
for _ in range(3000):
    pony.color(choice(color))
    pony.setheading(choice(direction))
    pony.forward(50)

pony.pensize(1)
for i in range(1, 361, 3):
    pony.color(choice(color))
    pony.circle(100)
    pony.right(3)


screen.exitonclick()