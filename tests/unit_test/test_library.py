import unittest
from datetime import datetime, timedelta
from src.library import Library
from src.book import Book


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

    def test_removing_hired_book_from_books(self):
        self.library.add_book(self.book)
        self.library.remove_hired_book_from_books(self.book)
        actual_value = self.library.get_number_of_books()
        excepted_value = 0
        self.assertEqual(actual_value, excepted_value)

    def test_add_book_to_hired_books(self):
        self.library.add_book(self.book)
        self.library.add_book_to_hired_books(self.book)
        actual_value = self.library.get_hired_books_number()
        expected_value = 1
        self.assertEqual(actual_value, expected_value)

    def test_get_hired_books_number(self):
        self.library.add_book(self.book)
        self.library.add_book_to_hired_books(self.book)
        expected_number = 1
        actual_number = self.library.get_hired_books_number()
        self.assertEqual(expected_number, actual_number)

    def test_get_date(self):
        actual_date = self.book.get_date()
        today = datetime.now()
        expected_date = today.strftime("%d/%m/%Y/%H:%M")
        self.assertEqual(actual_date, expected_date)

    def test_get_deadline(self):
        today = datetime.now()
        actual_deadline = self.book.get_deadline()
        expected_deadline = (today + timedelta(days=14)).strftime("%d/%m/%Y/%H:%M")
        self.assertEqual(actual_deadline, expected_deadline)
