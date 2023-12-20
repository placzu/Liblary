import tkinter as tk
from users_data import User
from books_data import book_store
from library_main_menu_strategies import SearchBookStrategy, DefaultStrategy, AllBooksStrategy, ChangeUserStrategy, \
    ExitStrategy, AddBookStrategy, RentedBooksStrategy, ReturnBookStrategy, RemoveBookStrategy, AddUserStrategy, \
    DeleteUserStrategy
from users_data import User, load_users, save_users


class LibraryMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.user = None
        self.users = self.initialize_users()
        self.book_store = book_store
        self.buttons = {
            "Add Book": AddBookStrategy(),
            "Remove Book": RemoveBookStrategy(),
            "Return the Book": ReturnBookStrategy(),
            "Rented Books": RentedBooksStrategy(),
            "All Books": AllBooksStrategy(),
            "Search Book": SearchBookStrategy(),
            "Add User": AddUserStrategy(),
            "Delete User": DeleteUserStrategy(),
            "Change User": ChangeUserStrategy(),
            "Exit": ExitStrategy()
        }
        self.user_label = tk.Label(self.root, text="", fg="blue")
        self.user_label.pack()
        self.search_entry = None
        self.create_user_buttons()

    def initialize_users(self):
        users = load_users()
        if not users:
            admin_user = User("Admin", "Admin", "123456789", "Admin Address", "admin@example.com", "Admin")
            user1 = User("User", "User", "123456789", "User Address", "user@example.com", "User")
            users = [admin_user, user1]
            save_users(users)
        return users

    def search_book(self):
        query = self.search_entry.get().lower()
        matching_books = [book for book in self.book_store.books if
                          query in book.title.lower() or query in book.author.lower()]
        for book in matching_books:
            print(f"Znaleziono książkę: {book.title} autorstwa {book.author}")

    def create_search_menu(self):
        for widget in self.root.winfo_children():
            if widget is not self.user_label:
                widget.destroy()

        label = tk.Label(self.root, text="Enter the name or author of the book:", fg="blue")
        label.pack()
        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack()
        search_button = tk.Button(self.root, text="Szukaj", command=self.search_book, height=2, fg="white", bg="gray")
        search_button.pack()
        back_button = tk.Button(self.root, text="Back", command=self.back_to_main_menu, height=2, fg="white",
                                bg="gray")
        back_button.pack()

    def search_book(self):
        query = self.search_entry.get().lower()
        matching_books = [book for book in self.book_store.books if
                          query in book.title.lower() or query in book.author.lower()]
        self.buttons["All Books"].execute(self, "All Books",
                                          matching_books)

    def set_user(self, user):
        self.user = user
        self.user_label.config(text=f"User: {self.user.first_name} {self.user.last_name}", bg="gray")
        for widget in self.root.winfo_children():
            if widget is not self.user_label:
                widget.destroy()
        self.create_main_buttons()

    def create_main_buttons(self):
        for button_text, strategy in self.buttons.items():
            button_color = "gray"
            text_color = "white"
            if button_text == "Change User":
                button_color = "green"
            elif button_text == "Exit":
                button_color = "red"
            elif self.user.status != "Admin" and button_text in ["Add Book", "Add User", "Rented Books", "Remove Book",
                                                                 "Delete User"]:
                continue
            button = tk.Button(self.root, text=button_text,
                               command=lambda bt=button_text: self.buttons[bt].execute(self, bt), height=5,
                               fg=text_color, bg=button_color)
            button.pack(fill=tk.BOTH, expand=True)

    def create_user_buttons(self):
        for user in self.users:
            button = tk.Button(self.root, text=f"{user.first_name} {user.last_name}",
                               command=lambda u=user: self.set_user(u), height=2, fg="white", bg="gray")
            button.pack(fill=tk.BOTH, expand=1)

    def back_to_main_menu(self):
        self.buttons["All Books"].clear_book_buttons()
        self.set_user(self.user)
