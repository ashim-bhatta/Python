from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()


def move_forward():
    pen.forward(10)


def move_backward():
    pen.backward(10)


def move_up():
    pen.left(10)


def move_down():
    pen.right(10)


pen_statue = True


def pen_up_down():
    global pen_statue
    if pen_statue:
        pen.penup()
        pen_statue = False
    else:
        pen.pendown()
        pen_statue = True

def clear():
    pen.clear()
    pen.home()


screen.listen()
screen.onkey(key='d', fun=move_forward)
screen.onkey(key='Right', fun=move_forward)
screen.onkey(key='d', fun=move_backward)
screen.onkey(key='Left', fun=move_backward)
screen.onkey(key='w', fun=move_up)
screen.onkey(key='Up', fun=move_up)
screen.onkey(key='s', fun=move_down)
screen.onkey(key='Down', fun=move_down)
screen.onkey(key='c', fun=clear)
screen.onkey(key='space', fun=pen_up_down)
screen.exitonclick()
