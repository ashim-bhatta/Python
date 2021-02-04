with open('text1.txt', 'r') as file:
    number1 = file.readlines()


with open('text2.txt', 'r') as file:
    number2 = file.readlines()

result = [int(num.strip()) for num in number1 if num in number2]
print(result)


