import tkinter as tk
from tkinter import messagebox
from books_data import book_store

class ButtonStrategy:
    def execute(self, app, button_text):
        pass

class ChangeUserStrategy(ButtonStrategy):
    def execute(self, app, button_text):
        app.user = None
        for widget in app.root.winfo_children():
            if widget is not app.user_label:
                widget.destroy()
        app.create_user_buttons()

class ExitStrategy(ButtonStrategy):
    def execute(self, app, button_text):
        app.root.destroy()

class DefaultStrategy(ButtonStrategy):
    def execute(self, app, button_text):
        messagebox.showinfo("Button Pressed", f"You pressed {button_text}")

class AllBooksStrategy(ButtonStrategy):
    def execute(self, app, button_text):
        all_books = app.book_store.get_all_books()
        new_window = tk.Toplevel(app.root)
        new_window.title("All Books")
        new_window.geometry("800x600")
        new_window.configure(bg='gray')
        scrollbar = tk.Scrollbar(new_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox = tk.Listbox(new_window, yscrollcommand=scrollbar.set, bg='gray', fg='black', font=("Helvetica", 12))
        for book in all_books:
            listbox.insert(tk.END, f"Title: {book.title}, Author: {book.author}")
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        back_button = tk.Button(new_window, text="Back", command=new_window.destroy, bg='green', fg='white', font=("Helvetica", 12))
        back_button.pack(side=tk.BOTTOM)
        scrollbar.config(command=listbox.yview)

class LibraryMenuApp:
    def __init__(self, root):
        self.root = root
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
            button = tk.Button(self.root, text=user, command=lambda u=user: self.set_user(u), height=2, width=50, fg="white", bg="gray")
            button.pack()

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
            button = tk.Button(self.root, text=button_text, command=lambda bt=button_text: self.buttons[bt].execute(self, bt), height=5, width=50, fg=text_color, bg=button_color)
            button.pack()
