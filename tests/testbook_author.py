import unittest
from src.book import Book
class TestBookAuthor(unittest.TestCase):
    def testbookauthor(self):
        example = Book.__init__(self, name="gowno",author="gowno",short_description="gowno",pages=69)
        correct_book_author = example

        self.assertEqual(correct_book_author, example)