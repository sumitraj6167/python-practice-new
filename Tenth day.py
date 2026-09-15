#program that cxchanges two numbers'values without the need of a temporary variable.

a=int(input("Enter value of first variable: "))
b=int(input("Enter value of second variable: "))
a=a+b
b=a-b
a=a-b
print("a is:",a,"b is:",b)

