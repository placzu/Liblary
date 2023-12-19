from tkinter import messagebox
import tkinter as tk
from abc import ABC, abstractmethod


class ButtonStrategy(ABC):
    @abstractmethod
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
        app.root.quit()


class DefaultStrategy(ButtonStrategy):
    def execute(self, app, button_text):
        messagebox.showinfo("Button Pressed", f"You pressed {button_text}")


class AllBooksStrategy(ButtonStrategy):
    def __init__(self):
        self.book_buttons = {}
        self.book_frame = None

    def execute(self, app, button_text, books=None):
        for widget in app.root.winfo_children():
            if widget is not app.user_label:
                widget.destroy()

        self.book_frame = self.create_scrollable_book_frame(app.root)
        all_books = [book for book in app.book_store.get_all_books() if not book.is_rented] if books is None else books
        for book in all_books:
            self.add_book_button(self.book_frame, book, app)

        button_frame = tk.Frame(app.root)
        button_frame.pack()

        rent_button = tk.Button(button_frame, text="Rent Book",
                                command=lambda: RentBookStrategy().execute(app, self.book_buttons), height=2,
                                fg="white", bg="gray")
        rent_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        back_button = tk.Button(button_frame, text="Back", command=app.back_to_main_menu, height=2, fg="white",
                                bg="gray")
        back_button.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

    def add_book_button(self, frame, book, app):
        if frame.winfo_exists():
            button = tk.Button(frame, text=f"{book.title} by {book.author}", height=2, fg="white", bg="gray")
            button.configure(command=lambda b=button: self.toggle_button_color(b))
            button.pack(fill=tk.BOTH, expand=1)
            self.book_buttons[book] = button

    def create_scrollable_book_frame(self, root):
        canvas = tk.Canvas(root, height=300, width=200)
        scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
        book_frame = tk.Frame(canvas)
        book_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=book_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill=tk.BOTH, expand=True)
        scrollbar.pack(side="right", fill="y")
        return book_frame

    def toggle_button_color(self, button):
        current_color = button.cget("bg")
        new_color = "green" if current_color == "gray" else "gray"
        button.configure(bg=new_color)

    def clear_book_buttons(self):
        self.book_buttons.clear()


class RentedBooksStrategy(ButtonStrategy):
    def __init__(self):
        self.book_buttons = {}
        self.book_frame = None

    def execute(self, app, button_text):
        for widget in app.root.winfo_children():
            if widget is not app.user_label:
                widget.destroy()

        search_label = tk.Label(app.root, text="Search by renter:")
        search_label.pack()
        search_entry = tk.Entry(app.root)
        search_entry.pack()

        search_button = tk.Button(app.root, text="Search",
                                  command=lambda: self.display_books(app, search_entry.get()))
        search_button.pack()

        self.book_frame = self.create_scrollable_book_frame(app.root)
        self.display_books(app)

        back_button = tk.Button(app.root, text="Back", command=app.back_to_main_menu, height=2, fg="white", bg="gray")
        back_button.pack()

    def add_book_button(self, frame, book, app):
        if frame.winfo_exists():
            button = tk.Button(frame, text=f"{book.title} by {book.author}", height=2, fg="white", bg="gray")
            button.configure(command=lambda b=button: self.toggle_button_color(b))
            button.pack(fill=tk.BOTH, expand=1)
            self.book_buttons[book] = button

    def create_scrollable_book_frame(self, root):
        canvas = tk.Canvas(root, height=300, width=200)
        scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
        book_frame = tk.Frame(canvas)
        book_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=book_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill=tk.BOTH, expand=True)
        scrollbar.pack(side="right", fill="y")
        return book_frame

    def toggle_button_color(self, button):
        current_color = button.cget("bg")
        new_color = "green" if current_color == "gray" else "gray"
        button.configure(bg=new_color)

    def display_books(self, app, renter=None):
        for book, button in self.book_buttons.items():
            button.destroy()
        self.book_buttons.clear()

        rented_books = [book for book in app.book_store.get_all_books() if book.is_rented and (renter is None or book.rented_by == renter)]
        for book in rented_books:
            self.add_book_button(self.book_frame, book, app)

class SearchBookStrategy(ButtonStrategy):
    def execute(self, app, button_text):
        for widget in app.root.winfo_children():
            if widget is not app.user_label:
                widget.destroy()
        app.create_search_menu()


class RentBookStrategy(ButtonStrategy):
    def execute(self, app, book_buttons):
        rented_books = [book for book, button in book_buttons.items() if button.cget("bg") == "green" and not book.is_rented]
        if not rented_books:
            messagebox.showinfo("No books to rent", "No book has been selected for rent or selected books are already rented.")
            return
        for book in rented_books:
            book.is_rented = True
            book.rented_by = app.user
        rented_books_titles = "\n".join([f"- {book.title} by {book.author}" for book in rented_books])
        messagebox.showinfo("Rented books", f"User {app.user} rented the following books:\n{rented_books_titles}")
        app.buttons["All Books"].execute(app, "All Books")


class AddBookStrategy(ButtonStrategy):
    def execute(self, app, button_text):
        for widget in app.root.winfo_children():
            if widget is not app.user_label:
                widget.destroy()

        title_label = tk.Label(app.root, text="Book title:")
        title_label.pack()
        title_entry = tk.Entry(app.root)
        title_entry.pack()

        author_label = tk.Label(app.root, text="Book author:")
        author_label.pack()
        author_entry = tk.Entry(app.root)
        author_entry.pack()

        add_button = tk.Button(app.root, text="Add book",
                               command=lambda: self.add_book(app, title_entry.get(), author_entry.get()))
        add_button.pack()

        back_button = tk.Button(app.root, text="Back", command=app.back_to_main_menu)
        back_button.pack()

    def add_book(self, app, title, author):
        app.book_store.add_book(title, author)
        messagebox.showinfo("Book added", f"Added book {title} by {author} to the store.")
