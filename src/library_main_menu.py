import tkinter as tk
from tkinter import messagebox, Toplevel, Text, Scrollbar, END
import unittest


class LibraryMenuApp:
    def __init__(self, root):
        self.root = root
        self.user = None
        self.users = ["Admin", "Michał", "Kasia"]
        self.buttons = ["Add Book", "Rent Book", "Return the Book", "Rented Books", "All Books", "Add User",
                        "Change User", "Run Tests", "Exit"]
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
        self.create_main_buttons()

    def create_main_buttons(self):
        for button_text in self.buttons:
            if self.user != "Admin" and button_text in ["Add Book", "Add User", "Rented Books", "Run Tests"]:
                continue
            button_color = "gray"
            text_color = "white"
            if button_text == "Change User":
                button_color = "green"
            elif button_text == "Exit":
                button_color = "red"
            elif button_text == "Run Tests":
                button_color = "yellow"
                text_color = "black"
            button = tk.Button(self.root, text=button_text, command=lambda bt=button_text: self.show_message(bt),
                               height=5, width=50, fg=text_color, bg=button_color)
            button.pack()

    def show_message(self, button_text):
        if button_text == "Change User":
            self.user = None
            for widget in self.root.winfo_children():
                widget.destroy()
            self.create_user_buttons()
        elif button_text == "Exit":
            self.root.destroy()
        elif button_text == "Run Tests":
            self.run_tests()
        else:
            messagebox.showinfo("Button Pressed", f"You pressed {button_text}")

    def run_tests(self):
        from tests_library_main_menu import TestLibraryMenuApp
        suite = unittest.TestLoader().loadTestsFromTestCase(TestLibraryMenuApp)
        result = unittest.TextTestRunner().run(suite)
        output_window = Toplevel(self.root)
        output_window.title("Test Results")
        output_text = Text(output_window, wrap='word', height=24, width=80)
        output_text.pack(fill='both', expand=True)
        scrollbar = Scrollbar(output_text)
        scrollbar.pack(side='right', fill='y')
        output_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=output_text.yview)
        if result.wasSuccessful():
            output_text.insert(END, "All tests passed successfully.")
        else:
            output_text.insert(END, "Some unit tests failed.")
