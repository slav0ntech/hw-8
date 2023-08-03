from datetime import datetime, timedelta


current_full = datetime.now()
current_year = datetime.now().year
current_month = datetime.now().month
current_weekday = datetime.now().weekday()
current_day = datetime.now().day

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
    current_date_zero_time = current_full.replace(
        hour=00, minute=00, second=00)  # set time 00-00-00
    if current_weekday != 0:
        start_point = current_date_zero_time - timedelta(days=current_weekday)
        return start_point
    return current_date_zero_time


def get_end_point(start_point: datetime) -> datetime:
    end_point = start_point + timedelta(weeks=2)
    return end_point


def get_users_convert_date(users_date: datetime) -> datetime:
    new_date = datetime.replace(users_date, year=current_year)
    return new_date


def get_weekday(name_user: str, year_birthday: datetime) -> dict:
    # print(year_birthday.weekday())
    if year_birthday.weekday() == 5:
        # if birthday in Saturday or Sunday , than add to Monday
        dict_result['Monday'].append(name_user)

    else:
        dict_result[dict_table_weekday[year_birthday.weekday()]].append(
            name_user)  # add to our dict: founded names and compared dates
    return dict_result


def convert_dict_to_str(dict_result: dict) -> str:
    # print(dict_result)
    full_result = ''

    for weekday, name in dict_result.items():
        if name:
            # print(f"{weekday}: {', '.join(name)}")
            full_result += f"{weekday}: {', '.join(name)} \n"

    # print(full_result)
    return full_result


def get_birthdays_per_week(users: list):
    start_point = get_start_point()         # get start date
    # print(f"Start point: {start_point}")   # print start point
    # call get_end_point() func and send start_point value
    end_point = get_end_point(start_point)
    # print(f"End point: {end_point}")       # print end point

    for user in users:
        user_year_modify = get_users_convert_date(user['birthday'])
        user['birthday'] = user_year_modify  # update year birthday

    delta = timedelta(days=1)

    while (start_point.date() <= end_point.date()):  # date iteration
        for i in users:
            if i['birthday'].date() == start_point.date():  # compare dates
                # print(i['name'], i['birthday'])
                get_weekday(i['name'], i['birthday'])

        start_point += delta
    # print(dict_result)

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