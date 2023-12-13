import tkinter as tk
from tkinter import messagebox


class LibraryMenuApp:
    def __init__(self, root):
        self.root = root
        self.user = None
        self.users = ["Admin", "Michał", "Kasia"]
        self.buttons = ["Add Book", "Rent Book", "Return the Book", "Rented Books", "All Books", "Add User",
                        "Change User", "Exit"]
        self.create_user_buttons()

    def create_user_buttons(self):
        for user in self.users:
            button = tk.Button(self.root, text=user, command=lambda u=user: self.set_user(u), height=2, width=50,
                               fg="white", bg="gray")
            button.pack()

    def set_user(self, user):
        self.user = user
        for widget in self.root.winfo_children():
            widget.destroy()
        for button_text in self.buttons:
            if self.user != "Admin" and button_text in ["Add Book", "Add User", "Rented Books"]:
                continue
            button = tk.Button(self.root, text=button_text, command=lambda bt=button_text: self.show_message(bt),
                               height=5, width=50, fg="white", bg="gray")
            button.pack()

    def show_message(self, button_text):
        if button_text == "Change User":
            self.user = None
            for widget in self.root.winfo_children():
                widget.destroy()
            self.create_user_buttons()
        elif button_text == "Exit":
            self.root.destroy()
        else:
            messagebox.showinfo("Button Pressed", f"You pressed {button_text}")
