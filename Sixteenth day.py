#python program to find the GCD of two numbers.

import math
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("The GCD of the two number is", math.gcd(a,b))

#GCD program in python using Recusion.

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
GCD=gcd(a,b)
print("GCD is: " ,GCD)
