"""
File I/O Lab
By: Liam Cleckner

CSCI 110
Date: 11/22/2025

Program prompts user to enter name of the file that contains 10 integers.
It opens, reads and stores the numbers into a list.
Program will then sort the numbers in the list in ascending and descending orders
Program will then print the sorted lists to an output file along with the 
largest and smallest values in the list.

NOTE: All fixme's are each worth 10 points except for the FIXME1 which is worth 20 points
"""

totalInts = 10


def readData():
    intList = []
    # FIXME1 (20 points):
    # Prompt user to input file name
    # open the file; read each number one line at a time;
    # and store it into intList list
    # close the file
    # return the intList
    fileName = input("Enter the name of the input file: ")
    with open(fileName, "r") as infile:
        for line in infile:
            intList.append(int(line.strip()))
    return intList


def sortListInAscendingOrder(lstInts):
    # FIXME2
    # sort lstInts list in ascending order
    lstInts.sort()


def sortListInDescendingOrder(lstInts):
    # FIXME3
    # sort lstInts in descending order
    lstInts.sort(reverse = True)


def printList(printFile, lstInts):
    for i in lstInts:
        # FIXME4
        # write each value one line at a time to file
        # handled by printFile object.
        
        printFile.write(str(i) + "\n")

    printFile.write('\n')


def main():
    integers = []  # list to store integers
    integers = readData()
    outputFileName = input('Enter a file to write output to: ')
    printFile = open(outputFileName, 'w')
    printFile.write("Numbers entered:\n")
    printList(printFile, integers)
    # sort numbers
    sortListInAscendingOrder(integers)
    printFile.write("Numbers sorted in ascending order:\n")
    printList(printFile, integers)

    # FIXME5
    # Call sortListInDescendingOrder function
    sortListInDescendingOrder(integers)

    # FIXME6
    # Write the sorted list in descending order to the output file
    printFile.write("Numbers sorted in descending order:\n")
    printList(printFile, integers)

    # FIXME7
    # Print the largest number to the output file
    printFile.write("Largest number: " + str(max(integers)) + "\n")

    # FIXME8
    # Print the smallest number to the output file
    printFile.write("Smallest number: " + str(min(integers)) + "\n")

    printFile.close()
    print('Done executing the program! Check the output file for results.')


# FIXME9
# Call main function if this module is run as the main module
if __name__ == "__main__":
    main()