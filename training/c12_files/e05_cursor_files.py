path = 'docs/doc.txt'

with open(path) as file:
    pos = file.tell()
    text = file.read(50)
    print(pos, text)

    pos = file.tell()
    text = file.read(50)
    print(pos, text)

    # Change the cursor position
    file.seek(20)

    pos = file.tell()
    text = file.read(50)
    print(pos, text)

