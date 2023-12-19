class Book:
    def __init__(self, title, author, is_rented=False):
        self.title = title
        self.author = author
        self.is_rented = is_rented

class BookStore:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def get_all_books(self):
        return self.books

book_store = BookStore()
book_store.add_book("The Witcher", "Andrzej Sapkowski")
book_store.add_book("1984", "George Orwell")
book_store.add_book("To Kill a Mockingbird", "Harper Lee")
book_store.add_book("The Science of Rick and Morty. Non-scientific guide to the world of science", "Matt Brady")
book_store.add_book("Book of people. The story of how we became us", "Adam Rutheford")
book_store.add_book("The brain rules", "Kaja Nordengen")
book_store.add_book("The brain exercises", "Kaja Nordengen")
book_store.add_book("Introduction to meme theory", "Dawid Fibich")
book_store.add_book("About the witch and the monster. Zielona Góra witch trials", "Igor Myszkiewicz")
book_store.add_book("Body and society. Men, women and sexual abstinence in early Christianity", "Peter Brown")
book_store.add_book("The Lost Tomb", "Douglas Preston")
book_store.add_book("Papacy. Inconvenient facts", "Adam Skwierczyński")
book_store.add_book("People", "Michael Ruse")
book_store.add_book("Mythologies of the world", "Unknown author")
book_store.add_book("Silk roads", "Unknown author")
book_store.add_book("Literature and controversies", "Unknown author")
book_store.add_book("Library \"Tawacinu\"", "Unknown author")
book_store.add_book("You can give birth easier", "Unknown author")
book_store.add_book("Saganami", "Unknown author")
book_store.add_book("Chronicles of the Earth", "Unknown author")
book_store.add_book("The Great Gatsby", "F. Scott Fitzgerald")
book_store.add_book("Moby Dick", "Herman Melville")
book_store.add_book("War and Peace", "Leo Tolstoy")
book_store.add_book("Pride and Prejudice", "Jane Austen")
book_store.add_book("To the Lighthouse", "Virginia Woolf")
book_store.add_book("Ulysses", "James Joyce")
book_store.add_book("Don Quixote", "Miguel de Cervantes")
book_store.add_book("The Catcher in the Rye", "J.D. Salinger")
book_store.add_book("One Hundred Years of Solitude", "Gabriel Garcia Marquez")
book_store.add_book("The Odyssey", "Homer")
book_store.add_book("Crime and Punishment", "Fyodor Dostoevsky")
book_store.add_book("The Divine Comedy", "Dante Alighieri")
book_store.add_book("Madame Bovary", "Gustave Flaubert")
book_store.add_book("The Iliad", "Homer")
book_store.add_book("The Brothers Karamazov", "Fyodor Dostoevsky")
book_store.add_book("In Search of Lost Time", "Marcel Proust")
book_store.add_book("Anna Karenina", "Leo Tolstoy")
book_store.add_book("The Adventures of Huckleberry Finn", "Mark Twain")
book_store.add_book("Heart of Darkness", "Joseph Conrad")
book_store.add_book("Frankenstein", "Mary Shelley")
book_store.add_book("rented book", "renter")