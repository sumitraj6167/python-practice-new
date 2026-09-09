#Sum of first N natural numbers.

n=int(input("Enter a number: "))
sum1 = 0
while(n > 0):
    sum1=sum1+n
    n=n-1
print("The sum of first n natural numbers is" ,sum1)

#This program determines the base's power given a base and a power.

def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:" ,power(base,exp))

