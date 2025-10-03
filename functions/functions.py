'''
programmer: Liam Cleckner
date: 10/1/25
Program: Functions
Algorithm Steps:
    Define all functions with 2 numbers
    Prompt the user to enter 2 numbers
    
'''

import math

def add_two(n1,n2):
    return ysum
def mult_two(n1, n2):
    return yproduct
def dev_two(n1,n2):
    return yquotient
def rem_two(n1, n2):
    return yremainder
def sub_two(n1,n2):
    return ydifference
def sqrt_n1(n1):
    return math.sqrt(n1)
def sqrt_n2(n2):
    return math.sqrt(n2)

n1, n2 = input("Enter two numbers separated by a space: ").split()
n1 = float(n1)
n2 = float(n2)

ysum = n1+n2
yproduct = n1*n2
yquotient = n1/n2 
ydifference = n1-n2
yremainder = n1%n2
ysqrt1 = math.sqrt(n1)
ysqrt2 = math.sqrt(n2)

#Functions

sum = add_two(n1, n2)
product = mult_two(n1, n2)
quotient = dev_two(n1, n2)
difference = sub_two(n1, n2)
remainder = rem_two(n1,n2)
sqrt1 = sqrt_n1(n1)
sqrt2 = sqrt_n2(n2)

#Test Functions



#Answer Print Statements

print(f"Sum of {n1} and {n2} = {sum}")
print(f"Product of {n1} and {n2} = {product}")
print(f"Quotient of {n1} and {n2} = {quotient}")
print(f"Difference of {n1} and {n2} = {difference}")
print(f"Remainder of {n1} and {n2} = {remainder}")
print(f"Square root of {n1} = {sqrt1}")
print(f"Square root of {n2} = {sqrt2}")