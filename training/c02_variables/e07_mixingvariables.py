# Mixing int + float
num = 1 + 1.0
print(type(num), num)

# Mixing int + complex
num = 1 + (1 + 1j)
print(type(num), num)

# Mixing float + complex
num = 1.0 + (1 + 1j)
print(type(num), num)

# Mixing int + bool
num = 1 + True # True --> 1 , False --> 0
print(type(num), num)

# Mixing float + bool
num = 1.0 + True # True --> 1 , False --> 0
print(type(num), num)

# Mixing complex + bool
num = 1j + True # True --> 1 , False --> 0
print(type(num), num)

# Mixing int + string
num = str(1) + "123" # Not valid
print(type(num), num)
