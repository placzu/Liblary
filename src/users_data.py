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


def load_users(filename='users_data.json'):
    with open(filename, 'r') as f:
        users_data = json.load(f)

    users = [User(**user_data) for user_data in users_data if
             all(field in user_data for field in User.__init__.__code__.co_varnames[1:])]
    return users


def save_users(users, filename='users_data.json'):
    # Save users to a file
    users_data = [user.to_dict() for user in users]
    with open(filename, 'w') as f:
        json.dump(users_data, f)
