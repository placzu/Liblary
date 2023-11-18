import unittest
from src.return_class import *


class Test_ReturnClass(unittest.TestCase):
    def test_return_number(self):
        example = ReturnClass()
        actual_value = example.return_number()
        self.assertEqual(actual_value, 897)