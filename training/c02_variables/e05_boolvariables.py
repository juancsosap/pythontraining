# Only True or False values are valid (not true or flase)
# It's storage in 1 bit

flag = True
print(type(flag), end="\n\n")
print(dir(bool), end="\n\n")
print(flag.bit_length(), end="\n\n")
