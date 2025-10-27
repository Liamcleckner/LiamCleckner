'''
programmer: Liam Cleckner
Date: 10/20/25
Program: Loop
Algorithm Steps:

'''

import random

name = input("What is your name?")
print(f"Hi {name}!")

def main():

    total_games = 0
    wins = 0
    losses = 0
    

    while(True):
        
        rand_num = random.randint(1,20)
        print("You get 6 tries to guess the number.")
        tries = 0
        correct = False
        
        while tries < 6 and correct == False:
            guess = int(input("Take a guess:"))

            tries += 1

            if guess > rand_num:
                print("Your guess is too high")
            elif guess < rand_num:
                print("Your guess is too low")
            else:
                print(f"Congratulations, {name}! You WIN!!")
                print(f"You guessed right in {tries} tries.")
                wins += 1
                correct = True
            
            if not correct and tries >= 6:
                print("You lost.")
                print(f"The number was {rand_num}")
                losses += 1
            
        total_games += 1
        again = input("Play again? [y/n]")
        if again != 'y':
            break

    print("Game over.")
    print(f"Total games = {total_games}")
    print(f"Total losses = {losses}")
    print(f"Total wins = {wins}")

main()