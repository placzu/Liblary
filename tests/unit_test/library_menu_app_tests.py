import unittest
import sys
import os
import json

sys.path.insert(0, 'D:\\liblary\\src\\')

from users_data import User, load_users, save_users


class TestUserClass(unittest.TestCase):

    def setUp(self):
        self.sample_user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "123456789",
            "address": "123 Main St, City",
            "email": "john.doe@example.com",
            "status": "User"
        }

    def test_user_creation(self):
        user = User(**self.sample_user_data)

        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.phone_number, "123456789")
        self.assertEqual(user.address, "123 Main St, City")
        self.assertEqual(user.email, "john.doe@example.com")
        self.assertEqual(user.status, "User")

    def test_user_str_method(self):
        user = User(**self.sample_user_data)

        self.assertEqual(str(user), "John Doe")

    def test_user_to_dict_method(self):
        user = User(**self.sample_user_data)

        user_dict = user.to_dict()

        self.assertEqual(user_dict, self.sample_user_data)

    def test_user_with_empty_values(self):
        empty_user_data = {
            "first_name": "",
            "last_name": "",
            "phone_number": "",
            "address": "",
            "email": "",
            "status": ""
        }
        empty_user = User(**empty_user_data)

        self.assertEqual(empty_user.first_name, "")
        self.assertEqual(empty_user.last_name, "")

    def test_valid_user_status(self):
        valid_status_data = {
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "123456789",
            "address": "123 Main St, City",
            "email": "john.doe@example.com",
            "status": "Admin"
        }
        valid_status_user = User(**valid_status_data)

        self.assertEqual(valid_status_user.status, "Admin")

    def test_load_users(self):
        # Test loading users from a file
        self.users_data = [
            {"first_name": "Alice", "last_name": "Smith", "phone_number": "123456789", "address": "Test Address 1",
             "email": "alice@example.com", "status": "User"},
            {"first_name": "Bob", "last_name": "Johnson", "phone_number": "987654321", "address": "Test Address 2",
             "email": "bob@example.com", "status": "Admin"}
        ]
        with open('test_users_data.json', 'w') as f:
            json.dump(self.users_data, f)

        with open('test_users_data.json', 'r') as f:
            data = json.load(f)
            print(f"Data written to the file: {data}")

        loaded_users = load_users('test_users_data.json')
        self.assertEqual(len(loaded_users), 2)
        self.assertEqual(loaded_users[0].first_name, "Alice")
        self.assertEqual(loaded_users[1].status, "Admin")

    def test_save_users(self):
        users = [
            User("Alice", "Smith", "123456789", "123 Main St", "alice@example.com", "User"),
            User("Bob", "Johnson", "987654321", "456 Oak St", "bob@example.com", "Admin")
        ]
        save_users(users, 'test_saved_users_data.json')

        with open('test_saved_users_data.json', 'r') as f:
            saved_data = json.load(f)

        self.assertEqual(len(saved_data), 2)
        self.assertEqual(saved_data[0]["phone_number"], "123456789")
        self.assertEqual(saved_data[1]["address"], "456 Oak St")

    def tearDown(self):
        files_to_remove = ['test_users_data.json', 'test_saved_users_data.json']
        for file_path in files_to_remove:
            try:
                os.remove(file_path)
            except FileNotFoundError:
                pass


if __name__ == '__main__':
    unittest.main()
