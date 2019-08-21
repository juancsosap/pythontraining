import re

text = '''
En un lugar de Chile que no recuerdo, habia
una inscripción que decia que en 1993 habia
muerto mi amigo, a quien conocía desde 1980
cuando estaba coniciendo la ciudad que paso
a ser mi hogar entre el 2007 y el 2013.
'''

regex_string = r'20[0-2][0-9]|19[5-9][0-9]'
regex = re.compile(regex_string)
matches = regex.finditer(text)

for match in matches:
    start_idx, end_idx = match.span()
    print(text[start_idx:end_idx])

print()

matches = re.findall(regex, text)
print(matches)

