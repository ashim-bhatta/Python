import random

print("Welcom to number guessing game.")

computer_picked_number = random.randrange(0, 100)


def checking_num(computer_picked, user_guessed):
    """Checking user guessed number matched to computer picked number or not"""
    if computer_picked == user_guessed:
        return f"You got it! answer is {user_guessed}"
    elif computer_picked > user_guessed:
        if computer_picked - user_guessed <= 15:
            return 'You are close, think a little high.'
        else:
            return 'Too low! think more than that.'

    elif computer_picked < user_guessed:
        if user_guessed - computer_picked <= 15:
            return 'You are close, think a little low.'
        else:
            return 'Too high! think a lot less that.'


game_level = input(
    'Choose a difficulty level. Type "easy", "medium" or "hard": ')

if game_level == 'medium':
    no_of_guessing_chance = 7
elif game_level == 'hard':
    no_of_guessing_chance = 4
elif game_level == 'easy':
    no_of_guessing_chance = 10
else:
    no_of_guessing_chance = 7
    print(
        f"You typed wrong '{game_level}' command. So We have picked you medium level."
    )

while no_of_guessing_chance > 0:
    print(f'You have {no_of_guessing_chance} attempts to guess the number.')
    user_guess = input('Make a guess between 0 and 100: ')
    result = checking_num(computer_picked_number, int(user_guess))
    no_of_guessing_chance -= 1
    if no_of_guessing_chance == 0:
        print("You've run out of guesses, You lose this round")
        print(f"Right Number is {user_guess}")
    if result == f"You got it! answer is {int(user_guess)}":
        no_of_guessing_chance = 0

    print(result)