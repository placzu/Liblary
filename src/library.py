from src.book import Book


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
