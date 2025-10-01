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
    return n1+n2
def mult_two(n1, n2):
    return n1*n2
def dev_two(n1,n2):
    return n1/n2
def rem_two(n1, n2):
    return n1%n2
def sub_two(n1,n2):
    return n1-n2
def sqrt_n1(n1):
    return math.sqrt(n1)
def sqrt_n2(n2):
    return math.sqrt(n2)

n1, n2 = input("Enter two numbers separated by a space: ").split()
n1 = float(n1)
n2 = float(n2)



sum = add_two(n1, n2)
product = mult_two(n1, n2)
quotient = dev_two(n1, n2)
difference = sub_two(n1, n2)
remainder = rem_two(n1,n2)
sqrt1 = sqrt_n1(n1)
sqrt2 = sqrt_n2(n2)

def test_functions():
    test = [(.4, .6), (-5,-4)]
        sum = add_two(a, b)
        product = mult_two(a, b)
        quotient = dev_two(a, b)
        difference = sub_two(a, b)
        remainder = rem_two(a,b)
        sqrt1 = sqrt_n1(a)
        sqrt2 = sqrt_n2(b)

print(f"Sum of {n1} and {n2} = {sum}")
print(f"Product of {n1} and {n2} = {product}")
print(f"Quotient of {n1} and {n2} = {quotient}")
print(f"Difference of {n1} and {n2} = {difference}")
print(f"Remainder of {n1} and {n2} = {remainder}")
print(f"Square root of {n1} = {sqrt1}")
print(f"Square root of {n1} = {sqrt2}")

