import unittest
from datetime import datetime, timedelta
from src.library import Library
from src.book import Book
from src.user import User


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book = Book("lord of the rings", "J.R.R", 987, "story about some rings")

    def test_add_user_first_name_and_last_name(self):
        self.user = User("John", "Carter")
        self.library.add_person(self.user)
        actual_user = f"{self.user.first_name} {self.user.last_name}"
        expected_user = "John Carter"
        self.assertEqual(expected_user, actual_user)

    def test_add_person_first_name(self):
        self.user = User("John")
        self.library.add_person(self.user)
        actual_user = f"{self.user.first_name}"
        expected_user = "John"
        self.assertEqual(expected_user, actual_user)

    def test_add_person_first_name_and_email(self):
        self.user = User("John", email="johncarter@gmial.com")
        self.library.add_person(self.user)
        actual_user = [self.user]
        expected_user = self.library.users
        self.assertEqual(expected_user, actual_user)

    def test_add_person_first_name_and_phone_number(self):
        self.user = User("John", phone_number=123456789)
        self.library.add_person(self.user)
        actual_user = [self.user]
        expected_user = self.library.users
        self.assertEqual(expected_user, actual_user)

    def test_add_person_first_name_and_borrowed_book(self):
        self.user = User("John", borrowed_books="Toy Story 3")
        self.library.add_person(self.user)
        actual_user = [self.user]
        expected_user = self.library.users
        self.assertEqual(expected_user, actual_user)

    def test_add_person_with_all_values(self):
        self.user = User("John", "Carter", email="johncarter@gmial.com", phone_number=123456789,
                         borrowed_books="Toy Story 3")
        self.library.add_person(self.user)
        actual_user = [self.user]
        expected_user = self.library.users
        self.assertEqual(expected_user, actual_user)
