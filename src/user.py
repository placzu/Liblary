import phonenumbers
from email_validator import validate_email, EmailNotValidError


class User:

    def __init__(self, first_name: str, last_name: str = None, email: str = None, phone_number: str = None,
                 borrowed_books: str = None):
        self.first_name = first_name
        self.last_name = last_name if last_name is not None else ""
        self.email = email
        self.phone_number = phone_number
        self.borrowed_books = borrowed_books if borrowed_books is not None else {}

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @staticmethod
    def validate_email(email: str) -> str:
        try:
            email_info = validate_email(email, check_deliverability=False)
            return email_info.normalized
        except EmailNotValidError as e:
            return (f"Not correct e-mail: {str(e)}")

    @staticmethod
    def validate_phone_number(phone_number: str) -> str:
        try:
            parsed_number = phonenumbers.parse(phone_number, "PL")
            if phonenumbers.is_valid_number(parsed_number):
                return phone_number
            else:
                return (f"Incorrect phone number: {phone_number}")
        except phonenumbers.phonenumberutil.NumberParseException as e:
            return (f"Incorrect phone number: {str(e)}")
