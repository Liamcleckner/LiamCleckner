'''
programmer: Liam Cleckner
date: 10/1/25
Program: Functions
Algorithm Steps:
    Define all functions with 2 numbers
    Prompt the user to enter 2 numbers
    
'''

import math

def add_two(a,b):
    return a+b
def mult_two(a,b):
    return a*b
def dev_two(a,b):
    return a/b
def rem_two(a,b):
    return a%b
def sub_two(a,b):
    return a-b


def sqrt_n1(a,b):
    if a>0:
        return math.sqrt(a)
    else:
        print()
def sqrt_n2(a,b):
    if a>0:
        return math.sqrt(b)
    else:
        print()

n1, n2 = input("Enter two numbers separated by a space: ").split()
n1 = float(n1)
n2 = float(n2)

#Functions

sum = add_two(n1, n2)
product = mult_two(n1, n2)
quotient = dev_two(n1, n2)
difference = sub_two(n1, n2)
remainder = rem_two(n1,n2)
sqrt1 = sqrt_n1(n1,n2)
sqrt2 = sqrt_n2(n1,n2)

#Test Functions

tsum_1 = add_two(.6, .7)
tproduct_1 = mult_two(.6, .7)
tquotient_1 = dev_two(.6, .7)
tdifference_1 = sub_two(.6, .7)
tremainder_1 = rem_two(.6,.7)
tsqrt1_1 = sqrt_n1(.6,.7)
tsqrt2_1 = sqrt_n2(.6,.7)

tsum_2 = add_two(-6, -7)
tproduct_2 = mult_two(-6, -7)
tquotient_2 = dev_two(-6, -7)
tdifference_2 = sub_two(-6, -7)
tremainder_2 = rem_two(-6,-7)
tsqrt1_2 = sqrt_n1(-6,-7)
tsqrt2_2 = sqrt_n2(-6,-7)

print(f"Test functions #1 for a = .6 and b = .7: sum = {tsum_1} product = {tproduct_1} quotient = {tquotient_1} difference = {tdifference_1} remainder = {tremainder_1} square root = {tsqrt1_1} square root = {tsqrt2_1}")
print(f"Test functions #2 for a = -6 and b = -7: sum = {tsum_2} product = {tproduct_2} quotient = {tquotient_2} difference = {tdifference_2} remainder = {tremainder_2} square root = {tsqrt1_2} square root = {tsqrt2_2}")
#Answer Print Statements

print(f"Sum of {n1} and {n2} = {sum}")
print(f"Product of {n1} and {n2} = {product}")
print(f"Quotient of {n1} and {n2} = {quotient}")
print(f"Difference of {n1} and {n2} = {difference}")
print(f"Remainder of {n1} and {n2} = {remainder}")
print(f"Square root of {n1} = {sqrt1}")
print(f"Square root of {n2} = {sqrt2}")