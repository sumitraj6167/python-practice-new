#Numbers in a right-angled triangle pattern.

rows = int(input('Enter the number of rows'))
for i in range(1, rows):
    num =1
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print('')

#Another name for this pattern is a right andled triangle pyramid.

rows = int(input("Enter the number of rows"))
for i in range(0, rows):
    #nested loop for each column
    for j in range(0, i + 1):
        #print star
        print("*", end=' ')
    #new line after each row
    print("\r")

#Mirrored right triangle.

rows = int(input("Enter the number of rows "))
k = 2 * rows - 2
for i in range(0, rows):
    #process each column
    for j in range(0, k):
        #print space in pyramid
        print(end=" ")
    k = k -2
    for j in range(0, i + 1):
        #display star
        print("* ", end="")
    print("")

#Program to Multiplication table pattern.

rows = int(input("Enter the number of rows "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        #multiplication current column and row
        square = i * j
        print(i * j, end='  ')
    print()