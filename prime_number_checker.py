def prime_number_checker(number):
    for num in range(2, number):
        if number % num == 0:
            print(f"{number} is not a prime number!!")
            return
    print(f"{number} is a prime number!!")


prime_number_checker((int(input('Number: '))))