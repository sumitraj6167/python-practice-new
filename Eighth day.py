#program to Equilateral triangle pattern of star.

print("print equilateral triangle pyramid using asterisk symbol ")
size = int(input("Enter the number of rows "))
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")

#program to Alphabet pattern.

ascii_number = 65
rows = int(input("Enter the number of rows "))
for i in range(0, rows):
    for j in range(0, i + 1):
        character = chr(ascii_number)
        print(character, end=' ')
        ascii_number += 1
    print(" ")

#pattern to display latters of the words.

word = input("Enter the word ")
x = ""
for i in word:
    x += i
    print(x)
    