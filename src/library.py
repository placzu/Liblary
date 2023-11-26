from src.book import Book


class Library:

    def __init__(self):
        self.books = []
        self.hired_books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)
            return self.books

    def get_number_of_books(self):
        return len(self.books)

    def add_book_to_hired_books(self, book: Book):
        self.hired_books.append(book)
        return self.hired_books

    def remove_hired_book_from_books(self, book: Book):
        self.books.remove(book)
        return self.books

    def get_hired_books_number(self):
        return len(self.hired_books)
