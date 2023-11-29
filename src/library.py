from src.book import Book
from src.user import User


class Library:

    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)
            return self.books

    def get_number_of_books(self):
        return len(self.books)

    def find_current_rented_books(self):
        return [book for book in self.books if book.is_rented()]

    def get_rented_books_number(self):
        return len(self.current_rented_books)

    def add_user(self, user: User):
        if user.email:
            email_validation = user.validate_email(user.email)
            if email_validation != user.email:
                return email_validation

        if user.phone_number:
            phone_validation = user.validate_phone_number(user.phone_number)
            if phone_validation != user.phone_number:
                return phone_validation

        self.users.append(user)

    def book_rent(self, user: User, book: Book):
        if book in self.books:
            book.get_date()
            book.get_deadline()
            user.borrowed_books[book.id] = book.name
            return (f"{user.first_name} rent a {book.name}")
        else:
            return (f"don't have {book.name}")
