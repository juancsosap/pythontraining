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
match = regex.search(text)

while(match):
    start_idx = match.start()
    end_idx = match.end()
    print(match.group(0), start_idx, end_idx)
    match = regex.search(text, end_idx)

print()

text = '''
<people>
    <person id=1>
        <name>Juan</name>
        <surname>Sosa</surname>
    </person>
    <person id=2>
        <name>Luis</name>
        <surname>Perez</surname>
    </person>
    <person id=3>
        <name>Andres</name>
        <surname>Lopez</surname>
    </person>
</people>
'''

regex1 = r'[\n\t ]'
regex2 = r'\<person.*\>'
replace_text = re.match(regex1, text)
split_text = re.split(regex2, text)

print(replace_text)
print(split_text)