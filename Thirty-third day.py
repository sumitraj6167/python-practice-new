#Python program to demonstrate class and object for book seller software.

class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quatity = quantity
        self.author = author
        self.price = price

    def __repr__(self):
        return f"Book:{self.title},quatity:{self.quatity},author:{self.author},price:{self.price}"


book1 = Book('Book 1', 12, 'author 1', 120)
book2 = Book('Book 2', 18, 'author 1', 220)
book3 = Book('Book 3', 18, 'author 1', 320)

print(book1)
print(book2)
print(book3)
