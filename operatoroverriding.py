class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __add__(self, other):
        if isinstance(other, Book):
            com_title = f'{self.title} & {other.title}'
            return Book(com_title, self.author)

    def __str__(self):
        return f'{self.title} by {self.author}'


b = Book("Wings of Fire", "Kalam")
b1 = Book("My Life Story", "Kalam")


b_s = b + b1


print(f'Book series: {b_s}')
