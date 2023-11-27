class Person:

    def __init__(self, first_name: str, last_name: str = None, email: str = None, phone_number: str = None,
                 borrowed_books: str = None):
        self.first_name = first_name
        self.last_name = last_name if last_name is not None else ""
        self.email = email if email is not None else ""
        self.phone_number = phone_number if phone_number is not None else ""
        self.borrowed_books = borrowed_books if borrowed_books is not None else ""

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
