#python program to remove the characters of add index values in a string.

def modify(string):
    final = ""
    for i in range (len(string)):
        if i % 2 == 0:
            final = final + string[i]
    return final
string=input("ENter string:")
print("Modified string is:" ,modify(string))
