import re

text = '''
Juan Carlos Sosa        26-03-1982
José Luis Perez         15-04-1967
Antonio Rodrigez        17-05-2000
Ana Esperanza Pita      23-10-1993
'''

regex_string = r'(\d{2})-(\d{2})-(\d{4})'
regex = re.compile(regex_string)
match = regex.search(text)

while(match):
    start_idx = match.start()
    end_idx = match.end()
    groups = match.groups()
    print('Groups :', groups)
    print('Text :', text[start_idx:end_idx])
    # Group 0 is everything
    # Each other groups are indexed from 1
    for i in range(len(groups) + 1):
        print('Group', i, ':', match.group(i))
    match = regex.search(text, end_idx)
    print('-'*10)

regex_string = r'(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d{4})'
regex = re.compile(regex_string)
matches = regex.finditer(text)

for match in matches:
    start_idx, end_idx = match.span()
    print(text[start_idx:end_idx])
    groups = match.groups()
    print('day   :', match.group('day'))
    print('month :', match.group('month'))
    print('year  :', match.group('year'))
    print(match.groupdict())
    print('-'*10)
