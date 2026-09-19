 #python program to read a number and print an identity matrix of the desired size.

n=int(input("Enter a number: "))
for i in range(0,n):
    for j in range (0,n):
        if(i==j):
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()

    #python program to find ssun of series: 1 +1/2 +1/3.......+ 1/N.

n=int(input("Enter the number of terms: "))
sum1=0
for i in range(1,n+1):
    sum1=sum1+(1/i)
print("The sum of series is",round(sum1,2))

     
