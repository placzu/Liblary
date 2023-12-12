import tkinter as tk
from tkinter import messagebox

class LibraryMenuApp:
    def __init__(self, root):
        self.root = root
        self.buttons = ["Add Book", "Rent Book", "Rented Books", "All Books", "Add User"]
        for button_text in self.buttons:
            button = tk.Button(self.root, text=button_text, command=lambda bt=button_text: self.show_message(bt), height=5, width=50, fg="white", bg="gray")
            button.pack()

    def show_message(self, button_text):
        messagebox.showinfo("Button Pressed", f"You pressed {button_text}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryMenuApp(root)
    root.mainloop()
