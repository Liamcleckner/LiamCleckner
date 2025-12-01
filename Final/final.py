'''
Final Project: Hangman
By: Liam Cleckner
CSCI 110
Date: 11/22/2025
Algorithm steps:
- Pick a random word from words.txt
- Set wrong guesses = 0, guessed letters = empty set
- Loop round
    Show ASCII gallows, masked word, guessed letters, and tries left
- Check win/lose
    If all letters guessed you win
    If wrong guesses >= max you lose
- Get input from player
- Update 
    If letter in word add to guessed 
    Else add to guessed and increase wrong guesses
- Repeat until win, lose, or quit
- Ask to play again
'''

import random


#acii art

gallows = [
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
    /|\\      |
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

]

max_tries = len(gallows) - 1

#Random word from words.txt
def choose_word():
    with open("words.txt") as f:
        word = random.choice(f.read().splitlines())
    return word.lower()
    # print("Random word:", word)

#Plays one round
#Each incorrect guess adds one to wrong_guesses
#Each correct guess is kept
#Each guess put in the word bank
def play_round(word):
    wrong_guesses = 0
    guessed = set()
    
    while True:
        ascii(word, guessed, wrong_guesses)

        if word_solved(word, guessed):
            print("You won! \nSecret word: ", word)
            return
        
        if wrong_guesses >= max_tries:
            print("Game over :( \nSecret word:", word)
            return

        letter = letter_input(guessed)
        if letter == "quit":
            print("Game over. \nThe word was", word)
            return
    
        if letter in word:
            guessed.add(letter)
            print("Good guess.", letter)

        else:
            guessed.add(letter)
            wrong_guesses += 1
            print("Bad guess.", letter)

#Checks for a valid single lietter input
def letter_input(guessed):
    while True:
        letter_guess = input("(To leave, type quit) Guess a letter: ").strip().lower()
        if letter_guess == "quit":
            return letter_guess
        if letter_guess in guessed:
            print("Already guessed that letter.")
            continue
        if len(letter_guess) != 1 or not letter_guess.isalpha():
            print("Please enter one letter.")
            continue
        return letter_guess

#Checks if word is solved     
def word_solved(word, guessed):
    return all(letter in guessed for letter in word)

#Display
def ascii(word, guessed, wrong_guesses):
    print(gallows[wrong_guesses])
    mask = "".join(letter if letter in guessed else "_" for letter in word)
    print("Word:", mask, f"({len(word)} letters)")
    print("Guessed:", " ".join(sorted(guessed)) if guessed else "(none)")
    print("Tries left:", max_tries - wrong_guesses)

#Asks to play again
def play_again():
    while True:
        ans = input("Play again? (y/n)").strip().lower()[0]
        if ans == "y":
            return True
        if ans == "n":
            return False


def main():
    print("Welcome to my hangman game!")
    while True:
        word = choose_word()
        play_round(word)
        if not play_again():
            print("Thanks for playing!!")
            break

if __name__ == "__main__":
    main()