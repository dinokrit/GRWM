lass Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def summary(book):
        print(f'{book.title} by {book.author}, {book.pages} pages')

nameb1 = str(input("Enter your first book name: "))
nameb2 = str(input("Enter your second book name: "))
namea1 = str(input("Enter your first author name: "))
namea2 = str(input("Enter your second author name: "))
book1 = Book(nameb1,namea1,45)
book2 = Book(nameb2,namea2, 67)

book1.summary()
book2.summary()