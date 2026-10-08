#Python program to implement object oriented programming and instantiate some objects with different properties, and call the method on them.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")


obj1 = Dog("Object-1", 2)
obj2 = Dog("Object-2", 12)
obj3 = Dog("Object-3", 8)

obj1.doginfo()
obj2.doginfo()
obj3.doginfo()