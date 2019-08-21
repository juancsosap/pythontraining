import re

text = '''
Juan Carlos Sosa        26-03-1982
José Luis Perez         15-04-1967
Antonio Rodrigez        17-05-2000
Ana Esperanza Pita      23-10-1993
'''

regex_string = r'(\d{2})-(\d{2})-(\d{2})(\d{2})'

regex = re.compile(regex_string)
matches = regex.finditer(text)

for match in matches:
    start_idx, end_idx = match.span()
    print(text[start_idx:end_idx])
    print(match.groups())
    print('-'*10)

text1 = re.sub(regex_string, lambda x : x.group(0)[:-4] + x.group(0)[-2:], text)

print(text1)

sub_regex = r'\1/\2/\4'
text2 = re.sub(regex_string, sub_regex, text)

print(text2)