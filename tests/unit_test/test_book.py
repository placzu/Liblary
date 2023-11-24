import unittest
from src.book import Book


def setUp():
    testemptybook = Book()

class TestBook(unittest.TestCase):

    def testbook_present(self):
        testbook = Book(name="Biography of John", author="John Grimmes", short_description="John's life story",
                        pages=264)
        expected_output = "Book entitled Biography of John written by: John Grimmes, with a short review John's life story and 264 pages."
        self.assertEqual(testbook.present(), expected_output)

    def testemptybook_present(self):
        testemptybook = Book(name="Best composer", author="Rok Nardin", pages=57)
        expected_solution = "Book entitled Best composer written by: Rok Nardin, with a short review No description and 57 pages."
        self.assertEqual(testemptybook.present(), expected_solution)
