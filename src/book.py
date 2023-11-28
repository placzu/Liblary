from datetime import datetime, timedelta
from src.user import User
import uuid


class Book:

    def __init__(self, name: str, author: str, pages: int, short_description: str = None, rent_date: str = None,
                 rent_deadline: str = None, current_renter: User = None):
        self.name = name
        self.author = author
        self.short_description = short_description if short_description is not None else ""
        self.pages = pages
        self.rent_date = rent_date if rent_date is not None else ""
        self.rent_deadline = rent_deadline if rent_deadline is not None else ""
        self.current_renter = current_renter if current_renter is not None else ""
        self.id = uuid.uuid4()

    def present(self):
        return (
            f"Book entitled {self.name} written by: {self.author}, with a short review {self.short_description} and {self.pages} pages.")

    def __str__(self):
        return f'{self.name} {self.author} {self.short_description} {self.pages}'

    def get_date(self):
        today = datetime.now()
        self.rent_date = today.strftime("%d/%m/%Y/%H:%M")
        return self.rent_date

    def get_deadline(self):
        today = datetime.now()
        self.rent_deadline = (today + timedelta(days=14)).strftime("%d/%m/%Y/%H:%M")
        return self.rent_deadline

    def add_renter_to_book(self, user: User):
        self.current_renter = user
        return f"{user} day {self.get_date()} has rented book '{self.name}' with deadline {self.get_deadline()}"

    def is_rented(self):
        if self.rent_date and self.rent_deadline:
            today = datetime.now()
            deadline = datetime.strptime(self.rent_deadline, "%d/%m/%Y/%H:%M")
            if today < deadline:
                return True
        return False
