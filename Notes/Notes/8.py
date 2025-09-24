'''
A program that is an extension of the Kattis problem - "The Last Problem"

ALgorithm Steps:
    1. Input a name
    2. print "Hello and goodbye {nam}"

    repeat 1 and 2, 3 times
'''
'''
name = input()
print(f"Hello and goodbye {name}")

name = input()
print(f"Hello and goodbye {name}")

name = input()
print(f"Hello and goodbye {name}")
'''
'''
#Using a function
def hello_and_goodbye(): #This function does not need any data,
                        #and is not returning any data to the rest of the program
                        #ie: a fruitless function
    name = input("Whatnam?")
    print(f"Hello and goodbye {name}")

hello_and_goodbye()
hello_and_goodbye()
hello_and_goodbye()
'''

#last problem evolution\/

import sys

def main():
    name_main = input()
    answer = solution(name_main)
    print(answer)

def solution(name : str) -> str:
    '''
    inputs a string, returns a string in a phrase
    '''
    ans = "Thank you, {name}, and farewell!"
    return ans # passes the answer back onto the calling function, in this case
                # our global main program
'''
print("Enter a name: ", file=sys.stderr) #ingored by kattis, for user use
name = input()
print(f"Thank you, {name}, and farewell")
'''

'''
name_main = input()
answer = solution(name_main)
print(answer)
'''
if __name__ == "__main__": # if i am the main file being run, run my main function
                            # otherwise my functions are open for import
    main()