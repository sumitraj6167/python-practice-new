#Inverted pyramid pattern of numbers.

rows = int(input('Enter number of rows'))
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')

#Inverted pyramid pattern with the same digit.

rows = int(input('Enter the number of rows'))
num = rows
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num,end=' ')
    print("\r")

#Alternate numbers pattern.

rows = int(input('Enter the number of rows'))
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 -1), end=" ")
        j = j + 1
    i = i + 1
    print('')