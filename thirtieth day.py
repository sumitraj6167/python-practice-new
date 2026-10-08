#Python program to find the area of a rectangle using classes.

class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length

a=int(input("Enter length of a rectangle: "))
b=int(input("Enter breadth of a rectangle: "))
obj=rectangle(a,b)
print("Area of rectangle:",obj.area())
