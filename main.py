from datetime import datetime, timedelta

current_full = datetime.now()
current_year = datetime.now().year
current_month = datetime.now().month
current_weekday = datetime.now().weekday()
current_day = datetime.now().day


def get_start_point() -> datetime:
    current_date_zero_time = current_full.replace(
        hour=00, minute=00, second=00)  # set time 00-00-00
    if current_weekday != 0:
        start_point = current_date_zero_time - timedelta(days=3)
        return start_point
    return current_date_zero_time


def get_end_point(start_point: datetime) -> datetime:
    end_point = start_point + timedelta(weeks=2)
    return end_point


def get_birthdays_per_week(users: list):
    start_point = get_start_point()
    print(f"Start point: {start_point}")
    # call get_end_point() func and send start_point value
    end_point = get_end_point(start_point)
    print(f"End point: {end_point}")


users = [
    {'name': 'Petro',
     'birthday': datetime(year=1987, month=8, day=3)},

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
