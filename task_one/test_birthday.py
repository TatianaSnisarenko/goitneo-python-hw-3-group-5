import unittest
from models import Birthday, ValidationError
from error_handling import invalid_birthday_format_error_message


class TestBirthday(unittest.TestCase):

    def test_birthday(self):
        birthday = Birthday('03.04.1990')
        self.assertEqual(type(birthday), Birthday)
        self.assertEqual(birthday.value, '03.04.1990')
        self.assertEqual(birthday, Birthday('03.04.1990'))
        self.assertEqual(str(birthday), '03.04.1990')

    def test_invalid_format_birthday(self):
        with self.assertRaises(ValidationError) as context:
            phone = Birthday('03-04-1990')
        self.assertEqual(str(context.exception),
                         invalid_birthday_format_error_message)
        with self.assertRaises(ValidationError) as context:
            phone = Birthday('3.03.1990')
        self.assertEqual(str(context.exception),
                         invalid_birthday_format_error_message)
        with self.assertRaises(ValidationError) as context:
            phone = Birthday('23.03.90')
        self.assertEqual(str(context.exception),
                         invalid_birthday_format_error_message)
        with self.assertRaises(ValidationError) as context:
            phone = Birthday('03.3.1990')
        self.assertEqual(str(context.exception),
                         invalid_birthday_format_error_message)

    def test_invalid_date_birthday(self):
        with self.assertRaises(ValidationError) as context:
            phone = Birthday('03.24.1990')
        self.assertEqual(str(context.exception),
                         invalid_birthday_format_error_message)


if __name__ == '__main__':
    unittest.main()
