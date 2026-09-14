#Program to find the roots of an equation.

print("Equation: ax^2 + bx + c ")
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
d=b**2-4*a*c
d1=d**0.5
if(d<0):
    print("The roots are imaginary. ")
else:
    r1=(-b+d1)/2*a
    r2=(-b-d1)/2*a
    print("The first root: ",round(r1,2))
    print("The second root: ",round(r2,2))

#Program to find area of a triangle given all threee sides.

import math
a=int(input("Enter first side: "))
b=int(input("Enter second side: "))
c=int(input("Enter third side: "))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle is: ",round(area,2))
