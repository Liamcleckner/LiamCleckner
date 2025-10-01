'''
while(True):
    print("An infinite loop!")

    #Ask the user to play again, break if not
    again = input("Play again?")
    if(again[0].lower() == 'y'): # take the first character, make it lower case, and compare to 'y' for yes
        continue # go bacl tp the beginning of the loop
    else:
        print("Thanks for playing!")
        break # I'm done, exit the loop
'''

def input_digit():

    while(True):
        number = input("Enter a number: ")
        if(number.isdigit() == True):
            number = int(number)
        else:
            print("Frack...")
            print("This aint wokr")
            print("Exiting")
            return "Error"
    #loop is done, got input
    return number