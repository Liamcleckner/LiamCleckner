'''
Final Project: Hangman
By: Liam Cleckner
CSCI 110
Date: 11/22/2025
'''

import os
import random

gallows:  {
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
    print("Random word:", word)

choose_word()