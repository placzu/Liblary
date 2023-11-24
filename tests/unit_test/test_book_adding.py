import unittest

import src.book_adding
from src.library import Library
from src.book_adding import Adding_Book



class Test_Adding_Book(unittest.TestCase):

    def testbook_adding(self):
        resoult = src.book_adding.book
        expected_resoult = src.book_adding.book1
        self.assertEqual(expected_resoult, resoult)


