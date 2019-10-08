# Text Length
text = 'Juan Carlos Sosa'
size = len(text)
print(size)

# Text transformation
text = 'how are you?'
print('capitalize -> ', text.capitalize())
print('upper ------> ', text.upper())
print('lower ------> ', text.lower())
print('swapcase ---> ', text.swapcase())

print('\n---------------------', end="\n\n")

# Text Validation
text = 'FINE, THANKS'
print('endswith ---> ', text.endswith('s'))
print('startswith -> ', text.startswith('F'))
print('isupper ----> ', text.isupper()) # Return True if all the text is uppercase
print('islower ----> ', text.islower()) # Return True if all the text is lowercase
text = '123'
print('isalnum ----> ', text.isalnum()) # Return True if all the text has alpha or numeric chars
print('isalpha ----> ', text.isalpha()) # Return True if all the text has alpha chars
print('isnumeric --> ', text.isnumeric()) # Return True if all the text has numeric chars
text = ' \t'
print('isprintable > ', text.isprintable()) # Return True if all the text has printable chars
print('isspace ----> ', text.isspace()) # Return True if all the text has not printable chars

print('\n---------------------', end="\n\n")

# Text Modification
text = '''Python es un lenguaje de programación interpretado cuya filosofía
hace hincapié en una sintaxis que favorezca un código legible.
Se trata de un lenguaje de programación multiparadigma, ya que
soporta orientación a objetos, programación imperativa y, en
menor medida, programación funcional. Es un lenguaje interpretado,
usa tipado dinámico y es multiplataforma.'''
# Replace all the occurrences of the word
print('replace ----> ', text.replace('\n', ' '))
print('##########################################')
print('replace ----> ', text.replace('lenguaje', 'LENGUAJE', 2))

print('\n---------------------', end="\n\n")

# Text Layout
text = 'Python es un lenguaje de programación interpretado'
print('center ---> |', text.center(60), '|')
print('center ---> |', text.center(60, '#'), '|')
print('ljust ----> |', text.ljust(60), '|')
print('ljust ----> |', text.ljust(60, '#'), '|')
print('rjust ----> |', text.rjust(60), '|')
print('rjust ----> |', text.rjust(60, '#'), '|')
text = '1234'
print('zfill ----> |', text.zfill(10), '|')
# print('rjust ----> |', text.rjust(10, '0'), '|')

print('\n---------------------', end="\n\n")

# Strip Spaces from Text
text = '   --- Python ---   '
print('strip -----> |', text.strip(), '|')
print('lstrip ----> |', text.lstrip(), '|')
print('rstrip ----> |', text.rstrip(), '|')
text = '---    Python    ---'
print('strip -----> |', text.strip('-'), '|')
print('lstrip ----> |', text.lstrip('-'), '|')
print('rstrip ----> |', text.rstrip('-'), '|')

print('\n---------------------', end="\n\n")

# Split Text
text = 'juan.sosa@company.com'
print('partition ----> |', text.partition('@'), '|')
print('partition ----> |', text.partition('.'), '|')
print('rpartition ----> |', text.rpartition('.'), '|')
print('partition ----> |', text.partition('-'), '|')

print('\n---------------------', end="\n\n")

# IndexOf
index = text.find('@')
print('find -----> |', index, '|')
print('find -----> |', text.find('.'), '|')
print('find -----> |', text.find('-'), '|')
print('find -----> |', text.find('.', index), '|')
print('rfind ----> |', text.rfind('.'), '|')
print('rfind ----> |', text.rfind('.', index), '|')
print('rfind ----> |', text.rfind('.', 0, index), '|')

print('\n---------------------', end="\n\n")

# Split Text
print('split -----> |', text.split('.'), '|')
print('split -----> |', text.split('.', 1), '|')
print('rsplit ----> |', text.rsplit('.'), '|')
print('rsplit ----> |', text.rsplit('.', 1), '|')
text = '''Python es un lenguaje de programación interpretado cuya filosofía
hace hincapié en una sintaxis que favorezca un código legible.
Se trata de un lenguaje de programación multiparadigma, ya que
soporta orientación a objetos, programación imperativa y, en
menor medida, programación funcional. Es un lenguaje interpretado,
usa tipado dinámico y es multiplataforma.'''
print('splitline -> |', text.splitlines(), '|')
#print('split     -> |', text.split('\n'), '|')
print('splitline -> |', text.splitlines(True), '|')

print('\n---------------------', end="\n\n")

# Other text Methods
text = 'Hello'
print('Reversed :', reversed(text))
print('Length   :', len(text))
