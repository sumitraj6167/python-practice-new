#python program to find the sun of series: 1 + x^2/2 + x^3/3 + ....... + x^n/n.

n=int(input("Enter the number of terms:"))
x=int(input("Enter the value of x:"))
sum1=1
for i in range(2,n+1):
    sum1=sum1+((x**i)/i)
print("The sum of series is",round(sum1,2))

#python program to read a number n and print and compute the series: 1+2+3+4+5+......+n

n=int(input("ENter a number: "))
a=[]
for i in range(1,n+1):
    print(i,sep=" ",end=" ")
    if(i<n):
        print("+",sep=" ",end=" ")
    a.append(i)
print("=",sum(a))

print()

#python program to ind the LCM of two numbers.

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if(a>b):
    min1=a
else:
    min1=b
while(1):
    if(min1%a==0 and min1%b==0):
        print("LCM is:",min1)
        break
    min1=min1+1