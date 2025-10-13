'''
programmer: Liam Cleckner
date: 10/13/25
Program: Conditionals
Algorithm Steps:

'''

import math

def add_five(a,b,c,d,e):
    return a+b+c+d+e
def mult_five(a,b,c,d,e):
    return a*b*c*d*e
def avg_five(a,b,c,d,e):
    return sum/5
def max_five(a,b,c,d,e):
    big = a
    if b > big:
        big = b
    if c > big:
        big = c
    if d > big:
        big = d
    if e > big:
        big = e
    return big
def min_five(a,b,c,d,e):
    small = a
    if b < small:
        small = b
    if c < small:
        small = c
    if d < small:
        small = d
    if e < small:
        small = e
    return small

def main():
    n1, n2, n3, n4, n5 = input("Enter five numbers separated by spaces: ").split()
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    n4 = float(n4)
    n5 = float(n5)

    sum = add_five(n1,n2,n3,n4,n5)
    product =  mult_five(n1,n2,n3,n4,n5)
    average = avg_five(n1,n2,n3,n4,n5)
    largest = max_five(n1,n2,n3,n4,n5)
    smallest = min_five(n1,n2,n3,n4,n5)

    print(sum)
    print(product)
    print(average)
    print(largest)
    print(smallest)

main()