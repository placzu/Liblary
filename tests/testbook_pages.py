import unittest
from src.book import Book
class TestBookPages(unittest.TestCase):
    def testbookpages(self):
        example = Book.__init__(self, name="gowno",author="gowno",short_description="gowno",pages=69)
        correct_book_pages = example

        self.assertEqual(correct_book_pages, example)