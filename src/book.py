class Book:

    def __init__(self, name: str, author: str, short_description: str, pages: int):
        self.name = name
        self.author = author
        self.short_description = short_description
        self.pages = pages

    def present(self):
        return (
            f"Book entitled {self.name} written by: {self.author}, with a short review {self.short_description} and {self.pages} pages.")
