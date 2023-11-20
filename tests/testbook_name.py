import unittest
from src.book import Book
class TestBookName(unittest.TestCase):
    def testbookname(self):
        example = Book.__init__(self, name="gowno",author="gowno",short_description="gowno",pages=69)
        correct_book_name = example

        self.assertEqual(correct_book_name, example)

