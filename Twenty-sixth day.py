#Python program to create a dictionary with key as first character and valur as words starting with that character.

test_string = input("Enter string:")
l = test_string.split()
d = {}
for word in l:
    if word[0] not in d.keys():
        d[word[0]] = []
        d[word[0]].append(word)
    else:
        if word not in d[word[0]]:
            d[word[0]].append(word)
for k, v in d.items():
    print(k, ":", v)

#Python program to genertate a dictionary that contains number (between 1 and n) in the form (x,x*x).

n=int(input("Enter a number:"))
d={x:x*x for x in range(1,n+1)}
print(d)
