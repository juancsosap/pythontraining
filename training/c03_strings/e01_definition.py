text = "String Text"
print(text)
print(type(text))
print(dir(str), end="\n\n")

# Using " "
text = "--> Hello... How are you?"
print(text)

# Using ' '
text = '<-- Fine, thanks'
print(text)

# Using """ """
text = """--> Where were you yesterday?"""
print(text)

# Using ''' '''
text = '''<-- I was working'''
print(text)

print()

# Conflict with the delimiter symbol used
# text = 'I'm working today too' # Not valid
text = "I'm working today too"
print(text)
# text = "I "love" my work" # Not valid
text = 'I "love" my work'
print(text)
# text = "I'd been "playing" all day in the work" # Not valid
# text = 'I'd been "playing" all day in the work' # Not valid
text = '''I'd been "playing" all day in the work'''
text = """I'd been "playing" all day in the work"""
print(text)

print()

# Scaping Characters
text = 'I\'m working today'
print(text)
text = "He said all days: \"I want to go Home\"."
print(text)

# Scaping Characters Commands
text = 'Name\tSurname' # \t print a TAB space
print(text)
text = 'Juan\nSosa' # \n print an ENTER
print(text)
text = 'Eduardo Carlos\rSosa' # \r return the cursor to the begining of the line
print(text)
text = 'Luis\vSosa' # \v move the cursor vertically
print(text)

print()

# Scaping Characters Symbols
text = ' \u2181 First Element'
print(text)
text = ' \u2181 Second Element'
print(text)

# Multiline String
text = '''
This long text will be printed as
it is write
'''
text = """
This long text will be printed as
it is write
"""
print(text)

# Concatenating texts
text1 = "Hello"
text2 = "World"
text = text1 + " " + text2
print(text)

# Multiplying Strings
text = "Hello "
text = 5 * text
print(text)

# Converting number to text
text = str(123)
print(type(text), text)

# Concatenating strings with non string values
# text = "Age: " + 25 # not valid
text = "Age: " + str(25)
print(text)

# Unicode String
ustr = u"\u00dcnic\u00f6de"
nstr = "\u00dcnic\u00f6de"
print(ustr)
print(ustr == nstr)

# Raw String
rstr = r"c:\documents\newfile.txt"
print(rstr)

# Format String
n1, n2 = 5, 10
fstr = f"{n1} + {n2} = {n1 + n2}"
print(fstr)

# Byte String
bstr = b'hello'
print(bstr)
