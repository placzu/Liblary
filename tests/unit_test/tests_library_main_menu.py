import sys

sys.path.append('D:\\Liblary\\src')

import unittest
import tkinter as tk
from library_main_menu import LibraryMenuApp


class TestLibraryMenuApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.app = LibraryMenuApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_initial_user_is_none(self):
        self.assertIsNone(self.app.user)

    def test_users_list(self):
        self.assertEqual(self.app.users, ["Admin", "Michał", "Kasia"])

    def test_buttons_list(self):
        self.assertEqual(self.app.buttons,
                         ["Add Book", "Rent Book", "Return the Book", "Rented Books", "All Books", "Add User",
                          "Change User", "Exit"])

    def test_set_user(self):
        self.app.set_user("Admin")
        self.assertEqual(self.app.user, "Admin")

    def test_create_user_buttons(self):
        self.assertEqual(len(self.root.winfo_children()), len(self.app.users))

    def test_create_main_buttons(self):
        self.app.set_user("Admin")
        self.assertEqual(len(self.root.winfo_children()), len(self.app.buttons))

    def test_create_main_buttons_non_admin(self):
        self.app.set_user("Michał")
        self.assertEqual(len(self.root.winfo_children()), len(self.app.buttons) - 3)


if __name__ == '__main__':
    unittest.main()
