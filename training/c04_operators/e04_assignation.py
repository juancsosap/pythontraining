print('Basic Calc'.center(50))
print(''.center(50, '-'))
num1 = int(input('Num1: '))
num2 = int(input('Num2: '))
print(''.center(50, '-'))

# num1 = num1 + num2
num1 += num2
print('Addition'.ljust(20), ':', num1)

# num1 = num1 - num2
num1 -= num2
print('Subtraction'.ljust(20), ':', num1)

# num1 = num1 * num2
num1 *= num2
print('Multiplication'.ljust(20), ':', num1)

# num1 = num1 / num2
num1 /= num2
print('Divition'.ljust(20), ':', num1)

# num1 = num1 // num2
num1 //= num2
print('Integer Divition'.ljust(20), ':', num1)

# num1 = num1 ** num2
num1 **= num2
print('Power'.ljust(20), ':', num1)

# num1 = num1 % num2
num1 %= num2
print('Module'.ljust(20), ':', num1)

print(''.center(50, '-'))
