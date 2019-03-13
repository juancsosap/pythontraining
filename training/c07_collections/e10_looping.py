# For Each loop could be used to read the elements of the collection
days = ('DOM', 'LUN', 'MAR', 'MIE', 'JUE', 'VIE', 'SAB')
for day in days:
    print(day)

print('-------------------------------------------------------------')

# For Each loop could not be used to modify the values of the elements of a collection
primes = [2, 3, 5, 7, 11, 13, 17, 19]
for prime in primes:
    prime += 1
print(primes)

# Loop using Indexes could be used to modify the elements of a collection
for i in range(len(primes)):
    primes[i] += 1
print(primes)

print('-------------------------------------------------------------')

# Looping with tuples
days = [(1, 'DOM', 'Domingo'),
        (2, 'LUN', 'Lunes'),
        (3, 'MAR', 'Martes'),
        (4, 'MIE', 'Miercoles'),
        (5, 'JUE', 'Jueves'),
        (6, 'VIE', 'Viernes'),
        (7, 'SAB', 'Sabado')]
for (num, code, name) in days:
    print(name, 'es el día número', num, 'de la semana, tambien llamado', code)

print('-------------------------------------------------------------')

# Looping accross strings (char collection)
text = 'Juan Carlos Sosa'
for letter in text:
    print(letter, end=',')
print()

print('-------------------------------------------------------------')

data = {'name': 'Juan',
        'surname': 'Sosa',
        'country': 'Chile'}
# For Each loop with keys could be used to modify the values of the elements of a collection
for key in data:
    data[key] = data[key].lower()

for key in data.keys():
    print(key, data[key])

# For Each loop with values could not be used to modify the values of the elements of a collection
# For Each loop could be used to read the elements of the collection
for value in data.values():
    value = value.upper()

for (key, value) in data.items():
    print(key, value)
