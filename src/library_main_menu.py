import tkinter as tk
from constants import ADMIN, USER
from users_data import User, load_users, save_users
from books_data import book_store
from library_main_menu_strategies import (
    SearchBookStrategy, AllBooksStrategy, ChangeUserStrategy,
    ExitStrategy, AddBookStrategy, RentedBooksStrategy, ReturnBookStrategy,
    RemoveBookStrategy, AddUserStrategy, DeleteUserStrategy
)


class LibraryMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.users = self.initialize_users()
        self.users = self.initialize_users()
        self.book_store = book_store
        self.buttons = self.initialize_buttons()
        self.user_label = tk.Label(self.root, text="", fg="blue")
        self.user_label.pack()
        self.search_entry = None
        self.create_user_buttons()

    def initialize_users(self):
        users = load_users()
        if not users:
            admin_user = User("Michal", "Admin", "123456789", "Admin Address", "admin@example.com", "Admin")
            users = [admin_user]
            save_users(users)
        return users

    def initialize_buttons(self):
        return {
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

    def set_user(self, user):
        self.user = user
        self.user_label.config(text=f"User: {self.user.first_name} {self.user.last_name}", bg="gray")
        self.clear_root_widgets()
        self.create_main_buttons()

    def clear_root_widgets(self):
        for widget in self.root.winfo_children():
            if widget is not self.user_label:
                widget.destroy()

    def create_main_buttons(self):
        for button_text, strategy in self.buttons.items():
            if self.user.status != ADMIN and button_text in ["Add Book", "Add User", "Rented Books", "Remove Book",
                                                             "Delete User"]:
                continue
            button_color = self.get_button_color(button_text)
            button = tk.Button(self.root, text=button_text,
                               command=lambda bt=button_text: self.buttons[bt].execute(self, bt), height=5,
                               fg="white", bg=button_color)
            button.pack(fill=tk.BOTH, expand=True)

    def get_button_color(self, button_text):
        if button_text == "Change User":
            return "green"
        elif button_text == "Exit":
            return "red"
        else:
            return "gray"

    def create_user_buttons(self):
        for user in self.users:
            button = tk.Button(self.root, text=f"{user.first_name} {user.last_name}",
                               command=lambda u=user: self.set_user(u), height=2, fg="white", bg="gray")
            button.pack(fill=tk.BOTH, expand=1)

    def back_to_main_menu(self):
        self.buttons["All Books"].clear_book_buttons()
        self.set_user(self.user)

    def create_scrollable_book_frame(self):
        canvas = tk.Canvas(self.root, height=300, width=200)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        book_frame = tk.Frame(canvas)
        book_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=book_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill=tk.BOTH, expand=True)
        scrollbar.pack(side="right", fill="y")
        return book_frame
