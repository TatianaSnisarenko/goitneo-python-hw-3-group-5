import unittest
from models import AddressBook, Record, ValidationError
from datetime import datetime, timedelta


class TestAddressBook(unittest.TestCase):
    def setUp(self):
        self.book = AddressBook()

    def test_add_record_correct_flow(self):
        john_record = Record('John', '1234567890')
        self.book.add_record(john_record)
        self.assertEqual(len(self.book.data), 1)

    def test_add_record_when_record_is_present(self):
        john_record = Record('John', '1234567890')
        self.book.add_record(john_record)
        self.assertEqual(len(self.book.data), 1)
        with self.assertRaises(KeyError) as context:
            self.book.add_record(Record('John', '1234567830'))
        self.assertEqual(len(self.book.data), 1)

    def test_create_record_correct_flow(self):
        self.book.create_record('John', '1234567890')
        self.assertEqual(len(self.book.data), 1)

    def test_create_record_when_record_is_present(self):
        john_record = Record('John', '1234567890')
        self.book.add_record(john_record)
        self.assertEqual(len(self.book.data), 1)
        with self.assertRaises(KeyError) as context:
            self.book.create_record('John', '1234567890')
        self.assertEqual(len(self.book.data), 1)

    def test_change_record_phone_correct_flow(self):
        self.book.create_record('John', '1234567890')
        self.book.change_record_phone('John', '5461237890')
        self.assertEqual(len(self.book.data), 1)
        self.assertEqual(self.book.show_record_phone('John'), '5461237890')

    def test_change_record_phone_when_record_is_apsent(self):
        with self.assertRaises(KeyError) as context:
            self.book.change_record_phone('John', '5461237890')

    def test_change_record_phone_when_validation_error(self):
        self.book.create_record('John', '1234567890')
        with self.assertRaises(ValidationError) as context:
            self.book.change_record_phone('John', '546123789')

    def test_add_record_birthday_correct_flow(self):
        self.book.create_record('John', '1234567890')
        self.book.add_record_birthday('John', '25.04.1990')
        self.assertEqual(len(self.book.data), 1)
        self.assertEqual(self.book.show_record_birthday('John'), '25.04.1990')

    def test_add_record_birthday_when_record_is_apsent(self):
        with self.assertRaises(KeyError) as context:
            self.book.add_record_birthday('John', '25.04.1990')

    def test_add_record_birthday_when_validation_error(self):
        self.book.create_record('John', '1234567890')
        with self.assertRaises(ValidationError) as context:
            self.book.change_record_phone('John', '25/04/1990')

    def test_show_record_phone_correct_flow(self):
        self.book.create_record('John', '1234567890')
        result = self.book.show_record_phone('John')
        self.assertEqual(result, '1234567890')

    def test_show_record_phone_when_record_is_apsent(self):
        with self.assertRaises(KeyError) as context:
            self.book.show_record_phone('John')

    def test_show_record_birthday_correct_flow(self):
        self.book.create_record('John', '1234567890')
        self.book.add_record_birthday('John', '25.04.1990')
        result = self.book.show_record_birthday('John')
        self.assertEqual(result, '25.04.1990')

    def test_show_record_birthday_when_record_is_apsent(self):
        with self.assertRaises(KeyError) as context:
            self.book.show_record_birthday('John')

    def test_show_record_birthday_is_apsent(self):
        self.book.create_record('John', '1234567890')
        result = self.book.show_record_birthday('John')
        self.assertEqual(result, 'Birthday is not added for John')

    def test_delete(self):
        john_record = Record('John', '1234567890')
        self.book.add_record(john_record)
        self.book.delete('John')
        self.assertEqual(len(self.book.data), 0)

    def test_delete_when_record_is_apsent(self):
        john_record = Record('John', '1234567890')
        self.book.add_record(john_record)
        self.assertEqual(len(self.book.data), 1)
        self.book.delete('Jane')
        self.assertEqual(len(self.book.data), 1)

    def test_get_record_contacts_correct_flow(self):
        self.book.create_record('John', '1234567890')
        self.book.create_record('Cher', '6541239870')
        result = self.book.get_record_contacts()
        self.assertEqual(result, ['John: 1234567890', 'Cher: 6541239870'])

    def test_get_record_contacts_when_no_records(self):
        result = self.book.get_record_contacts()
        self.assertEqual(result, [])

    def test_get_record_birthdays_per_week_correct_flow(self):
        today = datetime.today().strftime('%d.%m.%Y')
        tomorrow = (datetime.today() + timedelta(days=1)).strftime('%d.%m.%Y')
        self.book.create_record('John', '1236547890')
        self.book.add_record_birthday('John', today)
        self.book.create_record('Cher', '5689741230')
        self.book.add_record_birthday('Cher', tomorrow)
        result = self.book.get_record_birthdays_per_week()
        result_str = ", ".join(result)
        self.assertTrue('John' in result_str)
        self.assertTrue('Cher' in result_str)

    def test_get_record_contacts_when_no_records(self):
        result = self.book.get_record_contacts()
        self.assertEqual(result, [])

    def test_get_record_birthdays_per_week_when_no_records(self):
        result = self.book.get_record_birthdays_per_week()
        self.assertEqual(result, ())

    def test_get_record_birthdays_per_week_when_no_birthdays_for_next_week(self):
        date_out_of_range = (datetime.today() +
                             timedelta(days=8)).strftime('%d.%m.%Y')
        self.book.create_record('John', '1236547890')
        self.book.add_record_birthday('John', date_out_of_range)
        result = self.book.get_record_birthdays_per_week()
        self.assertEqual(result, ())


if __name__ == '__main__':
    unittest.main()
