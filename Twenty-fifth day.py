#Python program to check if a given key exists in a directory or not.

d={'A':1, 'B':2, 'C':3}
key=input("Enter key to check:")
if key in d.keys():
    print("key is present and value of the key is:" ,d[key])
else:
    print("key isn't present:")

#Python program to find the sum all the items in a dictionary.

d={'A':100, 'B':540, 'C':239}
print("Total sum of values in the dictionary:",sum(d.values()))