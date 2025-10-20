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
    ans = ''
    
    for vowel in vowels:
        if word[0] in vowels:
            ans = word + 'yay '
            return ans
    
    index = 0
    
    while(word[index] not in vowels):
        index += 1
    ans = word[index::] + word[0:index-1] + 'ay '
    return ans


import sys

print("Enter a phrase to convert: ", file=sys.stderr)


while(True):
    line = input()

    words = line.split()
    ans = ''
    for word in words:
        converted = pig_translate(word)
        ans = ans + converted + ''

    print(words)
    print(ans)