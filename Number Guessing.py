#Number Guessing

import random

number = random.randrange(1, 100)
number_of_guesses = 0

while number_of_guesses < 3:
    guess = int(input("You have 3 chances to guess the number. Guess a number between 1 and 100: "))
    number_of_guesses += 1
    if guess < number:
        print("You need to guess higher. Try again.")
    if guess > number:
        print("You need to guess lower. Try again.")
    if guess == number:
        break

if guess == number:
    print("You guessed the number correctly in " +str(number_of_guesses) + " tries!")
else:
    print("You didn't guess the number correctly. The number was " +str(number) + ".")



