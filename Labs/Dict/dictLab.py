"""
    CS110 Lab
    Dictionary Lab

    Updated By: FIXME1

    CSCI 110
    Date: FIXME2

    Working with Python dictionary (dict) data structure.
"""
import os

# create a mapping of state names to their codes using a dictionary
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
    # FIXME3 – add codes for the rest of the states
}

# create a mapping of states to their capital state using a dictionary
capitalCity = {
    'CA': 'Sacramento',
    'MI': 'Lansing',
    'FL': 'Tallahassee'
}

# add some more entires to capitalCity dictionary
capitalCity['NY'] = 'Albany'
capitalCity['OR'] = 'Salem'
# FIXME4: Add rest of the states’ capital cities to capitalCity dictionary


def menu():
    print("""
            Enter one of the menu options:
            [1] Find US state's code given its name
            [2] Find US state's capital given its code
            [3] Find US state's capital given its name
            [4] Exit the program
        """)


def main():
    while True:
        # clear screen
        os.system('clear')
        # print menu
        menu()
        # get menu option
        option = input()
        if option == '4':
            print('SEE YOU AGAIN... GOOD BYE!')
            break

        if option == '1':
            state = input('Enter a US state name: ')
            if state in states:  # check if state is in states dict
                print('Code for {} is {}.'.format(state, states[state]))
            else:
                print("Sorry! The US state name '{}' NOT found!".format(state))
        elif option == '2':
            # FIXME5 - complete menu option 2
            print('FIXME')

        # FIXME6 - complete menu option 3

        # FIXME7 - handle the case where user enters invalid menu option
        print('Enter to continue...')
        input()


if __name__ == "__main__":
    main()
