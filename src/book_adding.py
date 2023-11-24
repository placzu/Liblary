from src.book import Book
from src.library import Library


class Adding_Book:

    def add_book(self, library, book):
        library.books.append(book)


book1 = Book("lord of the rings", "J.R.R", 987, "story about some rings")
my_library = Library()
adding_book = Adding_Book()
adding_book.add_book(my_library, book1)
for book in my_library.books:
    (f"- {book.name}, {book.author}, {book.pages}, {book.short_description}")
