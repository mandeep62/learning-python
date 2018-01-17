
from math import *
def circle(radius):
    area = pi*radius**2
    return area

print(circle(5))


from math import *
def square(side):
    area = side*side
    return area

print(square(4))

from math import *
def sphere(radius):
    area = 4*pi*radius*radius
    return area

print(sphere(10))



def numbers(a,b,c,d):
    if a > b and a > c and a > d:
        a = (input("Enter the number:"))
        print("This number is largest")
    elif b < a and b > c:
        b = input(("Enter the number"))
        print("This number is second largest")
    else:
        print("this number is third largest")

print(numbers(a,b,c,d))
