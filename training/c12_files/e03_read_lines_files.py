basedir = __file__[:__file__.rfind('/')+1]

path = basedir + 'docs/doc.txt'

with open(path) as file:
    # Get lines using for loop
    for line in file:
        print(line, end='')
    print()

print('\n', '#' * 70, '\n')

with open(path) as file:
    # read one line at time
    line = file.readline()
    print(line, end='')

    line = file.readline()
    print(line, end='')

print('\n', '#' * 70, '\n')

with open(path) as file:
    # read all lines
    lines = file.readlines()
    print(lines)
    for line in lines:
        print(line, end='')

print()