# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.

random_person = {
    'first_name': 'Ashim',
    'last_name': 'Bhatta',
    'age': 21,
    'city': 'Kathmandu'
}
name = random_person['first_name'] + random_person['last_name']
age = {random_person['age']}
city = {random_person['city']}
print(f'My name is {name} and I am {age} years old. I live in {city}.')
print(random_person['age'])

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.

people_fav_num = {
    'Ashim': 3,
    'Nishal': 17,
    'Mugi': 493,
    'Jatthi': 453,
    'Pooja': 56234
}

print(people_fav_num.get('Ashim'))
print(people_fav_num.get('Nishal'))
print(people_fav_num.get('Mugi'))
print(people_fav_num.get('Jatthi'))
print(people_fav_num.get('Pooja'))

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# •	 Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# •	 Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

thingh_I_learned = {'List': 'none'}

# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# •	 Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.

rivers = {'egypt': 'nile', 'nepal': 'trishuli', 'austrila': 'darling'}

for country, river in rivers.items():
    print(f'The {river.title()} runs through {country.title()}')

# 6-6. Polling: Use the code in favorite_languages.py (page 97).
# •	 Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# •	 Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

peoples = ['ashim', 'nishal', 'saroj', 'selena', 'rachel', 'kevin', 'kaira']
poles = {'ashim': 'python', 'selena': 'c', 'kaira': 'ruby'}

for name in peoples:
    if name not in poles:
        print('\n')
        print(f'{name.title()}, I would like you to take part in our poll.')
    else:
        print('\n')
        print(f'{name.title()}, thank you got taking out poll.')
