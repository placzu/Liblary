import unittest

class Test_ReturnClass(unittest.TestCase):
    def test_return_number(self):
        back = ReturnClass()
        test_resolution = back.return_number()
        self.assertEqual(test_resolution, 897)