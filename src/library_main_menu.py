import tkinter as tk
from books_data import book_store
from library_main_menu_strategies import *


class LibraryMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.user = None
        self.users = ["Admin", "Michał", "Kasia"]
        self.book_store = book_store
        self.buttons = {
            "Add Book": DefaultStrategy(),
            "Rent Book": DefaultStrategy(),
            "Return the Book": DefaultStrategy(),
            "Rented Books": DefaultStrategy(),
            "All Books": AllBooksStrategy(),
            "Add User": DefaultStrategy(),
            "Change User": ChangeUserStrategy(),
            "Exit": ExitStrategy()
        }
        self.user_label = tk.Label(self.root, text="", fg="blue")
        self.user_label.pack()
        self.create_user_buttons()

    def set_user(self, user):
        self.user = user
        self.user_label.config(text=f"Aktualny użytkownik: {self.user}", bg="gray")
        for widget in self.root.winfo_children():
            if widget is not self.user_label:
                widget.destroy()
        self.create_main_buttons()

    def create_user_buttons(self):
        for user in self.users:
            button = tk.Button(self.root, text=user, command=lambda u=user: self.set_user(u), height=2,
                               fg="white", bg="gray")
            button.pack(fill=tk.BOTH, expand=True)

    def create_main_buttons(self):
        for button_text, strategy in self.buttons.items():
            button_color = "gray"
            text_color = "white"
            if button_text == "Change User":
                button_color = "green"
            elif button_text == "Exit":
                button_color = "red"
            elif self.user != "Admin" and button_text in ["Add Book", "Add User", "Rented Books"]:
                continue
            button = tk.Button(self.root, text=button_text,
                               command=lambda bt=button_text: self.buttons[bt].execute(self, bt), height=5,
                               fg=text_color, bg=button_color)
            button.pack(fill=tk.BOTH, expand=True)