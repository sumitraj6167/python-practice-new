#Reverse of number

n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:" ,rev)

#Number's Table

n=int(input("Enter the number to print the tables for: "))
for i in range(1,11):
    print(n,"x",i,"=",n*i)