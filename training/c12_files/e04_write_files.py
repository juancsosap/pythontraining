basedir = __file__[:__file__.rfind('/')+1]

path = basedir + 'docs/doc.txt'
copy_path = basedir + 'docs/doc-copy.txt'

# Write file
with open(path, 'r', encoding='utf-8') as rfile:
    text = rfile.read()
    with open(copy_path, 'w', encoding='utf-8') as wfile:
        wfile.write(text + '\n\n')
        wfile.write(text + '\n\n')
    with open(copy_path, 'w', encoding='utf-8') as wfile:
        wfile.write(text + '\n\n')
        wfile.write(text + '\n\n')
    
print('\n', '#' * 70, '\n')

# Append to an existing file
with open(path, 'r', encoding='utf-8') as rfile:
    text = rfile.read()
    with open(copy_path, 'a', encoding='utf-8') as wfile:
        wfile.write(text + '\n\n')
        wfile.write(text + '\n\n')

# Write Lines to a file
with open(path, encoding='utf-8') as rfile:
    lines = rfile.readlines()
    with open(copy_path, 'a', encoding='utf-8') as wfile:
        wfile.writelines(lines)
