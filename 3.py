# 1 Names: Store the names of a few of your friends in a list called names. Print each person's name by accessing
# each element in the lists, one at a time.

names = ['Naomi', 'Saroj', 'Anup']
for name in names:
    print(name)

# 2 Greeting: Start with the list you used in Exercise 3-1, but instead of just printing each person's name,
# print a message to them. The text of each message should be the same, but each message should be personalized with
# the person's name.

for name in names:
    print(name, ', Welcome to my friend zone.')

# 3 Your Own List: Think of your favourite mode of transportation, such as a motorcycle or a car, and make a list
# that stores examples. Use your list to print a series of statements about these items, such as "I would like to own
# a Honda motorcycle."

cars = ['BMW', 'Tesla', 'Porsche', 'Jaguar', 'Kia', 'Audi']

for car in cars:
    print(f'I love {car}.')
    print(f'One day I will like to own a {car}.')
