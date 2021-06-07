# Guess the numbers in a list game
import random

print('Welcome to the "Guess the random numbers in a list" game.' + '\nPlease guess the five numbers in a randomly generated list. \nNumbers are from 1 to 50. Good luck!\n')

randlist = []
for i in range(0, 5):
    secret = random.randint(1,50)
    if secret in randlist:
        secret = random.randint(1,50)
    else:
        randlist.append(secret)

# Debug mode. Remove comment tags to enable debug
print('DEBUG MODE')
print(randlist)

points = 0
guesses = 0
answers = []
guessed = []

# While loop until list is empty
while len(randlist) > 0:
    print('\nPlease guess a number from 1 to 50. If the number is in the list, you are granted five points. If not, you lose a point.')
    try:
        guess = int(input())
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess in randlist:
        print('You guessed ' + str(guess) + ', which was part of the list!')
        answers.append(guess)
        randlist.remove(guess)
        guesses = guesses + 1
        points = points + 5
        print('You are currently at ' + str(guesses) + ' guesses and ' + str(points) + ' points!')
        if len(randlist) == 0:
            print('\nThe game is over. You successfully guessed all numbers in ' + str(guesses) + ' guesses.')
            print('You finished with ' + str(points) + ' points.')
            print('The correct answers are as follows: ' + str(answers))
        else:
            continue
    elif guess not in randlist:
        if guess in guessed:
            print("You've already guessed that number. Please try again.")
        else:
            print("The number you guessed was not in the list.")
            guesses = guesses + 1
            guessed.append(guess)
            points = points - 1
            print('You are currently at ' + str(guesses) + ' guesses and ' + str(points) + ' points!')
