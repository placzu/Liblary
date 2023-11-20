
class Book:
    def __init__(self, name, author, short_description, pages):
        self.name = name
        self.author = author
        self.short_description = short_description
        self.pages = pages

    def present(self):
        return f"Book entitled,{self.name}, written by, {self.author}, with a short reviev {self.short_description}, and {self.pages} pages."

river_story = Book(name="River", author="John River", short_description="Story of the River", pages="999")
print(river_story.present())
