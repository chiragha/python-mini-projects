
from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

print('Enter your birthdate (dd mm yyyy format):')
day, month, year = map(int, input().split())
birthdate = date(year, month, day)

age = calculate_age(birthdate)
print(f'Your age is {age}')  