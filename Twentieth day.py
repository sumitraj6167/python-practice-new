#Python program to print the largest even and largest odd number in a list.

n = int(input("Enter the number of elements: "))

numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

largest_even = None
largest_odd = None

for num in numbers:
    if num % 2 == 0:
        if largest_even is None or num > largest_even:
            largest_even = num
    else:
        if largest_odd is None or num > largest_odd:
            largest_odd = num

print("Largest Even Number =", largest_even)
print("Largest Odd Number =", largest_odd)