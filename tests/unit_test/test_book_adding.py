import unittest
from src.library import Library
from src.book import Book


class Test_AddingBook(unittest.TestCase):

    def test_add_book(self):
        library = Library()
        book = Book("lord of the rings", "J.R.R", 987, "story about some rings")
        library.add_book(book)
        expected_library = [book]


        self.assertEqual(expected_library, library.books)
