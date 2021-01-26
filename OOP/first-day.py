# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('green')
# timmy.speed(50)
# timmy.forward(105)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table =  PrettyTable()
table.add_column('Name', ['Naomi', 'Saroj', 'Anup'])
table.add_column('Age', [21, 22, 20])
table.add_row(['love', 'what'])
table.align = 'r'
print(table)
