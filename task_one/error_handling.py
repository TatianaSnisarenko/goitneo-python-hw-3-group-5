from errors import ValidationError

generic_error_message = 'Something went wrong, please try again.'
invalid_phone_number_error_message = 'Invalid phone number: must be 10 digits value.'
invalid_birthday_format_error_message = 'Invalid birthday format: must be <DD.MM.YYYY>.'

generic_invalid_command_format_message = '''Invalid "command" format. Available commands: 
    - <add Name phone_namber> - to add contact, 
    - <change Name new_phone_number> - to update contact,
    - <phone Name> - to show phone for the contact
    - <all> - to show all contacts,
    - <hello> - to show assistance message,
    - <add-birthday Name DD.MM.YYYY> - to add birthday for contact,
    - <show-birthday Name> - to show birthday for the contact,
    - <birthdays> - to show all birthdays per working week
    - <exit> - to exit the bot
    - <close> - to close the bot'''

add_birthday_error_messages = {
    'FormatError': 'Invalid "add-birthday" format. Command "add-birthday" must have 3 arguments: <add-birthday Name DD.MM.YYYY>.',
    'KeyError': 'Such name is not found, please, use "add" command to add new contact first.',
    'ValidationError': invalid_birthday_format_error_message
}

add_contact_error_messages = {
    'FormatError': 'Invalid "add" format. Command "add" must have 3 arguments: <add Name phone_number>.',
    'KeyError': 'Such name is already present, please, use "change" command instead.',
    'ValidationError': invalid_phone_number_error_message
}

change_contact_error_messages = {
    'FormatError': 'Invalid "change" format. Command "change" must have 3 arguments: <change Name new_phone_number>.',
    'KeyError': 'Such name is not found, please, use "add" command instead.',
    'ValidationError': invalid_phone_number_error_message
}

show_phone_error_messages = {
    'FormatError': 'Invalid "phone" format. Command "phone" must have 2 arguments: <phone Name>.',
    'KeyError': 'Such name is not found, please, try again.'
}

show_birthday_error_messages = {
    'FormatError': 'Invalid "show-birthday" format. Command "show-birthday" must have 2 arguments: <show-birthday Name>.',
    'KeyError': 'Such name is not found, please, try again.'
}

show_all_error_messages = {
    'FormatError': 'Contacts are empty. Please, use "add" command to add new contacts.',
}

show_all_birthdays_error_messages = {
    'FormatError': 'Contacts are empty. Please, use "add" command to add new contacts first.'
}

parse_input_error_messages = {
    'FormatError': generic_invalid_command_format_message,
}


def input_error(error_messages):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (IndexError, ValueError):
                return error_messages.get('FormatError') if 'FormatError' in error_messages else generic_error_message
            except KeyError:
                return error_messages.get('KeyError') if 'KeyError' in error_messages else generic_error_message
            except ValidationError:
                return error_messages.get('ValidationError') if 'ValidationError' in error_messages else generic_error_message
            except Exception as e:
                return generic_error_message
        return inner
    return decorator
