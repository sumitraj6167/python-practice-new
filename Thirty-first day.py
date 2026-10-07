#Python program to create a class in which one method accepts a string form the user and another print it.

class printIO:
    def _init_(self):
        self.string = ""

    def get(self):
        self.string = input("Enter string: ")

    def put(self):
        print("String is:", self.string)

obj = printIO()
obj.get()
obj.put()

#Python program to Implement Linear Search.

def linear_search(alist, key):
    """Return index of key in alist. Return -1 if key not present."""
    for i in range(len(alist)):
        if alist[i] == key:
            return i
    return -1

alist = input('Enter the list of numbers: ')
alist = alist.split()
alist = [int(x) for x in alist]
key = int(input('The number to search for: '))

index = linear_search(alist, key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))
