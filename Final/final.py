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

def choose_word():
    with open("words.txt") as f:
        word = random.choice(f.read().splitlines())
    # print("Random word:", word)

def ascii(wrong_guesses):
    print(gallows[wrong_guesses])

def round():
    wrong_guesses = 0
    
#def solved():


def main():
    choose_word()
    round()
    ascii()

if __name__ == "__main__":
    main()