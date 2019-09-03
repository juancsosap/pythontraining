basedir = __file__[:__file__.rfind('/')+1]

path = basedir + 'docs/doc.txt'

# Opening File
file = open(path)

print(type(file))
print(dir(file))

# Closing File
file.close()

# Safer opening of the file
try:
    file = open(path)
    # Rest of commands
except:
    print('Error')
finally:
    file.close()

# Auto closing the file
with open(path) as file:
    pass

# Opening modes
''' 'r' 	Open a file for reading. (default)
    'w' 	Open a file for writing. Creates a new file if it does not exist or truncates the 
                 file if it exists.
    'x' 	Open a file for exclusive creation. If the file already exists, the operation fails.
    'a' 	Open for appending at the end of the file without truncating it. Creates a new file
                 if it does not exist.
    't' 	Open in text mode. (default)
    'b' 	Open in binary mode.
    '+' 	Open a file for updating (reading and writing) '''

with open(file=path, mode='rt', encoding='utf-8') as file:
    pass
