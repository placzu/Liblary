from datetime import datetime, timedelta


class Book:

    def __init__(self, name: str, author: str, pages: int, short_description: str = None, rent_date: str = None,
                 rent_deadline: str = None, current_renter: str = None):
        self.name = name
        self.author = author
        self.short_description = short_description if short_description is not None else ""
        self.pages = pages
        self.rent_date = rent_date if rent_date is not None else ""
        self.rent_deadline = rent_deadline if rent_deadline is not None else ""
        self.current_renter = current_renter if current_renter is not None else ""

    def present(self):
        return (
            f"Book entitled {self.name} written by: {self.author}, with a short review {self.short_description} and {self.pages} pages.")

    def get_date(self):
        today = datetime.now()
        self.rent_date = today.strftime("%d/%m/%Y/%H:%M")
        return self.rent_date

    def get_deadline(self):
        today = datetime.now()
        self.rent_deadline = (today + timedelta(days=14)).strftime("%d/%m/%Y/%H:%M")
        return self.rent_deadline

    def current_renter(self):
        self.current_renter
