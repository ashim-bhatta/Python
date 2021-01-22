import random

computer_card = []
user_card = []


def deal_card():
    card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(card_deck)


for _ in range(2):
    computer_card.append(deal_card())
    user_card.append(deal_card())


def check_winner():
    print(f'Your final hand: {user_card}, final score : {sum(user_card)}')
    if sum(computer_card) <= 16:
        computer_card.append(deal_card())
    print(
        f'Computer final hand: {computer_card}, final score : {sum(computer_card)}'
    )
    if sum(computer_card) < sum(user_card) and sum(user_card) < 23 or sum(
            computer_card) >= 23:
        print('You won')
    elif (sum(computer_card) == sum(user_card)):
        print('Draw')
    else:
        print('You Lose!!!')


print(f'Your card: {user_card}, current score: {sum(user_card) }')
print(f'Computer first card: {computer_card[0]}')
user_descison = input("Type 'y' to get another card, type 'n' to pass: ")
if user_descison == 'n':
    want_to_continue = False
    check_winner()
else:
    want_to_continue = True

while want_to_continue:
    computer_card.append(deal_card())
    user_card.append(deal_card())
    if sum(user_card) >= 23:
        want_to_continue = False
        print(f'Your final hand: {user_card}, final score : {sum(user_card)}')
        print(f'Computer first card: {user_card[0]}')
        print(
            f'Computer final hand: {computer_card}, final score : {sum(computer_card)}'
        )
        print('You went over')
    else:
        print(f'Your final hand: {user_card}, final score : {sum(user_card)}')
        print(f'Computer first card: {user_card[0]}')
        user_descison = input(
            "Type 'y' to get another card, type 'n' to pass: ")
        if user_descison == 'n':
            want_to_continue = False
            check_winner()
        else:
            want_to_continue = True
