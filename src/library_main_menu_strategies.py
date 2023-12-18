from tkinter import messagebox
import tkinter as tk


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
        app.root.quit()


class DefaultStrategy(ButtonStrategy):
    def execute(self, app, button_text):
        messagebox.showinfo("Button Pressed", f"You pressed {button_text}")


class AllBooksStrategy(ButtonStrategy):
    def __init__(self):
        self.book_frame = None

    def execute(self, app, button_text):
        all_books = app.book_store.get_all_books()
        if self.book_frame is None:
            self.book_frame = self.create_scrollable_book_frame(app.root)
        for book in all_books:
            self.add_book_button(self.book_frame, book)

    def create_scrollable_book_frame(self, root):
        canvas = tk.Canvas(root, height=300, width=200)  # Limit the width of the canvas
        scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
        book_frame = tk.Frame(canvas)
        book_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=book_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill=tk.BOTH, expand=True)
        scrollbar.pack(side="right", fill="y")
        return book_frame

    def add_book_button(self, frame, book):
        button = tk.Button(frame, text=f"{book.title} by {book.author}", height=2, fg="white", bg="gray")
        button.configure(command=lambda b=button: self.toggle_button_color(b))
        button.pack(fill=tk.BOTH, expand=1)

    def toggle_button_color(self, button):
        current_color = button.cget("bg")
        new_color = "green" if current_color == "gray" else "gray"
        button.configure(bg=new_color)