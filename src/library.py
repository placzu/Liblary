from src.book import Book
from src.person import Person


class Library:

    def __init__(self):
        self.books = []
        self.current_rented_books = []
        self.person = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)
            return self.books

    def get_number_of_books(self):
        return len(self.books)

    def add_book_to_hired_books(self, book: Book):
        self.current_rented_books.append(book)
        return self.current_rented_books

    def remove_hired_book_from_books(self, book: Book):
        self.books.remove(book)
        return self.books

    def get_hired_books_number(self):
        return len(self.current_rented_books)

    def add_person(self, person: Person):
        self.person.append(person)

    def book_rent(self, person: Person, book: Book):
        if book in self.books:
            self.books.remove(book)
            self.current_rented_books.append(book)
            return (f"{person.first_name} rent a {book.name}")
        else:
            return (f"don't have {book.name}")









#    def current_renter(self):
#        #kurwa ludzie ktorzy wynajmuja maja sie tutaj pojawiac pierdolona pamiec krotka!!!
#        book.current_renter



