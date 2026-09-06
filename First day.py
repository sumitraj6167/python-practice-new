#To determine given number is odd or even.

n = int(input("Enter a positive number: "))
if n % 2 == 0:
    print(n, "This is an even number.")
else:
    print(n, "This is an odd number.")

#To determine given integer is positive or negative.

num=int(input("Enter the number:" ))
if(num>0):
    print("The number is positive")
else:
    print("The number is negative")


#To determine the given number is palindrome.

n=int(input("Enter number: "))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
        print("The number is a palindrome!")
else:
    print("The number is not a palindrome!")
    