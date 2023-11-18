import unittest
from src.return_class import ReturnClass


class TestReturnClass(unittest.TestCase):
    def test_return_number(self):
        example = ReturnClass()
        actual_value = example.return_number()
        expected_value = 897
        self.assertEqual(actual_value, expected_value)