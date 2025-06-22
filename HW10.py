import  datetime

def local_date ():
    now = datetime.datetime.now()
    print(now.date(),'\n')

local_date()

def utc_datetime ():
    now = datetime.datetime.now()
    utc_current_datetime = now.astimezone(datetime.timezone.utc)
    print(utc_current_datetime, '\n')

utc_datetime ()

# Ex.2
from datetime import datetime, timedelta

current_date = datetime.now()
print('The next five days are: ')
for i in range(5):
    next_date = current_date + timedelta(days=i)
    formatted_date = next_date.strftime('%A')
    print(formatted_date,)
print('\n')

#Ex.3
import datetime

current_date2 = datetime.datetime.now()
formatted_days = current_date2.strftime('%d')
formatted_months = current_date2.strftime('%m')
formatted_years = current_date2.strftime('%Y')

print(formatted_days + '/' + formatted_months +'/' + formatted_years, '\n')

# Ex.4
import random

def random_index ():
    p1 = ['Who', 'let', 'the', 'dogs', 'out?']
    how_many_indexes = len(p1) -1
    random_index = random.randint(0, how_many_indexes)
    print(p1[random_index], '\n')

random_index()

# Ex.5
def reverse_own (original):
    string_char_rev = ""
    for char in original:
       string_char_rev = char + string_char_rev
    print(string_char_rev, '\n')

reverse_own('evol)

#Ex.6
def contain_any ():
    str1 = 'Humus'
    str2 = 'mus'
    if str2 in str1: print('Found!')
    else: print('Not found!')

contain_any()