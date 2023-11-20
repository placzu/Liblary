import unittest
from src.book import Book
class TestBookShortDescription(unittest.TestCase):
    def testbookshort_description(self):
        example = Book.__init__(self, name="gowno",author="gowno",short_description="gowno",pages=69)
        correct_book_short_description = example

        self.assertEqual(correct_book_short_description, example)