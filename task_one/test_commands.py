import unittest
from datetime import datetime, timedelta
from commands import (
    add_contact,
    add_contact_error_messages,
    change_contact,
    change_contact_error_messages,
    show_phone,
    show_phone_error_messages,
    show_all,
    show_all_error_messages,
    parse_input,
    parse_input_error_messages,
    add_birthday,
    add_birthday_error_messages,
    show_birthday,
    show_birthday_error_messages,
    show_all_birthdays,
    show_all_birthdays_error_messages

)
from models import AddressBook


class TestContactFunctions(unittest.TestCase):
    def setUp(self):
        self.book = AddressBook()

    def test_parse_input_correct_flow(self):
        result = parse_input('add')
        self.assertEqual(result, ('add',))

    def test_parse_input_value_error(self):
        result = parse_input('')
        self.assertEqual(
            result, parse_input_error_messages.get('FormatError'))

    def test_add_contact_correct_flow(self):
        result = add_contact(['John', '1234567890'], self.book)
        self.assertEqual(result, 'Contact added.')
        self.assertEqual(self.book.show_record_phone('John'), '1234567890')

    def test_add_contact_index_error(self):
        result = add_contact(['John'], self.book)
        self.assertEqual(
            result, add_contact_error_messages.get('FormatError'))

    def test_add_contact_value_error(self):
        result = add_contact(['John', '123456789', 'skdfjl'], self.book)
        self.assertEqual(
            result, add_contact_error_messages.get('FormatError'))

    def test_add_contact_validation_error(self):
        result = add_contact(['John', '123456789'], self.book)
        self.assertEqual(
            result, add_contact_error_messages.get('ValidationError'))

    def test_add_contact_name_already_present(self):
        self.book.create_record('John', '9876543210')
        result = add_contact(['John', '1234567890'], self.book)
        self.assertEqual(
            result, add_contact_error_messages.get('KeyError'))

    def test_change_contact_correct_flow(self):
        self.book.create_record('Cher', '9876543210')
        result = change_contact(['Cher', '3334444555'], self.book)
        self.assertEqual(result, 'Contact updated.')
        self.assertEqual(self.book.show_record_phone('Cher'), '3334444555')

    def test_change_contact_index_error(self):
        result = change_contact(['Cher'], self.book)
        self.assertEqual(
            result, change_contact_error_messages.get('FormatError'))

    def test_change_contact_value_error(self):
        result = change_contact(['Cher', '123456789', 'skdfjl'], self.book)
        self.assertEqual(
            result, change_contact_error_messages.get('FormatError'))

    def test_change_contact_name_is_apsent(self):
        result = change_contact(['Kyle', '1234567890'], self.book)
        self.assertEqual(
            result, change_contact_error_messages.get('KeyError'))

    def test_change_contact_validation_error(self):
        self.book.create_record('Cher', '9876543210')
        result = change_contact(['Cher', '123456789'], self.book)
        self.assertEqual(
            result, change_contact_error_messages.get('ValidationError'))

    def test_show_phone_correct_flow(self):
        self.book.create_record('John', '1234567890')
        result = show_phone(['John'], self.book)
        self.assertEqual(result, '1234567890')

    def test_show_phone_index_error(self):
        result = show_phone([], self.book)
        self.assertEqual(
            result, show_phone_error_messages.get('FormatError'))

    def test_show_phone_value_error(self):
        result = show_phone(['John', 'skdfl'], self.book)
        self.assertEqual(
            result, show_phone_error_messages.get('FormatError'))

    def test_show_phone_name_not_found(self):
        result = show_phone(['Kuki'], self.book)
        self.assertEqual(result, show_phone_error_messages.get('KeyError'))

    def test_show_all_correct_flow(self):
        self.book.create_record('John', '1234567890')
        self.book.create_record('Cher', '1122334450')
        result = show_all(self.book)
        self.assertEqual(result, 'John: 1234567890\nCher: 1122334450')

    def test_show_all_value_error(self):
        result = show_all(self.book)
        self.assertEqual(
            result, show_all_error_messages.get('FormatError'))

    def test_add_birthday_correct_flow(self):
        self.book.create_record('John', '9874563210')
        result = add_birthday(['John', '05.03.1990'], self.book)
        self.assertEqual(result, 'Birthday added.')
        self.assertEqual(self.book.show_record_birthday('John'), '05.03.1990')

    def test_add_birthday_index_error(self):
        result = add_birthday(['John'], self.book)
        self.assertEqual(
            result, add_birthday_error_messages.get('FormatError'))

    def test_add_birthday_value_error(self):
        result = add_birthday(['John', '05.03.1990', 'skdfjl'], self.book)
        self.assertEqual(
            result, add_birthday_error_messages.get('FormatError'))

    def test_add_birthday_validation_error(self):
        self.book.create_record('John', '9874563210')
        result = add_birthday(['John', '05.23.1990'], self.book)
        self.assertEqual(
            result, add_birthday_error_messages.get('ValidationError'))

    def test_add_birthday_when_record_is_apsent(self):
        result = add_birthday(['John', '05.23.1990'], self.book)
        self.assertEqual(
            result, add_birthday_error_messages.get('KeyError'))

    def test_show_birthday_correct_flow(self):
        self.book.create_record('John', '1234567890')
        self.book.add_record_birthday('John', '05.03.1990')
        result = show_birthday(['John'], self.book)
        self.assertEqual(result, '05.03.1990')

    def test_show_birthday_index_error(self):
        result = show_birthday([], self.book)
        self.assertEqual(
            result, show_birthday_error_messages.get('FormatError'))

    def test_show_birthday_value_error(self):
        result = show_birthday(['John', 'skdfl'], self.book)
        self.assertEqual(
            result, show_birthday_error_messages.get('FormatError'))

    def test_show_birthday_name_not_found(self):
        result = show_birthday(['Kuki'], self.book)
        self.assertEqual(result, show_birthday_error_messages.get('KeyError'))

    def test_show_all_birthdays_correct_flow(self):
        today = datetime.today().strftime('%d.%m.%Y')
        tomorrow = (datetime.today() + timedelta(days=1)).strftime('%d.%m.%Y')
        self.book.create_record('John', '1236547890')
        self.book.add_record_birthday('John', today)
        self.book.create_record('Cher', '5689741230')
        self.book.add_record_birthday('Cher', tomorrow)
        result = show_all_birthdays(self.book)
        self.assertTrue('John' in result)
        self.assertTrue('Cher' in result)

    def test_show_all_birthdays_value_error(self):
        result = show_all_birthdays(self.book)
        self.assertEqual(
            result, show_all_birthdays_error_messages.get('FormatError'))

    def test_show_all_birthdays_when_no_birthdays_for_next_week(self):
        date_out_of_range = (datetime.today() +
                             timedelta(days=8)).strftime('%d.%m.%Y')
        self.book.create_record('John', '1236547890')
        self.book.add_record_birthday('John', date_out_of_range)
        result = show_all_birthdays(self.book)
        self.assertEqual(
            result, 'No birthdays for this week.')


if __name__ == '__main__':
    unittest.main()
