from collections import UserDict
from datetime import datetime
from error_handling import invalid_phone_number_error_message, invalid_birthday_format_error_message
from errors import ValidationError
from user_birthdays import get_birthdays_per_week
import re


class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, Field):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)


class Name(Field):
    def __init__(self, name: str):
        super().__init__(name)

    def __eq__(self, other):
        if isinstance(other, Name):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)


class Phone(Field):
    def __init__(self, phone_number: str):
        super().__init__(self.clear_phone_number(phone_number))

    def __eq__(self, other):
        if isinstance(other, Phone):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)

    @staticmethod
    def clear_phone_number(phone_number: str) -> str:
        cleared_phone_number = phone_number.strip()
        if not phone_number.isdigit() or len(cleared_phone_number) != 10:
            raise ValidationError(invalid_phone_number_error_message)
        return cleared_phone_number


class Birthday(Field):
    def __init__(self, birthday: str):
        super().__init__(self.clear_birthday(birthday))

    def __eq__(self, other):
        if isinstance(other, Birthday):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)

    @property
    def birth_date(self):
        return datetime.strptime(self.value, '%d.%m.%Y') if self.value else None

    @staticmethod
    def clear_birthday(birthday: str) -> str:
        cleared_birthday = birthday.strip()
        pattern = re.compile(r'^\d{2}\.\d{2}\.\d{4}$')
        if not bool(pattern.match(cleared_birthday)):
            raise ValidationError(invalid_birthday_format_error_message)
        try:
            date_object = datetime.strptime(cleared_birthday, '%d.%m.%Y')
            return cleared_birthday
        except ValueError:
            raise ValidationError(invalid_birthday_format_error_message)


class Record:
    def __init__(self, name: str, phone: str) -> None:
        self.name = Name(name)
        self.phone = Phone(phone)
        self.birthday = None

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)

    def edit_phone(self, phone) -> None:
        self.phone = Phone(phone)

    def __eq__(self, other):
        if isinstance(other, Record):
            return self.name == other.name and self.phone == other.phone and self.birthday == other.birthday
        return False

    def __hash__(self):
        return hash(self.name, self.phone, self.birthday)

    def __str__(self):
        birthday_str = f', birthday: {
            self.birthday.value}' if self.birthday else ''
        return f'Contact name: {self.name.value}, phone: {self.phone.value}' + birthday_str


class AddressBook(UserDict):

    def create_record(self, name: str, phone: str) -> None:
        record = Record(name, phone)
        self.add_record(record)

    def add_record(self, record: Record) -> None:
        if self.data.get(record.name) != None:
            raise KeyError
        self.data[record.name] = record

    def change_record_phone(self, name: str, phone: str) -> None:
        existing_record = self.data[Name(name)]
        existing_record.edit_phone(phone)

    def add_record_birthday(self, name: str, birthday: str) -> None:
        existing_record = self.data[Name(name)]
        existing_record.add_birthday(birthday)

    def show_record_phone(self, name: str) -> str:
        existing_record = self.data[Name(name)]
        return str(existing_record.phone)

    def show_record_birthday(self, name: str) -> str:
        existing_record = self.data[Name(name)]
        return str(existing_record.birthday) if existing_record.birthday else f'Birthday is not added for {name}'

    def delete(self, name: str) -> None:
        self.data.pop(Name(name), None)

    def get_record_birthdays_per_week(self) -> list:
        contact_birthdays = [{'name': str(name), 'birthday': record.birthday.birth_date}
                             for name, record in self.data.items() if record.birthday is not None]
        return get_birthdays_per_week(contact_birthdays)

    def get_record_contacts(self) -> list:
        return [': '.join((str(name), str(record.phone))) for name, record in self.data.items()]
