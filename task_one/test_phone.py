import unittest
from models import Phone, ValidationError
from error_handling import invalid_phone_number_error_message


class TestPhone(unittest.TestCase):

    def test_phone(self):
        phone = Phone('1234567890')
        self.assertEqual(type(phone), Phone)
        self.assertEqual(phone.value, '1234567890')
        self.assertEqual(phone, Phone('1234567890'))
        self.assertEqual(str(phone), '1234567890')

    def test_invalid_phone_characters(self):
        with self.assertRaises(ValidationError) as context:
            phone = Phone('12345y7890')
        self.assertEqual(str(context.exception),
                         invalid_phone_number_error_message)

    def test_invalid_phone_length(self):
        with self.assertRaises(ValidationError) as context:
            phone = Phone('123457890')
        self.assertEqual(str(context.exception),
                         invalid_phone_number_error_message)


if __name__ == '__main__':
    unittest.main()
