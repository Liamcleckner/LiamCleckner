'''
def greet():
    print("Hello")
    print("World!")

def greet_name(name):
    print("Hello {name}")

greet() # This is a call to the "greet()" function

main_name = "Xander"
greet_name(main_name)
'''
def rectangle_calc(length, width):
    perimeter = 2*length + 2*width
    area = length*width
    return area, perimeter

length, width = input("Enter the length and widhth separated by a spave: ").split()
