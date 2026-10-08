#Celcius to Fahrenheit.

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is equal to {fahrenheit}°F")

#Pascal's triangle with n rows is printed by the program given a number n.

rows = int(input('Enter the number of rows'))
# outer Loop
for i in range(rows):
    #nested Loop
    for j in range(i):
        #display number
        print(i, end=' ')
    #new line after each row
    print('')

#pyramid pattern of numbers.

rows = int(input('Enter the number of rows'))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')
    