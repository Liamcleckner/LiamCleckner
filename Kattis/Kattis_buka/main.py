'''
programmer: Liam Cleckner
date: 9/5/25
Program: Kattis Problem - 
Algorithm Steos:
    input line1
    input line2
'''
'''
print("Enter three sides separated by a space"
a,b,c = input().split()
print(a,b,c)
'''
import sys

print("Enter first line: ", file=sys.stderr)

line1 = input()
line2 = input()

line1a, line1b = line1.split('|')
line2a, line2b = line2.split('|')

print(line1a+line2a, line1b+line2b)
