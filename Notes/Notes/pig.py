'''
Programmer: Liam Cleckner
Date 10/17/25
Program: Kattis Problem - Pig Latin - 
Algrotihm Steps:
    read lines while lines to read
        split line into words
        for each word:
            convert to pig latin:
                if word begins with consanent:
                    take the part before the firdst vowel, 
                    and add it to the end with an 'ay' attached
                if word begins with vowel:
                    add 'yay' to the end of the word
'''

def pig_translate(word: str) -> str:
    vowels = 'aeiouy'
    for vowel in vowels:
        if word[0] in vowels:
            

import sys

print("Enter a phrase to convert: ", file=sys.stderr)

line = input()

words = line.split()

for word in words:
    converted = pig_translate(word)
    ans = ans + converted + ""

print(words)