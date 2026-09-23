#python program to reverse a given string using Slicing.

a=str(input("Enter a string: "))
print("Reverse of the string is:" ,end=' ')
print(a[::-1])

#ython program to reverse a given string using Recursion.

def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a= str(input("Enter the string to be reversed:"))
print('reversed string is ',reverse(a))
