"""
    StdIO Lab
    ASCII Art - using literals and variables
    
    Updated By: Liam Cleckner
    Date: 8/26/2025
    
    This program produces an ASCII art on the console.

    Algorithm steps: 
    1. Use variables to store data/values
    2. Write a series of print statements to print the data/values to the console
"""

print("Welcome to ASCII Art Program...\n")

# FIXED: prompt user to enter their name and store the value into name variable using input function
name = input("What is your name?")
# FIXED: greet the name using the variable as the following output
# must output: Nice meeting you, <name>!
print("Nice meeting you, ", name, "!")
# prompt user to enter the semester and store the value into semester variable using input function
semester: str = input("What semester is this [Fall/Spring]? ")
print("This is " + semester + " semester.\n")

# FIXED: prompt user to enter the year and store the value into year variable using input function
year: str = input("What year is it?")
# FIXED: print the year using the variable as the following output
# must output: This is <year> year.
print("This is" + year + "year")

print("Hope you like my ASCII art...\n\n")

# FIXED: use variable to print the second line of the graphic
# FIXED: print the third line of the graphics
# FIXED: use variable to print the fourth line
# FIXED: use variable to print the fifth line
# Note: You can add more lines or print more ASCII arts of your choice if you'd like...

print("\nGood bye...  \n")

line1: str = "    |\\_/|    ***********************      (\\_/)"
print(line1)
line2: str = "   / @ @ \\   *      ASCII Lab      *     (='.'=)"
print(line2)
line3: str = '''  ( > 0 < )  *    ''' + name + '''  Liam Clec  *   ( " )_( " ) '''
print(line3)
line4: str = '''    >>x<<    *       ''' + semester + year + '''      * '''
print(line4)
line5: str = '''   /  O  \\   *       CSCI 111      * '''
print(line5)
line6: str = '''             ***********************   '''
print(line6)