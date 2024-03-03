from datetime import datetime, timedelta
from collections import defaultdict
from calendar import isleap


def get_birthdays_per_week(users):
    if not users:
        return tuple()
    return get_birthdays_per_week_from_date(users, datetime.today())


def get_birthdays_per_week_from_date(users, from_date):
    date = from_date.date()
    date_day_of_week = date.weekday()

    # Calculate the date of the next Monday
    days_until_monday = (0 - date.weekday()) % 7
    closest_monday = date + timedelta(days=days_until_monday)

    result = defaultdict(list)

    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        birthday_this_year = get_date(date.year, birthday.month, birthday.day)
        delta_days = (birthday_this_year - date).days

        # handle negative delta for weekends
        # include past saturday's birthday for Monday
        is_today_sunday = date_day_of_week == 6 and delta_days == -1
        # include past weekends birthdays for Monday
        is_today_monday = date_day_of_week == 0 and delta_days in [-1, -2]
        if is_today_sunday or is_today_monday:
            result[closest_monday].append(name)

        # if birthday less than today, consider next year's birthday.
        if delta_days < 0:
            birthday_this_year = get_date(
                date.year+1, birthday.month, birthday.day)

        # re-establish delta
        delta_days = (birthday_this_year - date).days
        birthday_week_day = birthday_this_year.weekday()

        # check delta should be within a week from today
        if delta_days < 7:
            # exclude next weekends
            if birthday_week_day in [5, 6]:
                if (delta_days >= birthday_week_day):
                    continue
                else:
                    result[closest_monday].append(name)
            # add all birthdays to its weekdays
            else:
                result[birthday_this_year].append(name)
    ordered_dict = dict(sorted(result.items()))
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    formatted_list = []
    for key, value in ordered_dict.items():
        formatted_list.append(
            f'{days_of_week[key.weekday()]}: {', '.join(value)}')
    return tuple(formatted_list)


def show_birthdays_per_week_from_date(users_birthdays):
    for value in users_birthdays:
        print(value)


def get_date(year, month, day):
    if not isleap(year) and month == 2 and day == 29:
        month = 3
        day = 1
    return datetime(year, month, day).date()
