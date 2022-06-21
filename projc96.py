import random

i = 0

num1 = random.randint(0, 9)

# print(num1)

state = 'start'

while(i < 5):

    i += 1

    guess = int(input('Guess: '))

    if(guess > num1):
        print('Too high!')

    elif(guess < num1):
        print('Too low!')

    elif(guess == num1):
        print('You guessed it!')
        state = 'win'

    if state == 'win':
        break

if(not i < 3 and state != 'win'):
    print('You lost!')
