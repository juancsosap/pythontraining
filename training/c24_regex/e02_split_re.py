import re

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


regex1 = r'<PERSON id=\d+>'
regex2 = r'<\w+>'

split_text = re.split(regex1, text, flags=re.IGNORECASE)

print(split_text)

print()

for item in map(lambda t : t.replace('\n', '').strip(), split_text[1:]):
    print(item)

print()

transform1 = lambda t : t.replace('\n', '').strip()

for item in map(transform1, split_text[1:]):
    print('-'*20)
    split_item = re.split(regex2, item)
    print(split_item)

print()

transform2 = lambda t : (t[t.find('</')+2:t.find('>')], t[:t.find('</')])

for item in map(transform1, split_text[1:]):
    print('-'*20)
    split_item = re.split(regex2, item)
    for (key, value) in map(transform2, split_item[1:]):
        print('{}: {}'.format(key, value))
