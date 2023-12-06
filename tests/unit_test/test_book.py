import unittest
from src.book import Book
from src.user import User
from src.library import Library
from datetime import datetime, timedelta


class TestBook(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book = Book("lord of the rings", "J.R.R", 987, "story about some rings")

    def test_book_present(self):
        book = Book(name="Biography of John", author="John Grimmes", short_description="John's life story",
                    pages=264)

        expected_output = "Book entitled Biography of John written by: John Grimmes, with a short review John's life story and 264 pages."

        self.assertEqual(book.present(), expected_output)

    def test_empty_book_present(self):
        empty_book = Book(name="Best composer", author="Rok Nardin", pages=57)

        expected_solution = "Book entitled Best composer written by: Rok Nardin, with a short review  and 57 pages."

        self.assertEqual(empty_book.present(), expected_solution)

    def test_get_date(self):
        today = datetime.now()

        actual_date = self.book.get_date()
        expected_date = today.strftime("%d/%m/%Y/%H:%M")

        self.assertEqual(actual_date, expected_date)

    def test_get_deadline(self):
        today = datetime.now()
        self.user = User("John")
        self.library.add_user(self.user)
        self.library.add_book(self.book)
        self.library.book_rent(self.user, self.book)

        actual_rent_date = self.book.rent_date
        excepted_rent_date = datetime.now().strftime("%d/%m/%Y/%H:%M")
        actual_deadline = self.book.rent_deadline
        expected_deadline = (today + timedelta(days=14)).strftime("%d/%m/%Y/%H:%M")

        self.assertEqual(actual_rent_date, excepted_rent_date)
        self.assertEqual(actual_deadline, expected_deadline)

    def test_add_renter(self):
        user = User("John", "Carter", email="johncarter@gmial.com", phone_number="123456789")

        actual_date = self.book.get_date()
        actual_deadline = self.book.get_deadline()
        actual_output = self.book.add_renter_to_book(user)
        expected_output = f"John Carter day {actual_date} has rented book 'lord of the rings' with deadline {actual_deadline}"

        self.assertEqual(actual_output, expected_output)

    def test_random_id(self):
        self.assertEqual(len(str(self.book.id)), 36)

    def test_is_rented_no_rent_date(self):
        self.assertFalse(self.book.is_rented())

    def test_is_rented_past_deadline(self):
        self.book.rent_date = (datetime.now() - timedelta(days=15)).strftime("%d/%m/%Y/%H:%M")
        self.book.rent_deadline = (datetime.now() - timedelta(days=7)).strftime("%d/%m/%Y/%H:%M")
        self.assertFalse(self.book.is_rented())

    def test_is_rented_before_deadline(self):
        self.book.rent_date = (datetime.now() - timedelta(days=7)).strftime("%d/%m/%Y/%H:%M")
        self.book.rent_deadline = (datetime.now() + timedelta(days=7)).strftime("%d/%m/%Y/%H:%M")
        self.assertTrue(self.book.is_rented())
