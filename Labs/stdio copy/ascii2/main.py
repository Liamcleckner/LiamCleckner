"""
    StdIO Lab 1B
    ASCII Art 2 - using literals and variables
    
    Updated By: Liam Cleckner
    Date: ... 9/4/2025
    
    This program produces an ASCII art on the console.
    It should look something like this.


         /\         ************************************************************      /~~   ~~\
        /##\                                                                       /~~         ~~\
       /#""#\                               Ascii Art 2                           {               }
      /#"##"#\                                 CS110                               \  _-     -_  /
     /#"#""#"#\                              Spring 25                              ~  \\   //  ~
    /#"#CMU!#"#\                            Corin Chepko                          _- -   | | _- _
         ||                                                                         _ -  | |   -_
         ||         ************************************************************        // \\

    Algorithm steps: 
    1. Use variables to store art and data
    2. Write a series of print statements to print the data/values to the console, using the .center() method
        to keep the strings centered.
    
    Note: You can add more lines or print differt ASCII arts of your choice if you'd like...
"""

print("Welcome to ASCII Art Program...\n")

# FIXED: prompt user to enter their name and store the value into name variable using input function
name = input("What is your name?")
# FIXED: greet the name using the variable as the following output
print("Hi "+ name + "!")
# must output: Nice meeting you, <name>!

# prompt user to enter the semester and store the value into semester variable using input function
semester: str = input("What semester is this [Fall/Spring]? ")
print("This is the " + semester + " semester")

# FIXED: prompt user to enter the course name and store the value into a variable using input function
course = input("What course is this?")
print("this is the " + course + " course")
# FIXED: prompt user to enter the lab title and store the value into a variable using input function
lab_title = input("What is the title of this lab?")
print("This is the " + lab_title + " lab")
print("Hope you like my ASCII art...\n\n")

# construct the art using set of three strings, one for art on the left, 
# one for the center text, and one for the art on the right
# We use 16 spaces for each art column and 30 spaces for the text in the center and border
left_width = 20
right_width = 20
center_width = 40  # Can change for smaller screens

# The extra spaces are not nessesary, but I used them to help line up the art
treeA_1: str = "      /\\     "
treeA_2: str = "     /##\\    "

treeB_1: str = "   /~~   ~~\\  "
treeB_2: str = "  /~~         ~~\\"

# FIXMEs7-8: use variables to add the rest of the art

asterics: str = "*"*center_width
spaces: str = " "*center_width

print(treeA_1.center(left_width) + asterics.center(center_width) + treeB_1.center(right_width))
print(treeA_2.center(left_width) + spaces.center(center_width) + treeB_2.center(right_width))


# FIXME9-10: print the rest of the art, including the collected name, lab title, course, and semester
# Note: You can add more lines or print differt ASCII arts of your choice if you'd like...

print("\nGoodbye...  \n")
