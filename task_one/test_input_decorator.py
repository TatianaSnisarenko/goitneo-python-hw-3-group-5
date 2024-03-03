import unittest
from error_handling import input_error, generic_error_message
from errors import ValidationError


class TestInputErrorDecorator(unittest.TestCase):
    def test_index_error_handling(self):
        @input_error({'FormatError': 'Invalid format', 'KeyError': 'Key not found'})
        def func_that_raises_index_error():
            raise IndexError()

        result = func_that_raises_index_error()
        self.assertEqual(result, 'Invalid format')

    def test_key_error_handling(self):
        @input_error({'FormatError': 'Invalid format', 'KeyError': 'Key not found'})
        def func_that_raises_key_error():
            raise KeyError()

        result = func_that_raises_key_error()
        self.assertEqual(result, 'Key not found')

    def test_validation_error_handling(self):
        @input_error({'ValidationError': 'Invalid format'})
        def func_that_raises_validation_error():
            raise ValidationError()

        result = func_that_raises_validation_error()
        self.assertEqual(result, 'Invalid format')

    def test_generic_error_handling(self):
        @input_error({'FormatError': 'Invalid format', 'KeyError': 'Key not found'})
        def func_that_raises_generic_error():
            raise ValidationError()

        result = func_that_raises_generic_error()
        self.assertEqual(result, generic_error_message)


if __name__ == '__main__':
    unittest.main()
