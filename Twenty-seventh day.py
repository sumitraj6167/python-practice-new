#Python program to count the frequency of words appearing in a string using a dictionary.

test_string = input("Enter string: ")
words = test_string.split()
wordfreq = [words.count(p) for p in words]
print(dict(zip(words, wordfreq)))

#Python program to create a list of tubles with the first element as the number and the second element as the square of the number.

l_range = int(input("Enter the lower range: "))
u_range = int(input("Enter the upper range: "))
a = [(x, x**2) for x in range(l_range, u_range + 1)]
print(a)