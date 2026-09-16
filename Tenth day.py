#program that cxchanges two numbers'values without the need of a temporary variable.

a=int(input("Enter value of first variable: "))
b=int(input("Enter value of second variable: "))
a=a+b
b=a-b
a=a-b
print("a is:",a,"b is:",b)

#Addition of two Matrices using Numpy.

import numpy as np

A= np.array([[2, 4], [5, -6]])
B= np.array([[9, -3], [3, 6]])
print('Matrix A:\n' ,A)
print('Matrix B:\n' ,B)
C = A + B
print('Sum of A and B Matrix is:\n' ,C)
