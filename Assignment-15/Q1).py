#Create a class Book with members as bid,bname,price and author.Add following methods:
#a. Constructor (Support both parameterized and parameterless)
#b. Destructor
#c. ShowBook
class Book:
    def __init__(self, bid=None, bname=None, price=None, author=None):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        print("Book object Created.")
        print("----------------------------------------")

    def __del__(self):
        print(f"Book object with ID {self.bid} is destroyed. ")

    def showBook(self):
        print("BOOK_ID:", {self.bid})
        print("BOOK_NAME:", {self.bname})
        print("PRICE:", {self.price})
        print("AUTHOR:", {self.author})
        print("----------------------------------------")

book1 = Book()
book1.bid = 101
book1.bname = "Python Programming"
book1.price = 400
book1.author = "Guido van Rossum" 
book1.showBook()
print("----------------------------------------")

book2 = Book(102, "C++ Basics", 550, "Bjarne Stroustrup")
book2.showBook()
print("----------------------------------------")