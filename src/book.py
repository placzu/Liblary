class Book:

    def __init__(self, name: str, author: str, pages: int, short_description: str = None):
        self.name = name
        self.author = author
        self.short_description = short_description if short_description is not None else ""
        self.pages = pages

    def present(self):
        return (
            f"Book entitled {self.name} written by: {self.author}, with a short review {self.short_description} and {self.pages} pages.")
