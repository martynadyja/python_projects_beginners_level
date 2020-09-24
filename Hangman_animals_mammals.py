#Hangman

import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_word = []
    tries = 7
    print("Let's play Hangman! You have to guess the Animal.")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or a word: ").upper()
        if len(guess) == 1 and guess.isalpha(): #isalpha = method returns True if all the characters are alphabet letters (a-z)
            if guess in guessed_letters:
                print("You already guess the letter,", guess + ".")
            elif guess not in word:
                print(guess, "isn't in the letters.")
                tries -= 1
                guessed_letters.append(guess)
                print(display_hangman(tries))
                print(word_completion)
                print("\n")
            else:
                print("Good job,", guess, "is in the letters!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]  # enumerate = it allows us to loop over something and have an
                                                                                   # automatic counter
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = "True"
                guessed_letters.append(guess)
                print(display_hangman(tries))
                print(word_completion)
                print("\n")
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_word:
                print("You already guess the word,", guess)
            elif guess != word:
                print(guess, "isn't the words.")
                tries -= 1
                guessed_word.append(guess)
                print(display_hangman(tries))
                print(word_completion)
                print("\n")
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
            print(display_hangman(tries))
            print(word_completion)
            print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " +word + ". Maybe next time!")

def display_hangman(tries):
    stages = [    """
                     --------
                     |      |
                     |      0
                     |     \\|/
                     |      |
                     |     / \\
                     -
                  """,
                  """
                     --------
                     |      |
                     |      0
                     |     \\|/
                     |      |
                     |     / 
                     -
                  """,
                  """
                     --------
                     |      |
                     |      0
                     |     \\|/
                     |      |
                     |     
                     -
                  """,
                  """
                     --------
                     |      |
                     |      0
                     |     \\|
                     |      |
                     |     
                     -
                  """,
                  """
                     --------
                     |      |
                     |      0
                     |      |
                     |      |
                     |     
                     -
                  """,
                  """
                     --------
                     |      |
                     |      0
                     |      |
                     |  
                     |     
                     -
                  """,
                  """
                      --------
                      |      |
                      |      0
                      |      
                      |  
                      |     
                      -
                  """,
                  """
                     --------
                     |      |
                     |      
                     |      
                     |  
                     |     
                     -
                  """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Play again? (yes/no) ") == "yes":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
