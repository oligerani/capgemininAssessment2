class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def display(self):
        print(f'book title:{self.title} \n author:{self.author} \n isbn:{self.isbn}') 
book=Book("wings of fire","apj abdhul kalam",123456789)
book.display()           