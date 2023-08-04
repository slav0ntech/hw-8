from datetime import datetime, timedelta

dict_result = {
    'Monday': [],
    'Tuesdayy': [],
    'Wednesday': [],
    'Thursday': [],
    'Friday': [],
    'Saturday': [],
    'Sunday': [],
}

dict_table_weekday = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}


def get_start_point() -> datetime:

    current_weekday = datetime.now().weekday()
    current_date = datetime.now()
    # current_date_zero_time= current_full.replace(hour=00, minute=00, second=00) #  set time 00-00-00
    if current_weekday != 0:
        current_date = current_date - timedelta(days=current_weekday)
        return current_date
    return current_date


def get_end_point(start_point: datetime) -> datetime:
    end_point = start_point + timedelta(weeks=2)
    return end_point


def get_weekday(name_user: str, year_birthday: datetime) -> dict:
    weekday = year_birthday.weekday()

    if weekday in [5, 6]:  # checking for day in weekdays. If that -> change to Monday and add to dict_result
        weekday = 0
        dict_result[dict_table_weekday[weekday]].append(name_user)
        return dict_result

    else:
        dict_result[dict_table_weekday[weekday]].append(name_user)
    return dict_result


def convert_dict_to_str(dict_result: dict) -> str:
    full_result = "\n".join(
        [f"{weekday}: {', '.join(name)}" for weekday, name in dict_result.items() if name])

    return full_result


def get_birthdays_per_week(users: list) -> str:
    start_point = get_start_point()         # get start date
    # print(f"Start point: {start_point}")   # print start point
    # call get_end_point() func and send start_point value
    end_point = get_end_point(start_point)
    # print(f"End point: {end_point}")       # print end point

    for user in users:
        current_year = datetime.now().year
        # new_date = datetime.replace(user['birthday'], year=current_year)

        user['birthday'] = datetime.replace(
            user['birthday'], year=current_year)  # update year birthday (change -> to current year)

        # print(user)

        if start_point.date() <= user['birthday'].date() <= end_point.date():
            get_weekday(user['name'], user['birthday'])

    print(convert_dict_to_str(dict_result))


users = [
    {'name': 'Dyadya Vanya',
     'birthday': datetime(year=1960, month=7, day=31)},

    {'name': 'Petro',
     'birthday': datetime(year=1987, month=8, day=5)},

    {'name': 'Vasyl',
     'birthday': datetime(year=1989, month=8, day=4)},

    {'name': 'Olga',
     'birthday': datetime(year=1982, month=8, day=9)},

    {'name': 'Maryna',
     'birthday': datetime(year=1992, month=2, day=2)},

    {'name': 'Olga Petrovna',
     'birthday': datetime(year=1956, month=12, day=22)},

    {'name': 'Timur',
     'birthday': datetime(year=2001, month=8, day=10)},
]

if __name__ == '__main__':
    get_birthdays_per_week(users)
