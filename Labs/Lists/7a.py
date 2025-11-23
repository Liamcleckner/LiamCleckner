"""
CSCI 110
List Lab

By: Liam Cleckner
Date: 11/19/2025

Program prompts user to enter 10 integers and stores the entered numbers into a list.
Program will then sort the numbers in the list in ascending and descending orders
and print the largest and smallest values in the list.
Program will also print the indices of the largest and smallest numbers in the list.
"""

totalInts = 10


def getIntegers():
    intList = []
    i = 0
    while i < totalInts:
        num = int(input("Enter an integer: "))
        # FIXME add num into integers list
        intList.append(num)
        i += 1
    return intList


def sortListInAscendingOrder(intList):
    intList.sort()


def sortListInDescendingOrder(intList):
    # FIXED3 (20 points)
    intList.sort(reverse=True)


def printList(intList):
    for val in intList:
        print(val, end=' ')
    print()


def main():
    integers = []  # empty list to store integers
    integers = getIntegers()
    print("Numbers entered are: ")
    printList(integers)
    print()
    # sort numbers
    sortListInAscendingOrder(integers)
    print("Numbers in ascending order: ")
    printList(integers)

    # FIXED4 (10 points)
    # Call sortListInDescendingOrder function


    sortListInDescendingOrder(integers)
    
    # FIXED5 (10 points)
    # Print the sorted list in descending order

    print("Numbers in descending order:")
    print(integers)

    # FIXED6 (10 points)
    # Print the largest number

    large = max(integers)
    print("Largest number:")
    print(large)

    # FIXED7 (10 points)
    # Print the smallest number

    small = min(integers)
    print("Smallest number:")
    print(small)

    # FIXED8 (10 points)
    # Find and print the index of the smallest number

    print("Index of the smallest number:")
    print(integers.index(small))

    # FIXED9 (10 points)
    # Print the index of the largest number

    print("index of largest number:")
    print(integers.index(large))


# FIXED10 (20 points)
# Call main function if this file is run as the main module

if __name__ == "__main__":
    main()

#print('call main() function to see partial outputs of the program...')