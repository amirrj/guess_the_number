import random
import math

while True:

    try:
        low = int(input('Pick the low number'))
        high = int(input('Pick the high number'))
        break
    except:
        print('Please enter a number')


random_number = random.randint(low, high)

chances = round(math.log(high - low + 1, 2))

while True:

    if chances == 0:
        print(f'You have run out of chances, The correct number was {random_number}')
        break

    print(f'You have {chances} chances')
    try:
        user_guess = int(input('Guess the number'))
    except:
        print('Please enter a number')
        continue

    if user_guess == random_number:
        print('Well done you have guessed correctly')
        break

    if user_guess < random_number:
        print('Too low')

    elif user_guess > random_number:
        print('Too high')

    chances -= 1
