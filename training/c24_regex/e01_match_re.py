import re

print('\n', [item for item in dir(re) if not item.startswith('__')])

print()

date_str = input('Birthday: ')

# Date Regex
year_re_str = r'(20[0-4][0-9]|19[5-9][0-9])'
month_re_str = r'(0[1-9]|1[1-2])'
day_re_str = r'(0[1-9]|[1-2][0-9]|3[0-1])'
date_re_str = '{}-{}-{}'.format(day_re_str, month_re_str, year_re_str)

if re.match(date_re_str, date_str):
    print('Valid date')
else:
    print('Invalid date')
