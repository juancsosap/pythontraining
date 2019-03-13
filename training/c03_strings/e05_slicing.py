text = "Juan Carlos Sosa Peña"
print(text)

# Getting one character
print(text[0], text[5], text[12], text[17])

# Getting a Slice of character
print(text[:4], text[5:11], text[12:16], text[17:])
print(text[:]) # All the string

# Getting a slice with steps
print(text[::2])
print(text[5::3])
print(text[:16:4])
print(text[5:16:5])

# Slicing Backward
print(text[-1], text[-6], text[-11], text[-18])
print(text[-9:])
print(text[0], text[-1]) # First and last char

# Getting first item
print(text[0])
print(text[-len(text)])

# Getting last item
print(text[-1])
print(text[len(text)-1])
