from tkinter import messagebox
import tkinter as tk
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
        book_frame = tk.Frame(app.root)
        book_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        canvas = tk.Canvas(book_frame)
        scrollbar = tk.Scrollbar(book_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for book in all_books:
            button = tk.Button(scrollable_frame, text=f"{book.title} by {book.author}", height=2, fg="white", bg="gray")
            button.configure(command=lambda b=button: self.update_button_color(b))
            button.pack(fill=tk.X)

        canvas.pack(side="left", fill=tk.X, expand=True)
        scrollbar.pack(side="right", fill="y")

        scrollable_frame.update()
        canvas.config(scrollregion=canvas.bbox("all"))

    def update_button_color(self, button):
        current_color = button.cget("bg")
        new_color = "green" if current_color == "gray" else "gray"
        button.configure(bg=new_color)
