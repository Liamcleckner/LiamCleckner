'''
programmer: Liam Cleckner
date: 10/13/25
Program: R2
Algorithm Steps:
    1. get user input for 2 numbers
    2. find the missing number considering that second number as the mean
    3. print r2

'''

r1, s = input().split()
r1 = int(r1)
s = int(s)

r2 = 2*s - r1
print(r2)

