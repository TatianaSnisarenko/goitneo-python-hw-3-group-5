import unittest
from datetime import datetime, timedelta
from user_birthdays import get_birthdays_per_week_from_date, get_birthdays_per_week
from calendar import isleap


class TestUserBirthdayFunctions(unittest.TestCase):

    def setUp(self):
        self.users = [
            {"name": "Last Wed", "birthday": datetime(1955, 2, 7)},
            {"name": "Last Thur", "birthday": datetime(1955, 2, 8)},
            {"name": "List Fri", "birthday": datetime(1955, 2, 9)},
            {"name": "Last Saturday", "birthday": datetime(1955, 2, 10)},
            {"name": "Last Sunday", "birthday": datetime(1955, 2, 11)},
            {"name": "Bill Mon", "birthday": datetime(1955, 2, 12)},
            {"name": "Bill Tue", "birthday": datetime(1955, 2, 13)},
            {"name": "Bill Wed", "birthday": datetime(1955, 2, 14)},
            {"name": "Bill Thur", "birthday": datetime(1955, 2, 15)},
            {"name": "Bill Fri", "birthday": datetime(1955, 2, 16)},
            {"name": "Next Saturday", "birthday": datetime(1955, 2, 17)},
            {"name": "Next Sunday", "birthday": datetime(1955, 2, 18)},
            {"name": "Next Monday", "birthday": datetime(1955, 2, 19)},
            {"name": "Next Tuesday", "birthday": datetime(1955, 2, 20)},
            {"name": "Next Wednesday", "birthday": datetime(1955, 2, 21)},
            {"name": "Next Thursday", "birthday": datetime(1955, 2, 22)},
            {"name": "Next Friday", "birthday": datetime(1955, 2, 23)},
            {"name": "Future Saturday", "birthday": datetime(1955, 2, 24)},
            {"name": "Future Sunday", "birthday": datetime(1955, 2, 25)},
            {"name": "Future Monday", "birthday": datetime(1955, 2, 26)},
            {"name": "Future Tuesday", "birthday": datetime(1955, 2, 27)},
            {"name": "Future Wednesday", "birthday": datetime(1955, 2, 28)},
            {"name": "Future Thursday", "birthday": datetime(1992, 2, 29)},
            {"name": "Future Friday", "birthday": datetime(1955, 3, 1)},
            {"name": "Future Saturday", "birthday": datetime(1955, 3, 2)},
            {"name": "Future Sunday", "birthday": datetime(1955, 3, 3)}
        ]

        self.users_next_year = [
            {"name": "First Jan", "birthday": datetime(1955, 1, 1)},
            {"name": "Third Jan", "birthday": datetime(1955, 1, 1)},
            {"name": "Third Feb", "birthday": datetime(1955, 2, 1)},
        ]

    def get_date(self, year, month, day):
        if not isleap(year) and month == 2 and day == 29:
            month = 3
            day = 1
        return datetime(year, month, day)

    def test_last_saturday(self):
        expected = ('Monday: Last Saturday, Last Sunday, Bill Mon',
                    'Tuesday: Bill Tue', 'Wednesday: Bill Wed',
                    'Thursday: Bill Thur', 'Friday: Bill Fri')
        result = get_birthdays_per_week_from_date(
            self.users, datetime(2024, 2, 10))
        self.assertEqual(result, expected)

    def test_last_sunday(self):
        expected = ('Monday: Last Saturday, Last Sunday, Bill Mon',
                    'Tuesday: Bill Tue', 'Wednesday: Bill Wed',
                    'Thursday: Bill Thur', 'Friday: Bill Fri')
        result = get_birthdays_per_week_from_date(
            self.users, datetime(2024, 2, 11))
        self.assertEqual(result, expected)

    def test_monday(self):
        expected = ('Monday: Last Saturday, Last Sunday, Bill Mon',
                    'Tuesday: Bill Tue', 'Wednesday: Bill Wed',
                    'Thursday: Bill Thur', 'Friday: Bill Fri')
        result = get_birthdays_per_week_from_date(
            self.users, datetime(2024, 2, 12))
        self.assertEqual(result, expected)

    def test_tuesday(self):
        expected = ('Tuesday: Bill Tue', 'Wednesday: Bill Wed',
                    'Thursday: Bill Thur', 'Friday: Bill Fri',
                    'Monday: Next Saturday, Next Sunday, Next Monday')
        result = get_birthdays_per_week_from_date(
            self.users, datetime(2024, 2, 13))
        self.assertEqual(result, expected)

    def test_wednesday(self):
        expected = ('Wednesday: Bill Wed', 'Thursday: Bill Thur',
                    'Friday: Bill Fri',
                    'Monday: Next Saturday, Next Sunday, Next Monday',
                    'Tuesday: Next Tuesday')
        result = get_birthdays_per_week_from_date(
            self.users, datetime(2024, 2, 14))
        self.assertEqual(result, expected)

    def test_thursday(self):
        expected = ('Thursday: Bill Thur',
                    'Friday: Bill Fri',
                    'Monday: Next Saturday, Next Sunday, Next Monday',
                    'Tuesday: Next Tuesday', 'Wednesday: Next Wednesday')
        result = get_birthdays_per_week_from_date(
            self.users, datetime(2024, 2, 15))
        self.assertEqual(result, expected)

    def test_friday(self):
        expected = ('Friday: Bill Fri',
                    'Monday: Next Saturday, Next Sunday, Next Monday',
                    'Tuesday: Next Tuesday', 'Wednesday: Next Wednesday',
                    'Thursday: Next Thursday')
        result = get_birthdays_per_week_from_date(
            self.users, datetime(2024, 2, 16))
        self.assertEqual(result, expected)

    def test_next_saturday(self):
        expected = ('Monday: Next Saturday, Next Sunday, Next Monday',
                    'Tuesday: Next Tuesday', 'Wednesday: Next Wednesday',
                    'Thursday: Next Thursday', 'Friday: Next Friday')
        result = get_birthdays_per_week_from_date(
            self.users, datetime(2024, 2, 17))
        self.assertEqual(result, expected)

    def test_next_sunday(self):
        expected = ('Monday: Next Saturday, Next Sunday, Next Monday',
                    'Tuesday: Next Tuesday', 'Wednesday: Next Wednesday',
                    'Thursday: Next Thursday', 'Friday: Next Friday')
        result = get_birthdays_per_week_from_date(
            self.users, datetime(2024, 2, 18))
        self.assertEqual(result, expected)

    def test_next_monday(self):
        expected = ('Monday: Next Saturday, Next Sunday, Next Monday',
                    'Tuesday: Next Tuesday', 'Wednesday: Next Wednesday',
                    'Thursday: Next Thursday', 'Friday: Next Friday')
        result = get_birthdays_per_week_from_date(
            self.users, datetime(2024, 2, 19))
        self.assertEqual(result, expected)

    def test_future_saturday(self):
        expected = ('Monday: Future Saturday, Future Sunday, Future Monday',
                    'Tuesday: Future Tuesday', 'Wednesday: Future Wednesday',
                    'Thursday: Future Thursday', 'Friday: Future Friday')
        result = get_birthdays_per_week_from_date(
            self.users, datetime(2024, 2, 24))
        self.assertEqual(result, expected)

    def test_not_leap_year(self):
        # The date is Monday with name Future Saturday for 2025 not leap year
        expected = ('Monday: Next Thursday, Next Friday, Future Saturday',
                    'Tuesday: Future Sunday', 'Wednesday: Future Monday',
                    'Thursday: Future Tuesday', 'Friday: Future Wednesday')
        result = get_birthdays_per_week_from_date(
            self.users, datetime(2025, 2, 24))
        self.assertEqual(result, expected)

    def test_next_year(self):
        # Today is 30th of december should include January and not February for next year
        expected = ('Monday: First Jan, Third Jan',)
        result = get_birthdays_per_week_from_date(
            self.users_next_year, datetime(2023, 12, 30))
        self.assertEqual(result, expected)

    def test_get_birthdays_per_week(self):
        today = datetime.today()
        users = [{'name': 'Name Today', 'birthday': self.get_date(
            1992, today.month, today.day)}]
        for i in range(1, 10):
            name = "Name Minus_" + str(i)
            date = today - timedelta(days=i)
            birthday = self.get_date(1992, date.month, date.day)
            users.append({'name': name, 'birthday': birthday})
            name = "Name Plus_" + str(i)
            date = today + timedelta(days=i)
            birthday = self.get_date(1992, date.month, date.day)
            users.append({'name': name, 'birthday': birthday})
        # Exected a list of 5 elements for each working day:
        # 3 names for Monday and 1 name for other working days
        result = get_birthdays_per_week(users)
        self.assertEqual(len(result), 5)

    def test_get_birthdays_per_week_when_users_are_empty(self):
        today = datetime.today()
        users = []
        result = get_birthdays_per_week(users)
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
