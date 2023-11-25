import unittest
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

    def test_books_number(self):
        self.library.add_book(self.book)
        expected_number = 1
        actual_number = self.library.get_number_of_books()
        self.assertEqual(expected_number, actual_number)

    def test_remove_book(self):
        expected_number_after_remove = 0
        actual_number_after_remove = self.library.get_number_of_books()
        self.assertEqual(actual_number_after_remove, expected_number_after_remove)
