import unittest
from email_validator import EmailNotValidError, validate_email
from datetime import datetime, timedelta
from src.library import Library
from src.book import Book
from src.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book = Book("lord of the rings", "J.R.R", 987, "story about some rings")

    def test_add_user_first_name_and_last_name(self):
        self.user = User("John", "Carter")
        self.library.add_user(self.user)
        actual_user = f"{self.user.first_name} {self.user.last_name}"
        expected_user = "John Carter"
        self.assertEqual(expected_user, actual_user)

    def test_add_user_first_name(self):
        self.user = User("John")
        self.library.add_user(self.user)
        actual_user = f"{self.user.first_name}"
        expected_user = "John"
        self.assertEqual(expected_user, actual_user)

    def test_add_user_first_name_and_email(self):
        self.user = User("John", email="johncarter@gmail.com")
        self.library.add_user(self.user)
        actual_user = [self.user]
        expected_user = self.library.users
        self.assertEqual(expected_user, actual_user)

    def test_add_user_first_name_and_phone_number(self):
        self.user = User("John", phone_number="+48123456789")
        self.library.add_user(self.user)
        actual_user = [self.user]
        expected_user = self.library.users
        self.assertEqual(expected_user, actual_user)

    def test_add_user_first_name_and_borrowed_book(self):
        self.user = User("John", borrowed_books="Toy Story 3")
        self.library.add_user(self.user)
        actual_user = [self.user]
        expected_user = self.library.users
        self.assertEqual(expected_user, actual_user)

    def test_add_user_with_all_values(self):
        self.user = User("John", "Carter", email="johncarter@gmial.com", phone_number="123456789",
                         borrowed_books="Toy Story 3")
        self.library.add_user(self.user)
        actual_user = [self.user]
        expected_user = self.library.users
        self.assertEqual(expected_user, actual_user)

    def test_users_number(self):
        self.user = User("John", "Carter", email="JohnCarter@gmail.com", phone_number="+48123456789")
        self.library.add_user(self.user)
        self.user = User ("Bob", "Carter", email="BobCarter@gmail.com", phone_number="+48987654321")
        self.library.add_user(self.user)
        self.user = User("Michal", "Kosakowski", email="Michal@gmail.com", phone_number="+47123789456")
        self.library.add_user(self.user)
        print(self.library.users)
        actual_output = len(self.library.users)
        self.assertEqual(actual_output, 3)
    def test_validate_phone_number_correct(self):
        self.user = User("John", "Carter", phone_number="123456789")
        resolution = self.user.phone_number
        self.assertEqual(resolution, "123456789")

    def test_validate_phone_number_incorrect(self):
        self.user = User("John", "Carter", phone_number="12346789")
        resolution = self.user.phone_number
        self.assertEqual(resolution, "12346789")

    def test_validate_email_incorrect(self):
        self.user = User("John", "Carter", email="JohnCarter@gmailcom")
        resolution = self.user.email
        expected_error_message = (f"JohnCarter@gmailcom")
        self.assertEqual(resolution, expected_error_message)
