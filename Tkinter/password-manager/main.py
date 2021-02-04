from tkinter import *
from tkinter import  messagebox
import random


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)
logo = Canvas(width=200, height=200)
logo_path = PhotoImage(file='logo.png')
logo.create_image(100, 100, image=logo_path)
logo.grid(column=1, row=0)

title_label = Label(text='', font=('calibre', 20, 'normal'))
title_label.grid(column=1, row=1)

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# generating password
def generate_password():
    password_letter = [random.choice(letters) for _ in range(0, 8)]
    password_symbol = [random.choice(symbols) for _ in range(0, 4)]
    password_number = [random.choice(numbers) for _ in range(0, 3)]
    password_list = password_number + password_letter + password_symbol
    random.shuffle(password_list)
    password = ''.join(password_list)
    pass_field.delete(0, 'end')
    pass_field.insert(0, password) 
    window.clipboard_clear()
    window.clipboard_append(password)


# saving password
def save_password():
    email = email_field.get()
    password = pass_field.get()
    website = web_field.get()
    if len(email) == 0 or len(password) == 0 or len(website) == 0:
        title_label.config(text='Empty Field', bg="red")
    elif len(password) <= 8:
        title_label.config(text='Easy Password', bg="red")
    else:
        save = messagebox.askokcancel(title= website, message=f'These are the details you entered: \n  Email: {email}'
                                                       f'\n Password: {password} \n Is it ok to save.')
        if save:
            title_label.config(text='Password Added', bg="white")
            with open('password.txt', 'a') as password_file:
                password_file.write(f'email: {email} | password: {password} | website: {website}\n')
                web_field.delete(0, 'end')
                pass_field.delete(0, 'end')
        else:
            title_label.config(text='Try Again', bg="white")


web_label = Label(text='Website: ', font=('calibre', 10, 'normal'))
email_label = Label(text='Email/UserName: ', font=('calibre', 10, 'normal'))
pass_label = Label(text='Password: ', font=('calibre', 10, 'normal'))

web_label.config(pady=5)
email_label.config(pady=5)
pass_label.config(pady=10)

web_label.grid(column=0, row=2)
email_label.grid(column=0, row=2)
pass_label.grid(column=0, row=4)

# entry field
web_field = Entry(width=40, highlightcolor='green', font=('calibre', 10, 'normal'), bd=0, fg='red')
web_field.focus()
email_field = Entry(width=40, font=('calibre', 10, 'normal'),  bd=0, fg='red')
email_field.insert(0, 'ashim.bhatta000@gmail.com')
pass_field = Entry(width=30, font=('calibre', 10, 'normal'), bd=0, fg='red')
web_field.grid(column=1, row=2, columnspan=2)
email_field.grid(column=1, row=3, columnspan=2)
pass_field.grid(column=1, row=4,)

# buttons
generate_button = Button(text='Generate Password', font=('calibre', 8, 'normal'), command=generate_password)
add_button = Button(text='Add', width=36, font=('calibre', 8, 'normal'), command=save_password )
generate_button.grid(column=2, row=4)
add_button.grid(column=1, row=5, columnspan=3)

mainloop()
