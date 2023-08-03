# hw-8

<img width="625" alt="Screenshot 2023-08-03 at 16 07 10" src="https://github.com/slav0ntech/hw-8/assets/131975866/f342c3f6-0eb9-4c6c-bdef-4612f66abcd0">


How it works:

Python script for output people, which need to happy birthday.
Users whose birthday was on the weekend should be congratulated on Monday.
The function displays users with birthdays one week ahead of the current day.
The week starts from Monday

for example, next list with names and birthdays:
```
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
```
after work **main.py** :
```
Monday: Dyadya Vanya, Petro 
Wednesday: Olga 
Thursday: Timur
```
