import json

class User:
    def __init__(self, first_name, last_name, phone_number, address, email, status):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.status = status

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def to_dict(self):
        return self.__dict__


def load_users():
    try:
        with open('users_data.json', 'r') as f:
            users_dict = json.load(f)
            return [User(**user) for user in users_dict]
    except (FileNotFoundError, EOFError):
        return []


def save_users(users):
    with open('users_data.json', 'w') as f:
        users_dict = [user.to_dict() for user in users]
        json.dump(users_dict, f)
