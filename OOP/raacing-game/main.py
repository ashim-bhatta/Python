from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_color = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race?? Enter the color: ")
turtleList = ['red', 'orange', 'blue', 'green', 'yellow', 'purple']
x = -230
y = -150
turtle_dict = {}
for tut in turtleList:
    turtle_dict[tut] = Turtle('turtle')
    turtle_dict[tut].penup()
    turtle_dict[tut].color(tut)
    turtle_dict[tut].goto(x=x, y=y)
    y += 60

is_race_on = True
while is_race_on:
    for tut in turtleList:
        turtle_dict[tut].pendown()
        if turtle_dict[tut].xcor() > 220:
            is_race_on = False
            if user_color == tut:
                print(f"You've won, {tut} color turtle won the race.")
            else:
                print(f'Opps {tut} color turtle won the race.')
            pass
        move_value = random.choice(range(0, 11))
        turtle_dict[tut].forward(move_value)


screen.exitonclick()
