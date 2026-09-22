#python program to remove the characters of odd index values in a string.

def modify(string):
    final = ""
    for i in range (len(string)):
        if i % 2 == 0:
            final = final + string[i]
    return final
string=input("ENter string:")
print("Modified string is:" ,modify(string))

#python program to remove the nth index character from a non-empty string.

def remove(string, n):
    first = string[:n]
    last = string[n+1:]
    return first + last
string=input("ENter the sring:")
n=int(input("Enter the index of the character to remove:"))
print("Modifed string:", remove(string,n))

#python program to take a string and replace every blank space with a hypen.

string=input("Enter string:")
string=string.replace(' ' , '_')
print("Modified string:" ,string)
