import unittest
import tkinter as tk
from library_main_menu import LibraryMenuApp


class TestLibraryMenuApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.app = LibraryMenuApp(self.root)

    def test_initial_user_is_none(self):
        self.assertIsNone(self.app.user)

    def test_users_list(self):
        self.assertEqual(self.app.users, ["Admin", "Michał", "Kasia"])

    def test_buttons_list(self):
        self.assertEqual(self.app.buttons,
                         ["Add Book", "Rent Book", "Return the Book", "Rented Books", "All Books", "Add User",
                          "Change User", "Run Tests", "Exit"])

    def test_set_user(self):
        self.app.set_user("Admin")
        self.assertEqual(self.app.user, "Admin")
