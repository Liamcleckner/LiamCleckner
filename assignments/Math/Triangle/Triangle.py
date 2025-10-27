'''
Programmer: Liam Cleckner
Date: 9/19/2025
Assignment: Triangle
ASCII art from: https://www.asciiarthub.com/animals.html

Triangle perimeter and area assignment for CSCII110

1. Prompt the user to enter 3 side lengths
2. Test whether these side lengths can make a real triangle
3. If the triangle is possible, calculate and display the perimeter and area values1
'''
import math


side1, side2, side3 = input("Enter 3 side lengths for your triangle separated by spaces.").split()
side1_num = float(side1)
side2_num = float(side2)
side3_num = float(side3)

perimeter = side1_num + side2_num + side3_num

s = (perimeter/2)

area_func = s*(s-side1_num)*(s-side2_num)*(s-side3_num)

if area_func <= 0 or side1_num <= 0 or side2_num <= 0 or side3_num <= 0:
    print("Triangle is not possible")
else:
    area = math.sqrt(area_func)

if area_func > 0 and side1_num > 0 and side2_num > 0 and side3_num > 0:
    print("perimeter = " + str(perimeter))
    print("area = " + str(area))