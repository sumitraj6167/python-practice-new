#Python program to generate random numbers from 1 to 20 and append them to the list.

import random 
a=[]
n=int(input("Enter number of elements:"))
for j in range(n):
    a.append(random.randint(1,20))
print('Randomised list is: ' ,a)