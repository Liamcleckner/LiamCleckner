'''
Circle - Basic Math - Homework
Updated By: Liam Cleckner
Date: 
CSCI 110

This program prompts user to enter radius of a circle and calculates and displays area
and circumference of the circle.

Algorithm steps:
	1. Prompt user to enter radius
	2. Store radius into a variable
	2. Calculate area using the formula: pi * radius * radius
	3. Calculate circumference using the formula: 2 * pi * radius
	4. Display the calculated values of area and circumference with proper description
'''

import math


radius = input("Please enter the radius for a circle:")
radius = float(radius)
area = math.pi*(radius**2)
circumference = 2*(math.pi)*radius
print(area)
print(circumference)