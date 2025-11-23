"""
    CS110 Lab
    Dictionary Lab

    Updated By: Liam Cleckner

    CSCI 110
    Date: 11/22/2025

    Working with Python dictionary (dict) data structure.
"""
import os

# create a mapping of state names to their codes using a dictionary
states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
    # FIXME3 – add codes for the rest of the states
}

# create a mapping of states to their capital state using a dictionary
capitalCity = {
    'AL': 'Montgomery',
    'AK': 'Juneau',
    'AZ': 'Phoenix',
    'AR': 'Little Rock',
    'CA': 'Sacramento',
    'CO': 'Denver',
    'CT': 'Hartford',
    'DE': 'Dover',
    'FL': 'Tallahassee',
    'GA': 'Atlanta',
    'HI': 'Honolulu',
    'ID': 'Boise',
    'IL': 'Springfield',
    'IN': 'Indianapolis',
    'IA': 'Des Moines',
    'KS': 'Topeka',
    'KY': 'Frankfort',
    'LA': 'Baton Rouge',
    'ME': 'Augusta',
    'MD': 'Annapolis',
    'MA': 'Boston',
    'MI': 'Lansing',
    'MN': 'Saint Paul',
    'MS': 'Jackson',
    'MO': 'Jefferson City',
    'MT': 'Helena',
    'NE': 'Lincoln',
    'NV': 'Carson City',
    'NH': 'Concord',
    'NJ': 'Trenton',
    'NM': 'Santa Fe',
    'NY': 'Albany',
    'NC': 'Raleigh',
    'ND': 'Bismarck',
    'OH': 'Columbus',
    'OK': 'Oklahoma City',
    'OR': 'Salem',
    'PA': 'Harrisburg',
    'RI': 'Providence',
    'SC': 'Columbia',
    'SD': 'Pierre',
    'TN': 'Nashville',
    'TX': 'Austin',
    'UT': 'Salt Lake City',
    'VT': 'Montpelier',
    'VA': 'Richmond',
    'WA': 'Olympia',
    'WV': 'Charleston',
    'WI': 'Madison',
    'WY': 'Cheyenne'
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
            state = input('Enter a US state name: ').strip().capitalize()
            if state in states:  # check if state is in states dict
                print('Code for {} is {}.'.format(state, states[state]))
            else:
                print("Sorry! The US state name '{}' NOT found!".format(state))
        elif option == '2':
            # FIXME5 - complete menu option 2
            code = input('Enter a US state code: ').strip().upper()
            if code in capitalCity:
                print("Capital city for {} is {}".format(code, capitalCity[code]))
            else:
                print("Sorry! The US state code '{}' NOT found!".format[code])

        # FIXME6 - complete menu option 3
        elif option == '3':
            state = input('Enter a US state name:').strip().capitalize()
            if state in states:
                print("Capital city for {} is {}".format(state, states[state]))
            else:
                print("Sorry! The US state name {} NOT found!".format(state))
        # FIXME7 - handle the case where user enters invalid menu option
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")
        print('Press Enter to continue...')
        input()


if __name__ == "__main__":
    main()
