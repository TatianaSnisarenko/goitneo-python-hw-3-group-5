import unittest
from models import *


class TestRecord(unittest.TestCase):

    def test_record_correct_flow(self):
        john_record = Record('John', '1234567890')
        self.assertEqual(type(john_record), Record)
        self.assertEqual(john_record.name, Name('John'))
        self.assertEqual(john_record, Record('John', '1234567890'))
        self.assertEqual(john_record.phone, Phone('1234567890'))
        self.assertIsNone(john_record.birthday)

    def test_add_birthday_correct_flow(self):
        john_record = Record('John', '1234567890')
        john_record.add_birthday('23.03.1990')
        self.assertEqual(john_record.birthday, Birthday('23.03.1990'))

    def test_add_birthday_when_birthday_is_set(self):
        john_record = Record('John', '1234567890')
        john_record.add_birthday('23.03.1990')
        self.assertEqual(john_record.birthday, Birthday('23.03.1990'))
        john_record.add_birthday('23.03.1991')
        self.assertEqual(john_record.birthday, Birthday('23.03.1991'))

    def test_add_birthday_when_validation_error(self):
        john_record = Record('John', '1234567890')
        with self.assertRaises(ValidationError) as context:
            john_record.add_birthday('23-03-1990')

    def test_edit_phone_correct_flow(self):
        john_record = Record('John', '1234567890')
        john_record.edit_phone('1234567890')
        self.assertEqual(john_record.phone, Phone('1234567890'))
        john_record.edit_phone('2222267890')
        self.assertEqual(john_record.phone, Phone('2222267890'))

    def test_edit_phone_when_validation_error(self):
        john_record = Record('John', '1234567890')
        with self.assertRaises(ValidationError) as context:
            john_record.edit_phone('234567890')

    def test_str(self):
        john_record = Record('John', '1234567890')
        expected_str = 'Contact name: John, phone: 1234567890'
        self.assertEqual(str(john_record), expected_str)
        john_record.add_birthday('23.05.1990')
        expected_str = 'Contact name: John, phone: 1234567890, birthday: 23.05.1990'
        self.assertEqual(str(john_record), expected_str)


if __name__ == '__main__':
    unittest.main()
