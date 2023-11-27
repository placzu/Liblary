class Person:

    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str, borrowed_books: str)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.borrowed_books = borrowed_books

    def borrow_book(self, person, book_name):
        person.borrowed_books.append(book_name)



