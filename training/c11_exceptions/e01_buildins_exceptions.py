# Builtins Errors 
for item in dir(__builtins__):
    if 'Error' in item:
        print(item)

print()

# ZeroDivisionError
# num = 1 / 0   

# NameError
# math.pi       

# SyntaxError
# if a == b     

# FileNotFoundError
# open('file.txt')

# TypeError
# [i for i in 5]

# ModuleNotFoundError
# import xyz

# ValueError
# num = int('hola')