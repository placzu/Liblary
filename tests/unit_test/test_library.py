import unittest
from datetime import datetime, timedelta
from src.library import Library
from src.book import Book
from src.user import User


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book = Book("lord of the rings", "J.R.R", 987, "story about some rings")

    def test_add_book(self):
        self.library.add_book(self.book)
        expected_library = [self.book]
        actual_library = self.library.books
        self.assertEqual(expected_library, actual_library)

    def test_remove_book(self):
        self.library.add_book(self.book)
        self.library.remove_book(self.book)
        expected_number_after_remove = 0
        actual_number_after_remove = self.library.get_number_of_books()
        self.assertEqual(actual_number_after_remove, expected_number_after_remove)

    def test_get_number_of_books(self):
        self.library.add_book(self.book)
        expected_number = 1
        actual_number = self.library.get_number_of_books()
        self.assertEqual(expected_number, actual_number)

    def test_find_current_rented_books(self):
        user = User("John", "Carter")
        self.library.add_book(self.book)
        self.library.book_rent(user, self.book)
        rented_books = self.library.find_current_rented_books()
        self.assertEqual(len(rented_books), 1)

    def test_correct_book_rent(self):
        self.library.add_book(self.book)
        user = User("John", "Carter", email="johncarter@gmial.com", phone_number=123456789)
        expected_output = "John rent a lord of the rings"
        actual_output = self.library.book_rent(user, self.book)
        self.assertEqual(expected_output, actual_output)

    def test_incorect_book_rent(self):
        self.library.add_book(self.book)
        self.library.remove_book(self.book)
        user = User("John", "Carter", email="johncarter@gmial.com", phone_number=123456789)
        expected_output = "don't have lord of the rings"
        actual_output = self.library.book_rent(user, self.book)
        self.assertEqual(expected_output, actual_output)
