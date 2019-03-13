# Foating point number of 8 bytes (double)

num = 123.123
print(type(num), end="\n\n")
print(dir(float), end="\n\n")

num = 1234.5678901234560
print(num, end="\n\n")

# Up to 16 digits of pressition
# The rest of digits are loss
num = 1234.56789012345678901234567890
print(num, end="\n\n")

num = 1234567890123456.78901234567890
print(num, end="\n\n")

# after max the pressition is reach, the number is represented in scientific notation
num = 12345678901234567.8901234567890
print(num, end="\n\n")

# equivalen to 1.23456789123456 x 10^100
num = 1.23456789012345678901234567890e+100
print(num, end="\n\n")

# Biggest number that could represent
num = 1.7976931348623158e+308
print(num, end="\n\n")

# Over the biggest number it is categorized as Infinity
num = 1.7976931348623159e+308
print(num, end="\n\n")

# Smallest number that could represent
num = 5e-324
print(num, end="\n\n")

# Under the Smallest number it is pass to 0.0
num = 5e-325
print(num, end="\n\n")

# the float class has a method to verify if the content is or not an Integer
num = 123.123
print(num.is_integer(), end="\n\n")

num = 123.0
print(num.is_integer(), end="\n\n")
