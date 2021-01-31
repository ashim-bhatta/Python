names = []

# open file and read the content in a list
with open('./Input/Names/invited_names.txt', 'r') as files:
    for line in files:
        currentName = line[:-1]
        names.append(currentName)
print(names)

for name in names:
    with open('./Input/Letters/starting_letter.txt') as files:
        for line in files:
            a = line.replace('[name]', name)
            with open(f'./Output/ReadyToSend/letter_for_{name}.txt', 'a') as writeFile:
                writeFile.write(a)
