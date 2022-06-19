import time
import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)

    secretNum = ""

    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])

    return secretNum

def getClues(guess, secretNum):

    if guess == secretNum:
        return 'Great Job, you got it!'
    clues = ['Nope', 'Nope', 'Nope']

    if guess[0] == secretNum[0]:
        clues[0] = 'Correct'
    if guess[1] == secretNum[1]:
        clues[1] = 'Correct'
    if guess[2] == secretNum[2]:
        clues[2] = 'Correct'

    if (guess[0] in secretNum) and (clues[0] != 'Correct'):
        if (guess[0] == guess[1]) and (clues[1] == 'Correct' or clues[1] == 'Almost'):
            clues[0] = 'Nope'
        elif (guess[0] == guess[2]) and (clues[2] == 'Correct' or clues[2] == 'Almost'):
            clues[0] = 'Nope'
        else:
            clues[0] = 'Almost'

    if (guess[1] in secretNum) and (clues[1] != 'Correct'):
        if (guess[1] == guess[0]) and (clues[0] == 'Correct' or clues[0] == 'Almost'):
            clues[1] = 'Nope'
        elif (guess[1] == guess[2]) and (clues[2] == 'Correct' or clues[2] == 'Almost'):
            clues[1] = 'Nope'
        else:
            clues[1] = 'Almost'

    if (guess[2] in secretNum) and (clues[2] != 'Correct'):
        if (guess[2] == guess[1]) and (clues[1] == 'Correct' or clues[1] == 'Almost'):
            clues[2] = 'Nope'
        elif (guess[2] == guess[0]) and (clues[0] == 'Correct' or clues[0] == 'Almost'):
            clues[2] = 'Nope'
        else:
            clues[2] = 'Almost'

    return ' '.join(clues)

def isOnlyDigits(num):
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True

print("This is wordle but with numbers.")
print('I am thinking of a %s-digit number. Try to guess what it is.' % NUM_DIGITS)

time.sleep(1)

print('The clues I give are...')

time.sleep(1)

print('When I say:                              That means:')
print('   Nope                           The digit is incorrect.')
print('   Almost             The digit is correct but in the wrong position.')
print('   Correct            The digit is correct and in the right position.')

time.sleep(1)

while True:
    secretNum = getSecretNum()
    print('You have %s guesses.' % MAX_GUESS)

    guessesTaken = 1

    while guessesTaken <= MAX_GUESS:
        guess = ''

        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print(str(11 - int(guessesTaken)) + ' guesses remaining.')
            print('Guess #%s: ' % guessesTaken)

            guess = input()

        print(getClues(guess, secretNum))
        guessesTaken += 1

        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print('Sorry, you ran out of guesses. The number was %s.' % secretNum)

    print('Would you like to play again? (yes or no)')

    if not input().lower().startswith('y'):
        break
