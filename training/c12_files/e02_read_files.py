path = 'docs/doc.txt'

# Reading file
with open(path) as file:
    text = file.read()
    print(text)

print('\n', '#' * 70, '\n')

# 'r' 	Open a file for reading. (default)
with open(file=path, mode='r', encoding='utf-8') as file:
    text = file.read()
    print(text)

print('\n', '#' * 70, '\n')

# Read buffer
with open(path, encoding='utf-8') as rfile:
    text = rfile.read(10)
    print(text)
    text = rfile.read(10)
    print(text)
    text = rfile.read(10)
    print(text)
    text = rfile.read(10)
    print(text)
