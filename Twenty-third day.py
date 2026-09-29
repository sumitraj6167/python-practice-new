#Python program to remove the duplicate items from a list.

a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("ENter element" + str(x+1) + ":"))
    a.append(element)
b = set()
unique = []
for x in a:
    if x not in b:
        unique.append(x)
        b.add(x)
print("Non-duplicate items:")
print(unique)

#Python program to read a list of words and return the length of the longest one.

a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=input("Enter element" + str(x+1) + ":") 
    a.append(element)
max1=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>max1):
        max1=len(i)
        temp=i
print("The word with the longest length is:" ,temp)
