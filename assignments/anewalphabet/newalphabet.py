'''
programmer: Liam Cleckner
Date: 11/22/2025
Program: Kattis problem - New Alphabet - https://open.kattis.com/problems/anewalphabet 
Algorithm Steps:


'''

letters = {
    'a': '@',
    'b': '8',
    'c': '(',
    'd': '|)',
    'e': '3',
    'f': '#',
    'g': '6',
    'h': '[-]',
    'i': '|',
    'j': '_|',
    'k': '|<',
    'l': '1',
    'm': '[]\\/[]',
    'n': '[]\\[]',
    'o': '0',
    'p': '|D',
    'q': '(,)',
    'r': '|Z',
    's': '$',
    't': '\'][\'',
    'u': '|_|',
    'v': '\\/',
    'w': '\\/\\/',
    'x': '}{',
    'y': '`/',
    'z': '2'
}

def translate(text):
    result = []
    for character in text:
        lower = character.lower()
        if lower in letters:
            result.append(letters[lower])
        else:
            result.append(character)
    return ''.join(result)

def test():
    assert translate("cat") == "(@']['"
    assert translate("Hello world!") == "[-]3110 \\/\\/0|Z1|)!"
    assert translate("abc 123") == "@8( 123"


def main():
    text = input().strip()
    print(translate(text))

if __name__ == '__main__':
    test()
    main()