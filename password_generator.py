import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ''
password_list = []

print('Welcome to python generator')
nr_letters = int(input('How many letters would you like in your password?\n'))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for num in range(nr_letters):
    password_list += random.choice(letters)
for num in range(nr_symbols):
    password_list += random.choice(symbols)
for num in range(nr_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)

for alpha in password_list:
    password += alpha

f = open("password.txt", "w+")
f.write(f'Your Password: {password}')
print(f'Your Password: {password}')
print(
    f'You can check Password.txt file for your password in same directory :-)')
