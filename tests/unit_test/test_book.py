import unittest
from src.book import Book


class TestBook(unittest.TestCase):

    def setUp(self):
        self.testbook = Book(name="Biography of John", author="John Grimmes", short_description="John's life story", pages=264)

    def test_book_present(self):
        expected_output = "Book entitled Biography of John written by: John Grimmes, with a short reviev John's life story and 264 pages."
        self.assertEqual(self.testbook.present(), expected_output)
