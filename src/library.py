from src.book import Book


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        if book in self.library.books:
            self.library.remove_book(self.book)
            return self.book

    def get_number_of_books(self):
        return len(self.books)
