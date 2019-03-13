# Dinamic Memory allocation
num = 123
print(type(num), end="\n\n")

num = 1
print(num, num.bit_length(), "0b{0:b}".format(num), sep=" : ", end="\n\n")

num = 1000
print(num, num.bit_length(), "0b{0:b}".format(num), sep=" : ", end="\n\n")

num = 12345678901234567890
print(num, num.bit_length(), "0b{0:b}".format(num), sep=" : ", end="\n\n")

# Too long numbers are supported
num = 1234567890123456789012345678901234567890123456789012345678901234567890
print(num, num.bit_length(), sep=" : ", end="\n\n")

# Where 8 bits are 1 Byte

# The under-scope (_) symbol could be used as thousand separator
num = 123_123_123_123
print(num, end="\n\n")
