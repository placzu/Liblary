import unittest
from src.book import Book


class TestBook(unittest.TestCase):

    def test_book_present(self):
        self.testbook = Book(name="Biography of John", author="John Grimmes", short_description="John's life story",
                             pages=264)
        expected_output = "Book entitled Biography of John written by: John Grimmes, with a short review John's life story and 264 pages."
        self.assertEqual(self.testbook.present(), expected_output)

    def test_empty_book_present(self):
        self.testemptybook = Book(name="", author="", short_description="", pages=0)
        expected_output = "Book entitled  written by: , with a short review  and 0 pages."
        self.assertEqual(self.testemptybook.present(), expected_output)
