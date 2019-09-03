# Texto de prueba
text = '''
An aware object has sufficient knowledge of 
applicable algorithmic and political time 
adjustments, such as time zone and daylight 
saving time information, to locate itself 
relative to other aware objects. An aware 
object is used to represent a specific moment 
in time that is not open to interpretation 1.

A naive object does not contain enough 
information to unambiguously locate itself 
relative to other date time objects. Whether 
a naive object represents Coordinated Universal 
Time , local time, or time in some other timezone
is purely up to the program, just like it is up 
to the program whether a particular number 
represents metres, miles, or mass. Naive 
objects are easy to understand and to work with, 
at the cost of ignoring some aspects of reality.
'''

# convertir todo el texto a minuscula
text = text.lower()

# elimina los saltos de linea
text = text.replace('\n', ' ').strip()

# elimina los simbolos
text = text.replace(',', '') \
           .replace('.', '') \
           .replace('  ', ' ')

# separa las palabras
split_text = text.split(' ')

# contabiliza la cantidad de veces que se presenta
# cada palabra
register = dict()
for word in split_text:
    if(not word.isnumeric()):
        if(len(word) > 3):
            register[word] = register.get(word, 0) + 1

# imprime una tabla con el listado de las palabras
print('{:20} {:20}'.format('Word', 'Quantity'))
print('-'*40)
for key, value in register.items():
    print('{:20} {:20}'.format(key, str(value)))    
print('-'*40)

# determina cual palabra se presenta con más frecuencia
max_quantity = 0
for key, value in register.items():
    if(value > max_quantity):
        max_quantity = value
        max_word = key

# determina cual es la palabra más larga
max_len = 0
for key in register:
    if(len(key) > max_len):
        max_len = len(key)
        max_word_len = key

# determina cual es la palabra más corta
min_len = 1_000_000_000
for key in register:
    if(len(key) < min_len):
        min_len = len(key)
        min_word_len = key

print ('the most frequently word is "{}" with {} times'.format(
                 max_word,     max_quantity))
print ('the longest word is "{}" with {} letter(s)'.format(
                 max_word_len,     max_len))
print ('the shortest word is "{}" with {} letter(s)'.format(
                 min_word_len,     min_len))
