#Python program to count the frequency of words appearing in a string using a dictionary.

test_string = input("Enter string: ")
words = test_string.split()
wordfreq = [words.count(p) for p in words]
print(dict(zip(words, wordfreq)))