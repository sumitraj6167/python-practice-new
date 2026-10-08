#Multiplication of two Matrices using numpy.

import numpy as np
A = np.array([[5, 4], [5, 4]])
B = np.array([[2, 3], [3, 4]])
print('Matrix A:\n' ,A)
print('Matrix B:\n' ,B)
C = A.dot(B)
print('Sum of A and B Matrix is:\n' ,C)