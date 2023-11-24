class Book:

    def __init__(self, name: str = "Unknow", author: str = "Unknown", short_description: str = "No description", pages: int = 0):
        self.name = name
        self.author = author
        self.short_description = short_description
        self.pages = pages

    def present(self):


        return (
            f"Book entitled {self.name} written by: {self.author}, with a short review {self.short_description} and {self.pages} pages.")
