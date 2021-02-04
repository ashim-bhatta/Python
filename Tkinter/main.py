from tkinter import *

window = Tk()
window.title('This is tkinter window...')
window.minsize(width=600, height=400)
label = Label(text='This is label', font=('Arial', 22))
label.pack()


def handle_click():
    user_input = input.get()
    label.config(text=user_input)


button = Button(text='Click ME', command=handle_click)
button.pack()

input = Entry(width=20)
input.pack()

mainloop()
