'''
Final Project: Hangman
By: Liam Cleckner
CSCI 110
Date: 11/22/2025
'''

import random

gallows = {
    '''
      _______
     |       |
             |
             |
             |
             |
             |
    ============         
    ''', 
    '''
      _______
     |       |
     O       |
             |
             |
             |
             |
    ============         
    ''',
    '''
      _______
     |       |
     O       |
     |       |
             |
             |
             |
    ============         
    ''',
    '''
      _______
     |       |
     O       |
    /|       |
             |
             |
             |
    ============         
    ''',
    '''
      _______
     |       |
     O       |
    /|\\        |
             |
             |
             |
    ============         
    ''',
    '''
      _______
     |       |
     O       |
    /|\\      |
    /        |
             |
             |
    ============         
    ''',
    '''
      _______
     |       |
     O       |
    /|\\      |
    / \\      |
             |
             |
    ============
    '''

}

max_tries = len(gallows) - 1

def choose_word():
    with open("words.txt") as f:
        word = random.choice(f.read().splitlines())
    # print("Random word:", word)

def round(word):
    wrong_guesses = 0
    guessed = set()
    
    while True:
        ascii(word, guessed, wrong_guesses)

        if word_solved():
            print("You won! \nSecret word: ", word)
        
        if wrong_guesses >= max_tries:
            print("Game over :( \nSecret word:", word)

        letter = letter_input(guessed)
        if letter == "quit":
            print("Game over. \nThe word was", word)
        if letter in word:
            guessed.addletter
            print("Good guess.", letter)
        else:
            guessed.addletter
            wrong_guesses += 1
            print("Bad guess.", letter)

def letter_input(guessed):
    while True:
        letter_guess = input("(To leave, type quit) Guess a letter: ").strip().lower
        if letter_guess == quit:
            return letter_guess
        if letter_guess in guessed:
            print("Already guessed that letter!")
            continue
        if len(letter_guess) != 1 or not letter_guess.isalpha:
            print("Please etner one letter.")
            continue
        return letter_guess
            
def word_solved(word, guessed):
    return all(letter in guessed for letter in word)


def ascii(word, guessed, wrong_guesses):
    print(gallows[wrong_guesses])
    mask = "".join(letter if letter in guessed else "_" for letter in word)
    print("Word:", mask, f"({len(word)} letters)")
    print("Guessed:", " ".join(sorted(guessed)) if guessed else "(none)")
    print("Tries left:", max_tries - wrong_guesses)

def play_again():
    while True:
        ans = input("Play again? (y/n)").strip().lower()[0]


def main():
    print("Welcome to my hangman game!")
    while True:
        word = choose_word()
        round(word)

if __name__ == "__main__":
    main()