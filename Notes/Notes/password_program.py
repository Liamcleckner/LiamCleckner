'''
Programmer: Liam Cleckner
Date: 10/20/25
Program: Create amd validate a password
Password requirements:
    At least 1 digit
    At least 1 uppercase letter
    At least 1 lowercase letter
    At least 1 special character
'''

import random
import string

MAX_SIZE = 12

symbols = "!@#$%^&*()"
all_characters = symbols + string.ascii_letters + string.digits

print(all_characters)




password = ""
for i in range(MAX_SIZE):
    new_char = random.choice(all_characters)
    password = password + new_char

print(password)