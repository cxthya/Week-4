'''
Cinthya Calderon-Hernandez
CMSC 111
Spring 2026
Calculate Area of a Rectangle
'''

def area(length, width):
    return length * width

length = float(input("enter length: "))
width = float(input("enter width: "))

print ("Area=", area(length, width))