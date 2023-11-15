import unittest


class ReturnClass:
    def return_number(self):
        return 897
back = ReturnClass()
resolution = back.return_number()
print(f"number = {resolution}")

class Test_ReturnClass(unittest.TestCase):
    def test_return_number(self):
        back = ReturnClass()
        test_resolution = back.return_number()
        self.assertEqual(test_resolution, 897)

if __name__ == "__main__":
    unittest.main()










